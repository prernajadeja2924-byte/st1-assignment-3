
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
