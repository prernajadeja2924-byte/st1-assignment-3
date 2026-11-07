# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register a patient with valid details and confirm the patient is stored successfully. | Attempt to register a patient with invalid or missing required details. | The valid patient is registered and retrievable; invalid registration raises the specified exception and does not add a record. |
| FR-05 Prevent practitioner conflict | Book a practitioner for an available appointment time and confirm the booking succeeds. | Attempt to book the same practitioner for a conflicting appointment time. | The first booking succeeds; the conflicting booking is rejected and no additional appointment is stored. |
| FR-06 Cancel appointment | Cancel an existing scheduled appointment using its valid ID. | Attempt to cancel an appointment that has already been cancelled. | The appointment status changes to `AppointmentStatus.CANCELLED`; repeated cancellation raises the appropriate exception. |
| FR-07 Retain cancelled history | Cancel an existing appointment and retrieve it from the data store afterward. | Check that cancellation does not delete the appointment from the data store. | `data_store.find_appointment(appointment_id) is appointment` and the appointment status remains `AppointmentStatus.CANCELLED`. |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.


**1. `assert True`**

**Judgement:** Weak/unclear

**Why:** This assertion always passes regardless of the program's behaviour. It does not check any actual result and cannot detect an incorrect implementation.

**2. `assert appointment is not None`**

**Judgement:** Weak/unclear

**Why:** This only confirms that an appointment object exists. It does not verify whether the appointment has the correct patient, practitioner, scheduled time or status. It may be useful as a basic existence check but is insufficient to prove successful booking or cancellation.

**3. `assert appointment.status == AppointmentStatus.CANCELLED`**

**Judgement:** Strong for stated behaviour

**Why:** This directly verifies that the appointment has the expected cancelled status. It is meaningful when used after performing a cancellation. However, it does not prove that the appointment remains stored or that invalid cancellations are rejected.

**4. `assert len(results) > 0`**

**Judgement:** Weak/unclear

**Why:** This only verifies that at least one result exists. It does not confirm that the correct record was returned or that the results satisfy the requested search criteria.

**5. `assert data_store.find_appointment('A1') is appointment`**

**Judgement:** Strong for stated behaviour

**Why:** This verifies that the data store returns the exact same appointment object for identifier `A1`. It provides meaningful evidence that the appointment remains retrievable, which supports FR-07 Retained History. However, it does not independently verify that the appointment's status is cancelled.
### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 

| Input or state | Expected result | Supporting requirement or contract |
|---|---|---|
| Blank patient identifier (`""`) | Reject the identifier with `ValueError`. No patient records should be changed. | Patient identifier validation contract. |
| Whitespace-only patient identifier (`"   "`) | Reject the identifier with `ValueError`. The existing patient records remain unchanged. | Patient identifier validation contract. |
| Whitespace-only patient name (`"   "`) | Reject patient construction or registration according to the domain validation contract. No invalid patient should be registered. | FR-01 Register Patient and patient name validation. |
| Two appointments for the same practitioner at the same time | Reject the second booking because the practitioner is already booked. The original appointment remains unchanged. | FR-05 Prevent Practitioner Conflict. |
| Cancelling a scheduled appointment | Change its status from `SCHEDULED` to `CANCELLED` and retain the appointment in the data store. | FR-06 Cancel Appointment and FR-07 Retain Cancelled History. |
| Cancelling an already-cancelled appointment | Reject the repeated cancellation with the exception specified by the domain contract. The appointment remains `CANCELLED`. | FR-06 and appointment status-transition validation. |
| Cancelling a completed appointment | Reject the invalid transition. The appointment remains `COMPLETED`. | Appointment status-transition validation contract. |
| Cancelling an unknown appointment ID | Raise `LookupError` without changing any stored appointments. | Appointment lookup and cancellation service contract. |
| Cancelling an appointment with a blank ID | Raise `ValueError` without changing stored appointments. | Appointment identifier validation contract. |

**Boundary testing explanation:**

