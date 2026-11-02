"""Stage 6 service checks: lookup, cancellation and retained history."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def build_services() -> tuple[
    SmartCareDataStore,
    PatientService,
    PractitionerService,
    AppointmentService,
]:
    """Create fresh services that share one new store."""
    data_store = SmartCareDataStore()
    return (
        data_store,
        PatientService(data_store),
        PractitionerService(data_store),
        AppointmentService(data_store),
    )


def test_find_patient_returns_registered_patient() -> None:
    """TEST-11: lookup returns the same registered patient."""
    _, patient_service, _, _ = build_services()
    patient = patient_service.register_patient('P1', 'Alex Example')

    found = patient_service.find_patient('P1')

    assert found is patient
    assert found.name == 'Alex Example'


@pytest.mark.parametrize(
    ('patient_id', 'expected_error'),
    [
        ('missing', LookupError),
        ('p1', LookupError),
        ('', ValueError),
        ('   ', ValueError),
    ],
)
def test_find_patient_rejects_invalid_id(
    patient_id: str,
    expected_error: type[Exception],
) -> None:
    """TEST-13: invalid lookups raise the contract error and add nothing."""
    data_store, patient_service, _, _ = build_services()
    patient = patient_service.register_patient('P1', 'Alex Example')

    with pytest.raises(expected_error):
        patient_service.find_patient(patient_id)

    assert data_store.list_patients() == [patient]


def test_find_practitioner_returns_registered_practitioner() -> None:
    """TEST-14: lookup returns the same registered practitioner."""
    _, _, practitioner_service, _ = build_services()
    practitioner = practitioner_service.register_practitioner(
        'D1',
        'Taylor Example',
        'General',
    )

    assert practitioner_service.find_practitioner('D1') is practitioner


@pytest.mark.parametrize(
    ('practitioner_id', 'expected_error'),
    [
        ('missing', LookupError),
        ('', ValueError),
        ('   ', ValueError),
    ],
)
def test_find_practitioner_rejects_invalid_id(
    practitioner_id: str,
    expected_error: type[Exception],
) -> None:
    """TEST-15: invalid lookups raise the contract error and add nothing."""
    data_store, _, practitioner_service, _ = build_services()
    practitioner = practitioner_service.register_practitioner(
        'D1',
        'Taylor Example',
        'General',
    )

    with pytest.raises(expected_error):
        practitioner_service.find_practitioner(practitioner_id)

    assert data_store.list_practitioners() == [practitioner]


def test_unknown_appointment_id_raises_lookup_error() -> None:
    """TEST-21: unknown IDs raise LookupError and change nothing."""
    data_store, patient_service, practitioner_service, appointment_service = (
        build_services()
    )
    patient_service.register_patient('P1', 'Alex Example')
    practitioner_service.register_practitioner(
        'D1',
        'Taylor Example',
        'General',
    )
    appointment = appointment_service.book_appointment(
        'A1',
        'P1',
        'D1',
        datetime(2026, 10, 1, 9),
    )

    with pytest.raises(LookupError):
        appointment_service.find_appointment('A9')
    with pytest.raises(LookupError):
        appointment_service.cancel_appointment('A9')

    assert data_store.list_appointments() == [appointment]
    assert appointment.status is AppointmentStatus.SCHEDULED


def test_cancel_retains_same_appointment() -> None:
    """TEST-22: cancelling changes status and keeps the same record."""
    data_store, patient_service, practitioner_service, appointment_service = (
        build_services()
    )
    patient_service.register_patient('P1', 'Alex Example')
    practitioner_service.register_practitioner(
        'D1',
        'Taylor Example',
        'General',
    )
    appointment = appointment_service.book_appointment(
        'A1',
        'P1',
        'D1',
        datetime(2026, 10, 1, 9),
    )

    result = appointment_service.cancel_appointment('A1')

    assert result is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
    assert appointment_service.find_appointment('A1') is appointment
    assert data_store.list_appointments() == [appointment]


def test_repeated_service_cancel_is_rejected() -> None:
    """TEST-23: a second cancel raises ValueError and keeps the record."""
    data_store, patient_service, practitioner_service, appointment_service = (
        build_services()
    )
    patient_service.register_patient('P1', 'Alex Example')
    practitioner_service.register_practitioner(
        'D1',
        'Taylor Example',
        'General',
    )
    appointment = appointment_service.book_appointment(
        'A1',
        'P1',
        'D1',
        datetime(2026, 10, 1, 9),
    )
    appointment_service.cancel_appointment('A1')

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')

    assert appointment.status is AppointmentStatus.CANCELLED
    assert data_store.list_appointments() == [appointment]
