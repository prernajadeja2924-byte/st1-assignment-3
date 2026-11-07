
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService


def test_find_registered_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    original = service.register_patient("P001", "Alex Smith")
    found = service.find_patient("P001")

    assert found is original
    assert found.patient_id == "P001"
    assert found.name == "Alex Smith"


import pytest


def test_find_patient_returns_original_object():
    store = SmartCareDataStore()
    service = PatientService(store)

    original = service.register_patient("P001", "Alex Smith")
    found = service.find_patient("P001")

    assert found is original


def test_find_unknown_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(LookupError):
        service.find_patient("P999")


def test_find_blank_patient_id():
    store = SmartCareDataStore()
    service = PatientService(store)

    with pytest.raises(ValueError):
        service.find_patient("   ")


def test_rejected_lookup_preserves_patient():
    store = SmartCareDataStore()
    service = PatientService(store)

    original = service.register_patient("P001", "Alex Smith")

    with pytest.raises(LookupError):
        service.find_patient("P999")

    assert service.find_patient("P001") is original


from smartcare.services import PractitionerService


def test_find_registered_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    original = service.register_practitioner(
        "D001", "Taylor Smith", "General"
    )
    found = service.find_practitioner("D001")

    assert found is original
    assert found.practitioner_id == "D001"
    assert found.name == "Taylor Smith"


def test_find_practitioner_returns_original_object():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    original = service.register_practitioner(
        "D001", "Taylor Smith", "General"
    )

    assert service.find_practitioner("D001") is original


def test_find_unknown_practitioner():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(LookupError):
        service.find_practitioner("D999")


def test_find_blank_practitioner_id():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    with pytest.raises(ValueError):
        service.find_practitioner("   ")


def test_rejected_practitioner_lookup_preserves_record():
    store = SmartCareDataStore()
    service = PractitionerService(store)

    original = service.register_practitioner(
        "D001", "Taylor Smith", "General"
    )

    with pytest.raises(LookupError):
        service.find_practitioner("D999")

    assert service.find_practitioner("D001") is original


from datetime import datetime, timedelta

from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import AppointmentService


def  cancellation_setup():
    store = SmartCareDataStore()

    patient = PatientService(store).register_patient(
        "P001", "Alex Smith"
    )
    practitioner = PractitionerService(store).register_practitioner(
        "D001", "Taylor Smith", "General"
    )

    service = AppointmentService(store)
    appointment = service.book_appointment(
        "A001",
        patient.patient_id,
        practitioner.practitioner_id,
        (datetime.now() + timedelta(days=7)).replace(second=0, microsecond=0)
    )

    return service, store, appointment


def test_cancel_scheduled_appointment():
    service, store, appointment = cancellation_setup()

    result = service.cancel_appointment("A001")

    assert result is appointment
    assert result.status == AppointmentStatus.CANCELLED


def test_cancelled_appointment_remains_in_history():
    service, store, appointment = cancellation_setup()

    service.cancel_appointment("A001")

    assert store.find_appointment("A001") is appointment
    assert appointment.status == AppointmentStatus.CANCELLED


def test_cancel_unknown_appointment():
    service, store, appointment = cancellation_setup()

    with pytest.raises(LookupError):
        service.cancel_appointment("A999")


def test_cancel_blank_appointment_id():
    service, store, appointment = cancellation_setup()

    with pytest.raises(ValueError):
        service.cancel_appointment("   ")


def test_cannot_cancel_twice():
    service, store, appointment = cancellation_setup()

    service.cancel_appointment("A001")

    with pytest.raises(ValueError):
        service.cancel_appointment("A001")

    assert appointment.status == AppointmentStatus.CANCELLED


def test_cannot_cancel_completed_appointment():
    service, store, appointment = cancellation_setup()

    # Arrange: create a completed appointment using the domain constructor.
    completed = Appointment(
        "A002",
        appointment.patient,
        appointment.practitioner,
        appointment.date_time + timedelta(minutes=30),
        status=AppointmentStatus.COMPLETED,
    )
    store.add_appointment(completed)

    # Act and Assert: cancellation must be rejected.
    with pytest.raises(ValueError):
        service.cancel_appointment("A002")

    # Verify that the rejected operation did not change stored data.
    assert completed.status is AppointmentStatus.COMPLETED
    assert store.find_appointment("A002") is completed