Boundary tests examine invalid inputs and unusual states that may not be covered by ordinary successful test cases. These tests are important because SmartCare must reject invalid operations while preserving existing records and maintaining valid appointment states.

The expected exception for an invalid status transition must be confirmed against the revision 2 domain contract before implementing its test.

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | The test only checks that a patient object is not `None`. This does not prove that the correct patient was registered or that its details are valid. | Register a patient with valid details, retrieve the patient by ID and assert that the stored patient is the expected object with the correct information. |
| 2 | The test only checks that an appointment object is not `None`. It does not verify the appointment's practitioner, time or status. | Create an appointment and assert that the correct patient and practitioner are assigned, the scheduled time is correct and the initial status is `SCHEDULED`. |
| 3 | The test uses `assert True`, which always passes and does not verify any application behaviour. | Cancel a scheduled appointment and assert that its status changes to `CANCELLED` and the appointment remains retrievable from the data store. |
| 4 | The test assumes SmartCare sends an SMS notification after appointment cancellation, but the supplied activity does not establish SMS notifications as a requirement. | Verify that cancelling an appointment changes its status to `CANCELLED` without introducing unsupported notification behaviour. |
| 5 | The test assumes an SMS notification is sent when an appointment is booked, which is not established by the stated requirements. | Attempt to book a practitioner at an already-occupied time and assert that the conflicting booking is rejected without changing the existing appointment. |

**Reflection:** Passing tests are not automatically meaningful. Tests must trace to actual requirements and use assertions that can detect incorrect behaviour. GitHub Copilot suggestions should be reviewed critically, especially when they contain weak assertions or introduce functionality that is not part of the requirements.
### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
100% code coverage does not necessarily mean that software has been tested correctly. Code coverage measures which parts of the code were executed during testing, but it does not prove that the tests checked the correct behaviour.

For example, a test using `assert True` may execute a function and contribute to code coverage without checking whether the function produces the expected result.

Effective software verification requires meaningful assertions, positive and negative test cases, boundary testing and traceability to the actual requirements.

In the SmartCare project, tests should verify not only that methods execute successfully but also that invalid inputs are rejected, appointment conflicts are prevented, cancellation changes the correct status and cancelled appointments remain stored.

Therefore, high code coverage is useful, but it must be combined with strong test design to provide reliable evidence of correctness.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

The following matrix maps SmartCare functional requirements to the existing pytest tests. The mapping is based on the SmartCare A3 revision 2 starter README and the collected test names. The exact acceptance criterion IDs must be checked against the official requirements baseline when available.

