"""Stage 7 domain checks: construction, validation and cancellation."""

from datetime import datetime, timezone

import pytest

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)

WHEN = datetime(2026, 10, 1, 9)


def build_appointment(**overrides: object) -> Appointment:
    """Create a valid appointment, replacing any named fields."""
    fields = {
        'appointment_id': 'A1',
        'patient': Patient('P1', 'Alex Example'),
        'practitioner': Practitioner('D1', 'Taylor Example', 'General'),
        'date_time': WHEN,
    }
    fields.update(overrides)
    return Appointment(**fields)


def test_patient_stores_valid_fields() -> None:
    """TEST-01: a valid patient exposes its trimmed ID and name."""
    patient = Patient(' P1 ', ' Alex Example ')

    assert patient.patient_id == 'P1'
    assert patient.name == 'Alex Example'


@pytest.mark.parametrize('blank_id', ['', '   '])
def test_blank_patient_id_is_rejected(blank_id: str) -> None:
    """TEST-02: blank and whitespace-only patient IDs raise ValueError."""
    with pytest.raises(ValueError):
        Patient(blank_id, 'Alex Example')


def test_whitespace_patient_name_is_rejected() -> None:
    """TEST-03: a whitespace-only patient name raises ValueError."""
    with pytest.raises(ValueError):
        Patient('P1', '   ')


def test_practitioner_stores_valid_fields() -> None:
    """TEST-04: a valid practitioner exposes its ID, name and specialty."""
    practitioner = Practitioner('D1', 'Taylor Example', 'General')

    assert practitioner.practitioner_id == 'D1'
    assert practitioner.name == 'Taylor Example'
    assert practitioner.specialty == 'General'


@pytest.mark.parametrize(
    ('practitioner_id', 'name', 'specialty'),
    [
        ('', 'Taylor Example', 'General'),
        ('D1', '   ', 'General'),
        ('D1', 'Taylor Example', ''),
    ],
)
def test_blank_practitioner_fields_are_rejected(
    practitioner_id: str,
    name: str,
    specialty: str,
) -> None:
    """TEST-05: each blank required practitioner field raises ValueError."""
    with pytest.raises(ValueError):
        Practitioner(practitioner_id, name, specialty)


def test_new_appointment_starts_scheduled() -> None:
    """TEST-06: a new appointment is SCHEDULED with its given details."""
    patient = Patient('P1', 'Alex Example')
    practitioner = Practitioner('D1', 'Taylor Example', 'General')

    appointment = Appointment('A1', patient, practitioner, WHEN)

    assert appointment.status is AppointmentStatus.SCHEDULED
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == WHEN


@pytest.mark.parametrize(
    'invalid_field',
    [
        {'patient': 'P1'},
        {'practitioner': 'D1'},
        {'status': 'cancelled'},
        {'date_time': '2026-10-01 09:00'},
        {'date_time': datetime(2026, 10, 1, 9, 0, 30)},
        {'date_time': datetime(2026, 10, 1, 9, 0, 0, 1)},
        {'date_time': datetime(2026, 10, 1, 9, tzinfo=timezone.utc)},
    ],
)
def test_appointment_rejects_invalid_inputs(invalid_field: dict) -> None:
    """TEST-07: invalid participant, status and time values raise ValueError."""
    with pytest.raises(ValueError):
        build_appointment(**invalid_field)


def test_cancel_changes_status() -> None:
    """TEST-08: cancelling changes SCHEDULED to CANCELLED."""
    appointment = build_appointment()

    appointment.cancel()

    assert appointment.status is AppointmentStatus.CANCELLED


def test_repeated_cancel_is_rejected() -> None:
    """TEST-09: a second cancel raises ValueError and keeps CANCELLED."""
    appointment = build_appointment()
    appointment.cancel()

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status is AppointmentStatus.CANCELLED


def test_completed_appointment_cannot_be_cancelled() -> None:
    """TEST-10: cancelling COMPLETED raises ValueError and keeps COMPLETED."""
    appointment = build_appointment(status=AppointmentStatus.COMPLETED)

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status is AppointmentStatus.COMPLETED
