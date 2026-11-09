from datetime import datetime

from smartcare.domain import Appointment, Patient, Practitioner, AppointmentStatus
from smartcare.queries import select_appointments
from smartcare.queries import select_appointments, appointment_sort_key
import pytest
from smartcare.data_store import SmartCareDataStore
from smartcare.services import AppointmentService, PractitionerService



#QRY-01
def test_practitioner_isolation():
    patient = Patient('P1', "Alex")
    d1 = Practitioner('D1', 'Dr Taylor', 'General')
    d2 = Practitioner('D2', 'Dr Sam', 'General')

    a1 = Appointment('A1', patient, d1, datetime(2026, 11, 13, 9, 0))
    a2 = Appointment('A2', patient, d2, datetime(2026, 11, 13, 10, 0))

    result = select_appointments([a1, a2], 'D1')

    assert result == [a1]
    assert a2 not in result

#QRY-02
def test_status_filter():
    from smartcare.domain import AppointmentStatus

    patient = Patient('P1', "Alex")
    practitioner = Practitioner('D1', 'Dr Sam', 'General')

    a1 = Appointment('A1', patient, practitioner, datetime(2026, 11, 13, 9))
    a2 = Appointment('A2', patient, practitioner, datetime(2026, 11, 13, 10))

    a2.cancel()

    appointments = [a1, a2]

    assert select_appointments(appointments, 'D1') == [a1, a2]
    assert select_appointments(
        appointments, 'D1', AppointmentStatus.SCHEDULED
    ) == [a1]
    assert select_appointments(
        appointments, 'D1', AppointmentStatus.CANCELLED
    ) == [a2]
    assert select_appointments(
        appointments, 'D1', AppointmentStatus.COMPLETED
    ) == []

#QRY-03
def test_appointment_sorting():
    patient = Patient('P1', 'Alex')
    practitioner = Practitioner('D1', 'Dr Sam', 'General')

    a1 = Appointment('A1', patient, practitioner, datetime(2026, 11, 13, 10))
    a2 = Appointment('A2', patient, practitioner, datetime(2026, 11, 13, 9))
    a3 = Appointment('A3', patient, practitioner, datetime(2026, 11, 13, 10))

    appointments = [a3, a1, a2]
    original_order = appointments.copy()
    original_fields = [
        (a.appointment_id, a.date_time, a.status)
        for a in appointments
    ]

    result = select_appointments(appointments, 'D1')

    assert result == [a2, a1, a3]
    assert appointments == original_order
    assert [
        (a.appointment_id, a.date_time, a.status)
        for a in appointments
    ] == original_fields
    assert result is not appointments


#QRY-04
def test_service_validation():
    store = SmartCareDataStore()
    practitioner_service = PractitionerService(store)
    appointment_service = AppointmentService(store)

    #D1 registered with no appointments
    practitioner_service.register_practitioner(
        'D1', 'Dr Sam', 'General'
    )

    #Practitioner that is known with no appointments
    result = appointment_service.list_practitioner_appointments('D1')
    assert result == []

    #Return a new empty list
    second_result = appointment_service.list_practitioner_appointments('D1')
    assert result is not second_result

    #Unknown practitioner that is valid
    with pytest.raises(LookupError):
        appointment_service.list_practitioner_appointments('D2')

    #Practitioner ID blank
    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments('')


    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments('   ')


    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments(
            'D1', 'scheduled'
        )

    #Status not matched to known practitioner
    assert appointment_service.list_practitioner_appointments(
        'D1', AppointmentStatus.CANCELLED
    ) == []



#FP-01
def test_repeated_calls():
    patient = Patient('P1', 'Alex')
    practitioner = Practitioner('D1', 'Dr Sam', 'General')

    a1 = Appointment('A1', patient, practitioner, datetime(2026, 11, 13, 10))
    a2 = Appointment('A2', patient, practitioner, datetime(2026, 11, 13, 9))

    appointments = [a1, a2]

    first_result = select_appointments(appointments, 'D1')
    second_result = select_appointments(appointments, 'D1')

    assert first_result == second_result
    assert first_result == [a2, a1]
    assert appointments == [a1, a2]
    assert first_result is not second_result

#FP-02
def test_fresh_lists():
    patient = Patient('P1', 'Alex')
    practitioner = Practitioner('D1', 'Dr Sam', 'General')

    a1 = Appointment('A1', patient, practitioner, datetime(2026, 11, 13, 9))
    a2 = Appointment('A2', patient, practitioner, datetime(2026, 11, 13, 10))

    for appointments in ([], [a1, a2], [a2, a1]):
        original_order = appointments.copy()
        original_fields = [
            (a.appointment_id, a.date_time, a.status)
            for a in appointments
        ]

        result = select_appointments(appointments, 'D1')

        assert result == sorted(
            appointments,
            key=lambda a: (a.date_time, a.appointment_id),
        )
        assert result is not appointments
        assert appointments == original_order
        assert [
            (a.appointment_id, a.date_time, a.status)
            for a in appointments
        ] == original_fields


#FP-03
def test_named_sorting_key():
    patient = Patient('P1', 'Alex')
    practitioner = Practitioner('D1', 'Dr Sam', 'General')

    a1 = Appointment('A1', patient, practitioner, datetime(2026, 11, 13, 10))
    a2 = Appointment('A2', patient, practitioner, datetime(2026, 11, 13, 9))

    #Named key returns the correct values
    assert appointment_sort_key(a1) == (
        datetime(2026, 11, 13, 10), 'A1'
    )

    #Query returns appointments in the correct order
    result = select_appointments([a1, a2], 'D1')

    assert result == [a2, a1]