| Requirement | Acceptance criterion / expected behaviour | Test ID | Test source | Status |
|---|---|---|---|---|
| FR-01 – Register patient | Valid patient registration succeeds | `test_registration_and_booking` | Supplied | Existing test collected |
| FR-01 – Register patient | Required fields are validated | `test_required_fields` | Supplied | Existing test collected |
| FR-01 – Register patient | Duplicate patient registration preserves the original record | `test_duplicate_patient_preserves_original` | Supplied | Existing test collected |
| FR-02 – Find patient | A registered patient can be found | `test_find_registered_patient` | Student-authored | Existing test collected |
| FR-02 – Find patient | Lookup returns the original stored object | `test_find_patient_returns_original_object` | Student-authored | Existing test collected |
| FR-02 – Find patient | Unknown patient IDs are rejected | `test_find_unknown_patient` | Student-authored | Existing test collected |
| FR-02 – Find patient | Blank patient IDs are rejected | `test_find_blank_patient_id` | Student-authored | Existing test collected |
| FR-02 – Find patient | Rejected lookup does not modify the existing patient | `test_rejected_lookup_preserves_patient` | Student-authored | Existing test collected |
| Practitioner registration | Duplicate practitioner registration preserves the original record | `test_duplicate_practitioner_preserves_original` | Supplied | Existing test collected |
| Practitioner lookup | A registered practitioner can be found | `test_find_registered_practitioner` | Student-authored | Existing test collected |
| Practitioner lookup | Lookup returns the original stored object | `test_find_practitioner_returns_original_object` | Student-authored | Existing test collected |
| Practitioner lookup | Unknown practitioner IDs are rejected | `test_find_unknown_practitioner` | Student-authored | Existing test collected |
| Practitioner lookup | Blank practitioner IDs are rejected | `test_find_blank_practitioner_id` | Student-authored | Existing test collected |
| Practitioner lookup | Rejected lookup preserves the existing record | `test_rejected_practitioner_lookup_preserves_record` | Student-authored | Existing test collected |
| Appointment booking | Valid appointment booking succeeds | `test_registration_and_booking` | Supplied | Existing test collected |
| Appointment booking | Duplicate appointment IDs preserve the original record | `test_duplicate_appointment_preserves_original` | Supplied | Existing test collected |
| Appointment booking | Unregistered participants are rejected | `test_unregistered_participants_rejected` | Supplied | Existing test collected |
| FR-05 – Practitioner conflict | Conflicting practitioner bookings are rejected | `test_conflict_rule_and_different_practitioner` | Supplied | Existing test collected |
| FR-06 – Cancel appointment | A scheduled appointment can be cancelled | `test_cancel_scheduled_appointment` | Student-authored | Existing test collected |
| FR-06 – Cancel appointment | Unknown appointment IDs are rejected | `test_cancel_unknown_appointment` | Student-authored | Existing test collected |
| FR-06 – Cancel appointment | Blank appointment IDs are rejected | `test_cancel_blank_appointment_id` | Student-authored | Existing test collected |
| FR-06 – Cancel appointment | Repeated cancellation is rejected | `test_cannot_cancel_twice` | Student-authored | Existing test collected |
| FR-06 – Domain cancellation | Cancellation and illegal transitions are guarded | `test_domain_cancellation_and_guard` | Supplied | Existing test collected |
| FR-07 – Retain cancelled history | Cancelled appointments remain retrievable | `test_cancelled_appointment_remains_in_history` | Student-authored | Existing test collected |

**Traceability notes:**

- The suite contains 23 distinct collected tests. Some tests support more than one requirement.
- Eight tests are supplied in `test_starter.py`, and fifteen student-authored tests are in `test_services.py`.
- The official acceptance criterion identifiers have not yet been verified against the separate SmartCare A3 2026 revision 2 requirements baseline.
- Test collection confirms that pytest discovered the tests; it does not establish that they passed or that every assertion is sufficient.
- The mapping should be reviewed against the test implementations and official acceptance criteria before final submission.

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

The test design focuses on observable SmartCare behaviour, including successful operations, invalid inputs, exceptions and preservation of existing records. Existing tests are mapped to the revision 2 starter contracts. The exact acceptance criterion IDs remain subject to verification against the official baseline.

| Test ID | Test intention | Expected observable evidence |
|---|---|---|
| `test_find_registered_patient` | Verify successful patient lookup | A registered patient is returned for a valid ID |
| `test_find_unknown_patient` | Verify rejection of an unknown patient ID | `LookupError` is raised |
| `test_find_blank_patient_id` | Verify invalid patient ID handling | `ValueError` is raised |
| `test_rejected_lookup_preserves_patient` | Verify that a failed lookup does not change stored data | The original patient remains stored and unchanged |
| `test_find_registered_practitioner` | Verify successful practitioner lookup | A registered practitioner is returned |
| `test_find_unknown_practitioner` | Verify rejection of an unknown practitioner ID | `LookupError` is raised |
| `test_find_blank_practitioner_id` | Verify invalid practitioner ID handling | `ValueError` is raised |
| `test_rejected_practitioner_lookup_preserves_record` | Verify that a failed lookup does not change stored data | The original practitioner remains stored and unchanged |
| `test_cancel_scheduled_appointment` | Verify successful cancellation | The appointment status becomes `CANCELLED` |
| `test_cancelled_appointment_remains_in_history` | Verify retained cancellation history | The cancelled appointment remains retrievable from the data store |
| `test_cancel_unknown_appointment` | Verify rejection of an unknown appointment ID | `LookupError` is raised |
| `test_cancel_blank_appointment_id` | Verify invalid appointment ID handling | `ValueError` is raised |
| `test_cannot_cancel_twice` | Verify protection against repeated cancellation | `ValueError` is raised when an already cancelled appointment is cancelled again |
| `test_conflict_rule_and_different_practitioner` | Verify practitioner booking conflict rules | A same-time booking conflict is rejected, while the permitted different-practitioner case succeeds |

