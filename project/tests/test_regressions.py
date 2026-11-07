"""Stage 8 regression tests for the two prepared data-store defects.

F8-01: practitioner conflict (FR-05, AC-04.1 / AC-04.2, BR-05).
F8-02: cancelled appointment remains retrievable (FR-06/07/08, BR-07,
AC-05.2 / AC-05.3).
"""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


WHEN = datetime(2026, 10, 1, 9, 0)


def build_store() -> tuple[SmartCareDataStore, AppointmentService]:
    """Return a fresh store with synthetic P1, P2, D1 and D2 registered."""
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    patients.register_patient('P1', 'Alex Example')
    patients.register_patient('P2', 'Sam Example')
    practitioners = PractitionerService(data_store)
    practitioners.register_practitioner('D1', 'Taylor Example', 'General')
    practitioners.register_practitioner('D2', 'Morgan Example', 'General')
    return data_store, AppointmentService(data_store)


def test_f8_01_same_practitioner_same_time_rejected_other_allowed() -> None:
    """F8-01: same practitioner/exact time conflicts; another may book."""
    data_store, appointments = build_store()
    original = appointments.book_appointment('A1', 'P1', 'D1', WHEN)

    with pytest.raises(ValueError):
        appointments.book_appointment('A2', 'P2', 'D1', WHEN)
    assert data_store.list_appointments() == [original]
    assert data_store.find_appointment('A2') is None

    other = appointments.book_appointment('A3', 'P2', 'D2', WHEN)
    assert other.status is AppointmentStatus.SCHEDULED
    assert data_store.list_appointments() == [original, other]


def test_f8_02_cancelled_appointment_remains_retrievable() -> None:
    """F8-02: cancelled history is still found by store and service."""
    data_store, appointments = build_store()
    appointment = appointments.book_appointment('A1', 'P1', 'D1', WHEN)

    cancelled = appointments.cancel_appointment('A1')
    assert cancelled is appointment
    assert appointment.status is AppointmentStatus.CANCELLED
    assert data_store.list_appointments() == [appointment]
    assert data_store.find_appointment('A1') is appointment
    assert appointments.find_appointment('A1') is appointment

    with pytest.raises(ValueError):
        appointments.cancel_appointment('A1')
    assert appointment.status is AppointmentStatus.CANCELLED
    assert data_store.list_appointments() == [appointment]