### Test design rationale

The tests cover both positive and negative scenarios. Positive tests establish that supported operations work with valid data. Negative tests check that invalid inputs and prohibited operations raise the expected exceptions.

State-preservation tests provide additional evidence that rejected operations do not unintentionally alter existing records.

Cancellation tests verify two separate behaviours: the appointment status changes to `CANCELLED`, and the appointment remains stored for later retrieval. Both are necessary because changing a status does not, by itself, prove that history has been retained.

The existing tests provide a starting point for Stage 7 verification. Their assertions and execution results must be checked before claiming complete requirement coverage.
## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

The Arrange–Act–Assert (AAA) pattern was used to organise the SmartCare tests into three clear stages.

Arrange: Prepare the required test objects, register any necessary patients and practitioners, and create a fresh data store where appropriate.

Act: Call the service or domain method being tested, such as finding a patient, finding a practitioner or cancelling an appointment.

Assert: Verify the expected return value, exception, appointment status or retained data-store state.

Example 1 – Patient lookup

Arrange: Create a patient and register it in the SmartCare data store.

Act: Call find_patient() using the registered patient ID.

Assert: Confirm that the returned patient is the original registered object.

Related test: test_find_patient_returns_original_object

Example 2 – Unknown practitioner

Arrange: Create a practitioner service with a data store that does not contain the requested practitioner ID.

Act: Call find_practitioner() using the unknown ID.

Assert: Confirm that LookupError is raised.

Related test: test_find_unknown_practitioner

Example 3 – Appointment cancellation

Arrange: Register the required patient and practitioner, then create a scheduled appointment.

Act: Call cancel_appointment() using the appointment ID.

Assert: Confirm that the appointment status becomes CANCELLED.

Related test: test_cancel_scheduled_appointment

Example 4 – Retained cancellation history

Arrange: Create and store a scheduled appointment.

Act: Cancel the appointment and retrieve it from the data store.

Assert: Confirm that the stored appointment is the original object and its status is CANCELLED.

Related test: test_cancelled_appointment_remains_in_history

Why this structure is useful

The AAA pattern makes the purpose of each test easier to understand. It separates test setup from the operation being tested and the evidence used to verify the result.

It also helps identify weak tests. A test that only confirms an object exists may not verify the required behaviour. Stronger assertions check specific results, exceptions and state changes.

The examples above describe the intended test structure. The corresponding source code and pytest results provide the execution evidence.

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

The SmartCare domain tests examine the validation and state-management behaviour of the `Patient`, `Practitioner` and `Appointment` classes.

The following evidence is taken from the supplied `test_starter.py` test implementations.

| Domain area | Test | Test input or action | Assertion or expected result |
|---|---|---|---|
| Patient validation | `test_required_fields` | Construct `Patient(' ', 'Alex Example')` | `ValueError` is expected for a blank patient ID |
| Practitioner validation | `test_required_fields` | Construct `Practitioner('D1', 'Taylor Example', '')` | `ValueError` is expected for a blank specialty |
| Appointment creation | `test_registration_and_booking` | Book appointment `A1` with registered patient `P1` and practitioner `D1` | The appointment references the original registered patient and practitioner objects |
| Initial appointment status | `test_registration_and_booking` | Create a new appointment | `appointment.status is AppointmentStatus.SCHEDULED` |
| Domain cancellation | `test_domain_cancellation_and_guard` | Call `appointment.cancel()` on a scheduled appointment | `appointment.status is AppointmentStatus.CANCELLED` |
| Retained appointment record | `test_domain_cancellation_and_guard` | Retrieve the appointment list after cancellation | `data_store.list_appointments() == [appointment]` |
| Repeated cancellation | `test_domain_cancellation_and_guard` | Call `appointment.cancel()` a second time | `ValueError` is expected and status remains `CANCELLED` |

### Domain test observations

**Patient and practitioner validation**

The `test_required_fields` test verifies two invalid construction scenarios: a blank patient ID and an empty practitioner specialty. Both operations are expected to raise `ValueError`.

The supplied test does not independently demonstrate every possible invalid patient or practitioner field. Additional boundary tests may be required for complete validation evidence.

**Appointment construction and initial status**

The `test_registration_and_booking` test verifies that a booked appointment references the registered patient and practitioner objects. It also checks that the appointment initially has the `SCHEDULED` status and is present in the data store.

**Appointment cancellation**

The `test_domain_cancellation_and_guard` test calls the domain object's `cancel()` method and verifies that the status changes to `CANCELLED`.

The test also checks that the appointment remains in the data store after cancellation.

**Illegal or repeated transitions**

The same test attempts to cancel the appointment again. It expects `ValueError` and verifies that the status remains `CANCELLED`.

This demonstrates protection against repeated cancellation. Other possible illegal transitions have not been independently demonstrated by the supplied tests.

### Evidence limitations

The reviewed tests provide evidence of the intended domain behaviours, but reviewing their source code alone does not prove that they passed during the current Stage 7 verification run.

Further domain boundary testing may be needed, including whitespace-only names and other invalid construction inputs, depending on the confirmed revision 2 requirements.

The actual pytest execution result and tested Git commit will be recorded in Section J.

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

The SmartCare service tests verify the Stage 6 functionality implemented in `PatientService`, `PractitionerService` and `AppointmentService`.

The evidence is based on the fifteen student-authored tests in `project/tests/test_services.py`.

### F.1 PatientService

| Test | Action | Expected evidence |
|---|---|---|
| `test_find_registered_patient` | Register patient `P001` and retrieve the patient | The returned object is the original patient, with ID `P001` and name `Alex Smith` |
| `test_find_patient_returns_original_object` | Retrieve a registered patient | The returned object is identical to the stored object |
| `test_find_unknown_patient` | Search for `P999` | `LookupError` is raised |
| `test_find_blank_patient_id` | Search using whitespace-only ID | `ValueError` is raised |
| `test_rejected_lookup_preserves_patient` | Attempt an unknown lookup after registering a patient | The original patient remains retrievable |

### F.2 PractitionerService

| Test | Action | Expected evidence |
|---|---|---|
| `test_find_registered_practitioner` | Register and retrieve practitioner `D001` | The original practitioner is returned with the correct ID and name |
| `test_find_practitioner_returns_original_object` | Retrieve a registered practitioner | The returned object is identical to the registered object |
| `test_find_unknown_practitioner` | Search for `D999` | `LookupError` is raised |
| `test_find_blank_practitioner_id` | Search using whitespace-only ID | `ValueError` is raised |
| `test_rejected_practitioner_lookup_preserves_record` | Attempt an unknown lookup | The original practitioner remains retrievable |

### F.3 AppointmentService

| Test | Action | Expected evidence |
|---|---|---|
| `test_cancel_scheduled_appointment` | Cancel appointment `A001` | The original appointment is returned with status `CANCELLED` |
| `test_cancelled_appointment_remains_in_history` | Cancel and retrieve appointment `A001` | The same appointment remains stored with status `CANCELLED` |
| `test_cancel_unknown_appointment` | Cancel unknown appointment `A999` | `LookupError` is raised |
| `test_cancel_blank_appointment_id` | Cancel using a whitespace-only ID | `ValueError` is raised |
| `test_cannot_cancel_twice` | Cancel appointment `A001` twice | The second cancellation raises `ValueError`, and the status remains `CANCELLED` |

### F.4 Test isolation and shared data store

Each service test creates a new `SmartCareDataStore` instance. This reduces interference between tests and avoids relying on records created by earlier tests.

The appointment tests use a shared setup function, `cancellation_setup()`, which creates:

- A new `SmartCareDataStore`.
- A registered patient with ID `P001`.
- A registered practitioner with ID `D001`.
- An `AppointmentService` using the same data store.
- A scheduled appointment with ID `A001`.

The appointment time is set seven days ahead, with seconds and microseconds removed to maintain minute precision.

The patient, practitioner and appointment services in this setup share the same data store instance, allowing the appointment service to use the registered participants.

### F.5 Assertions and limitations

The tests use object identity checks (`is`), exact exception checks (`pytest.raises`) and appointment status assertions.

These assertions provide more specific evidence than checking only that an object exists.

The cancellation history test verifies that a cancelled appointment remains retrievable from the data store. However, the current service tests do not independently verify every possible invalid field, appointment transition or booking boundary.

The source code demonstrates the intended test coverage. Execution results will be recorded separately in Section J.

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.


Negative and boundary testing checks that SmartCare rejects invalid operations without causing unintended changes to stored records.

The following cases are based on the supplied tests in `test_starter.py` and the student-authored tests in `test_services.py`.

| Test or scenario | Invalid input or operation | Expected result | State-preservation evidence |
|---|---|---|---|
| `test_required_fields` | Whitespace-only patient ID | `ValueError` | Object construction is rejected |
| `test_required_fields` | Empty practitioner specialty | `ValueError` | Object construction is rejected |
| `test_find_blank_patient_id` | Whitespace-only patient lookup ID | `ValueError` | No mutation assertion in this test |
| `test_find_unknown_patient` | Unknown patient ID `P999` | `LookupError` | No mutation assertion in this test |
| `test_rejected_lookup_preserves_patient` | Unknown patient lookup after registration | `LookupError` | Original patient remains retrievable as the same object |
| `test_find_blank_practitioner_id` | Whitespace-only practitioner lookup ID | `ValueError` | No mutation assertion in this test |
| `test_find_unknown_practitioner` | Unknown practitioner ID `D999` | `LookupError` | No mutation assertion in this test |
| `test_rejected_practitioner_lookup_preserves_record` | Unknown practitioner lookup after registration | `LookupError` | Original practitioner remains retrievable as the same object |
| `test_duplicate_patient_preserves_original` | Duplicate patient ID | `ValueError` | Original patient identity and name are preserved |
| `test_duplicate_practitioner_preserves_original` | Duplicate practitioner ID | `ValueError` | Original practitioner identity and name are preserved |
| `test_duplicate_appointment_preserves_original` | Duplicate appointment ID | `ValueError` | Appointment list and original booking time are preserved |
| `test_unregistered_participants_rejected` | Unknown patient or unregistered patient object | `LookupError` or `ValueError`, depending on the operation | Appointment list remains empty |
| `test_conflict_rule_and_different_practitioner` | Same practitioner booked at the same time | `ValueError` | No explicit assertion that the original booking remains unchanged |
| `test_cancel_unknown_appointment` | Unknown appointment ID `A999` | `LookupError` | No explicit state-preservation assertion |
| `test_cancel_blank_appointment_id` | Whitespace-only appointment ID | `ValueError` | No explicit state-preservation assertion |
| `test_cannot_cancel_twice` | Cancel an already cancelled appointment | `ValueError` | Appointment status remains `CANCELLED` |
| `test_domain_cancellation_and_guard` | Repeat domain cancellation | `ValueError` | Appointment remains stored and status remains `CANCELLED` |

### Boundary testing observations

The tests cover blank identifiers, unknown records, duplicate IDs, practitioner scheduling conflicts and repeated cancellation.

Several tests explicitly verify that an unsuccessful operation does not replace or alter an existing record.

However, not every negative test includes a state-preservation assertion. For example, the unknown and blank appointment cancellation tests verify the exception but do not separately assert that the original appointment remains unchanged.

### Additional testing opportunities

Further tests could strengthen the evidence by checking:

- Whitespace-only patient and practitioner names.
- Preservation of an existing appointment after an unsuccessful cancellation.
- Preservation of the original booking after a scheduling conflict.
- Other invalid appointment status transitions, where supported by the domain model.

These are identified testing gaps or proposed improvements, not completed test results.

### Conclusion

The existing tests demonstrate that SmartCare rejects several invalid inputs and prohibited operations. State-preservation assertions provide stronger evidence where they are present.

Additional tests would improve confidence that rejected operations leave the complete data-store state unchanged.
## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

**Requirement:** FR-06 – Cancel Appointment

**Acceptance criterion:** Illegal appointment status transitions must be rejected without changing the appointment. Exact canonical AC ID not yet verified.

**Behaviour to test:** Cancelling an appointment that is already in `COMPLETED` status.

**Human-first test idea/categories:** Before consulting Copilot, the test design covered successful cancellation, repeated cancellation, invalid appointment IDs and preservation of cancelled appointment history.

**Prompt and purpose:**

Prompt submitted to GitHub Copilot:

"Review my SmartCare pytest tests for FR-06 appointment cancellation. Suggest one additional negative or boundary test for AppointmentService.cancel_appointment() using only the existing project requirements. Explain what the test should assert and why. Do not invent new features or modify any files."

Purpose: Identify a missing negative or boundary test without introducing unsupported functionality.

### Copilot candidate 1

**Copilot test idea/candidate:** Attempt to cancel an appointment that is already in `COMPLETED` status.

**What it claims to verify:** Illegal appointment status transitions are rejected without changing the appointment.

**Requirement trace:** FR-06 – Appointment Cancellation. Exact acceptance criterion ID remains unverified.

**Assertion quality:** The suggested assertions are specific: `ValueError` should be raised, the appointment should remain `COMPLETED`, and the same appointment should remain retrievable from the data store.

**Human critique:** The Copilot suggestion is relevant because the existing tests cover repeated cancellation but do not explicitly cover cancellation from `COMPLETED` status. The `Appointment` constructor accepts an `AppointmentStatus` value, and the `cancel()` method rejects every status other than `SCHEDULED`. The availability of `COMPLETED` in the enum still needs confirmation.

Decision: Accept with a verified test implementation.

Reason: GitHub Copilot identified an additional negative test for cancelling a completed appointment. I checked the existing AppointmentStatus enum and Appointment class to confirm that COMPLETED is supported and that cancellation is restricted to scheduled appointments. I then implemented the test using the existing domain constructor and data-store methods.

Final test reference: project/tests/test_services.py::test_cannot_cancel_completed_appointment

Actual verification result: PASSED. The targeted pytest run collected one test and reported 1 passed in 0.14s.

Assertions verified:

Cancelling a completed appointment raises ValueError.

The appointment status remains COMPLETED.

The original appointment remains retrievable from the data store.

Human review conclusion: The Copilot suggestion was accepted after checking that it matched the existing SmartCare requirements and implementation. No unsupported functionality was introduced.

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

**Selected Copilot suggestion:** Test cancellation of an appointment that is already in `COMPLETED` status.

**Potential weakness:** A test that only checks whether `cancel_appointment()` raises `ValueError` would be incomplete. It would not prove that the rejected cancellation leaves the existing appointment unchanged.

**Human improvement:** I strengthened the test by adding assertions that the appointment remains in `COMPLETED` status and that the data store still contains the original appointment object.

**Why the improved assertions matter:** The requirement is not simply to reject an illegal operation. It is also important that rejection does not corrupt or remove existing appointment information.

**Verification:** The targeted test `test_cannot_cancel_completed_appointment` passed. The complete regression suite subsequently reported 24 passing tests.

**Reflection:** GitHub Copilot helped identify a missing boundary case, but I checked the suggestion against the existing domain model before implementing it. This demonstrated why AI-generated test ideas require human review and verification.

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
[response]

2. What question does validation answer?
[response]

3. What is a unit test?
[response]

4. What is a pytest fixture?
[response]

5. What is parametrisation in pytest?
[response]

6. What is regression testing?
[response]

7. What does code coverage tell us, and what does it not prove?
[response]

8. What makes an assertion weak?
[response]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[response]

10. What is the Stage 7 engineering rule?
[response]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
