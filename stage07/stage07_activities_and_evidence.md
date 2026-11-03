# Stage 7 Testing and Verification Record

Group/tutorial: Thu 2:30 - 4:30 Group 5  Members/cohorts: Oliver11233211, Unavailable-11, kathryn-n1, Josh-Uni1 (GitHub usernames) - All members are undergraduate 4483
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register P1 "Alex Example" in store. | Register P1 with name consisting of spaces only. | Positive: Same Patient object returned. Negative: ValueError raised, store still empty. |
| FR-05 Prevent practitioner conflict | Book D1 at time 9:00 then attempt to book D1 at time 9:01. | Book D1 at time 9:00 for P1 then book D1 again at 9:00 for registered patient P2. | Positive: Second appointment status is SCHEDULED and both are stored. Negative: ValueError raised. Only original appointment is stored. |
| FR-06 Cancel appointment | Cancel SCHEDULED appointment A1. | Attempt to cancel A1 again. | Positive: Appointment has status CANCELLED. Negative: ValueError raised. Appointment remains in CANCELLED state. |
| FR-07 Retain cancelled history | Cancel A1 and retrieve A1. | Cancel A1 and try cancelling again. | Positive: Shows that find_appointment('A1') returns the same object and has a status of CANCELLED. A1 also appears in list_appointments(). Negative: Shows that a ValueError is thrown but A1 remains in list_appointments() with a status of CANCELLED. Cancelling fails so no removal or alteration occurs. |


### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: Weak/Unclear  
Why: This statement will always pass, so it does not tell us anything about how SmartCare behaves. 


`assert appointment is not None`
Judgement: Weak/Unclear  
Why: Whilst this shows that a value was returned, it doesn’t show that the correct appointment has been returned. 

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong  
Why: This shows that the appointment is exactly in the state it needs to be when cancelled (FR-06). However, it doesn’t show that the appointment was kept (FR-07). As we are comparing enums, using `is` is preferable. 

`assert len(results) > 0`
Judgement: Weak/Unclear  
Why: Any results which are not empty will pass. It doesn’t ensure that the correct records were returned. We should have asserted against what results we actually expect. 


`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong  
Why: This shows that the appointment returned is the exact object that was stored. It doesn’t show that the appointment has the correct status though.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 
| Case | Input/state | Expected result | Supporting contract |
|---|---|---|---|
| Empty ID | '' | Raises a ValueError. | ID must not be blank. IDs are trimmed, non-blank and case-sensitive. |
| Empty ID | ' ' | Raises a ValueError because it is blank once trimmed. | IDs are trimmed, non-blank and case-sensitive. |
| Empty ID | ' P1 ' | Will be accepted and stored as 'P1'. However, attempting to register 'P1' again will result in a ValueError due to duplication. | IDs are trimmed. Duplicate IDs raise a ValueError. |
| Empty ID | A lowercase 'p1' ID when there is only a 'P1' ID | Will raise a LookupError, as IDs are case-sensitive. | ID must be case-sensitive. |
| Empty ID | An unknown ID | Will raise a LookupError. | No entry will be added. ID must be a known ID. |
| Whitespace names | Patient name ' ' | Raises a ValueError. | Name must be non-blank text (required_text). |
| Whitespace names | Practitioner name or specialty of '' | Raises a ValueError. No data will be stored. | Name and specialty must be non-blank text (required_text). |
| Practitioner with same time | Same Practitioner at same time | Will raise a ValueError. The existing booking will remain. | If there is a conflict, raise a ValueError. |
| Practitioner with same time | Same Practitioner at +1 minute | Will be allowed, as only if there is an exact-time SCHEDULED conflict will there be a problem. | "No … duration … rules apply". |
| Practitioner with same time | Different Practitioner at same time | Will be allowed. | This is illustrated by test_conflict_rule_and_different_practitioner. |
| Practitioner with same time | Two Practitioners for the same Patient at same time | Will be allowed. | "No … patient-conflict … rules apply". |
| Practitioner with same time | Time with seconds (e.g. 09:00:30) | Raises a ValueError. | Time must be minute precision. |
| Practitioner with same time | Appointment slot with a cancelled appointment | Can be rebooked, as there is no conflict with cancelled appointments. Cancelled appointment will still be stored. | Only SCHEDULED appointments count as a conflict. |
| Cancel appointments | Cancelling an already cancelled appointment | Will raise a ValueError. It will stay as cancelled. | Raise ValueError for illegal transition. Failed state remains. |
| Cancel appointments | Cancel appointment | Will return the same object but with a cancelled status. It will still be included in list_appointments(). | Cancel a SCHEDULED appointment without deleting it. |
| Invalid status changes | Trying to cancel a COMPLETED appointment | Will raise a ValueError. It will stay as completed. | Only SCHEDULED appointments can be cancelled. |
| Invalid status changes | Creating an appointment with an invalid status (e.g. 'cancelled' string) | Will raise a ValueError. | Invalid appointment status. |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.


| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | This test only checks that a patient object was returned, so it would pass even if it was the wrong patient or was never stored. | By registering a new patient (P1 - Alex Example) we can assert that find_patient('P1') will return the same patient object and that the patient's name is "Alex Example". (FR-01, AC-01.1). |
| 2 | This test only checks that an appointment object was returned and will pass regardless of whether the status has been updated, or if the appointment was even deleted. | By cancelling appointment A1 we can assert that its status is now AppointmentStatus.CANCELLED, find_appointment('A1') returns the same object and A1 is still in list_appointments(). (FR-06, FR-07, AC-05.1, AC-05.2). |
| 3 | This assert will never fail as it is always true. Since it doesn’t check any functionality it cannot be linked to any requirements. | By booking D1 at 09:00 we can then attempt to book D1 at the same time for P2. We can assert that a ValueError is raised and that list_appointments() only contains the original appointment. (FR-05, AC-04.1). |
| 4 | Assumes that an SMS will be sent when booking. This is not mentioned in the requirements so a new business rule has been created. This test can only pass if something is checked that SmartCare does not have to do. | By not checking the SMS, we can book A1 using the registered P1 and D1. We can assert that the appointment stored is the same object, that it is linked to the same participants and that it is SCHEDULED. (FR-04, AC-03.1). |
| 5 | Assumes that an SMS will be sent when cancelling. This is the same made-up rule so there is no evidence that the appointment was cancelled. | By not checking the SMS, we can cancel A1 and then attempt to cancel it again. We can assert that a ValueError is raised and that A1 is still stored with status CANCELLED. (FR-06, FR-07, AC-05.3). |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?

A: Coverage is just measuring how much of your code was executed but does not tell you if the assertions are actually testing what they should be. You could have 100% coverage on your test suite if your tests all use ‘assert True’ but you would not have found any bugs. Your test suite may have 100% coverage but may not have found any incorrect outputs, invalid inputs or untested requirements.


## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.



| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| FR-01 | Not AC-01.2 but "IDs are strings, trimmed, non-blank and case-sensitive." | SUP-01 | Negative | tests/test_starter.py::test_required_fields | If the patient ID and specialty fields are empty then a ValueError is raised | Passed | Supplied |
| FR-04 | AC-03.1 | SUP-02 | Positive | tests/test_starter.py::test_registration_and_booking | The scheduled status is stored for the booked appointment with the registered participants | Passed | Supplied |
| FR-01 | AC-01.2 | SUP-03 | Negative | tests/test_starter.py::test_duplicate_patient_preserves_original | A ValueError is raised if a duplicate patient ID is used | Passed | Supplied |
| FR-03 | "Invalid inputs, duplicate IDs, conflicts and illegal transitions raise ValueError." | SUP-04 | Negative | tests/test_starter.py::test_duplicate_practitioner_preserves_original | A ValueError is raised if a duplicate practitioner ID is used | Passed | Supplied |
| FR-04 | "Invalid inputs, duplicate IDs, conflicts and illegal transitions raise ValueError." | SUP-05 | Negative | tests/test_starter.py::test_duplicate_appointment_preserves_original | A ValueError is raised if a duplicate appointment ID is used | Passed | Supplied |
| FR-04 | AC-03.2 | SUP-06 | Negative | tests/test_starter.py::test_unregistered_participants_rejected | A LookupError is raised if the patient is not known. A ValueError is raised if there is a similar patient. Nothing is stored. | Passed | Supplied |
| FR-05 | AC-04.1 & AC-04.2 | SUP-07 | Negative & Positive | tests/test_starter.py::test_conflict_rule_and_different_practitioner | If the same practitioner is used at the same time then a ValueError is raised. However, if a different practitioner is used it is allowed. | Passed | Supplied |
| FR-06 & FR-07 | AC-05.1 & AC-05.3 (Domain Evidence) | SUP-08 | Positive & Negative | tests/test_starter.py::test_domain_cancellation_and_guard | The status is changed to cancelled. If cancelled again a ValueError is raised. The appointment remains stored. | Passed | Supplied |
| FR-01 | AC-01.1 (Partial Domain Evidence) | TEST-01 | Positive | tests/test_domain.py::test_patient_stores_valid_fields | If a valid patient is created it will have its trimmed ID and name exposed | Passed | Student |
| FR-01 | "IDs are strings, trimmed, non-blank and case-sensitive." | TEST-02 | Negative & Boundary | tests/test_domain.py::test_blank_patient_id_is_rejected | If the ID is ‘’ or consists of all whitespace then a ValueError is raised | Passed | Student |
| FR-01 | "Required names and specialty are non-blank." | TEST-03 | Boundary | tests/test_domain.py::test_whitespace_patient_name_is_rejected | If the name consists of all whitespace then a ValueError is raised | Passed | Student |
| FR-03 | "Required names and specialty are non-blank." | TEST-04 | Positive | tests/test_domain.py::test_practitioner_stores_valid_fields | If a valid practitioner is created it will have its ID, name and specialty exposed | Passed | Student |
| FR-03 | "Required names and specialty are non-blank." | TEST-05 | Negative & Boundary | tests/test_domain.py::test_blank_practitioner_fields_are_rejected | If the ID, name or specialty are empty then a ValueError is raised | Passed | Student |
| FR-04 | AC-03.1 (Partial Domain Evidence) | TEST-06 | Positive | tests/test_domain.py::test_new_appointment_starts_scheduled | A new appointment will be in the SCHEDULED status with the provided participants and time | Passed | Student |
| FR-04 | "Invalid inputs, duplicate IDs, conflicts and illegal transitions raise ValueError." "Timezone-aware values and nonzero seconds/microseconds are invalid." | TEST-07 | Negative & Boundary | tests/test_domain.py::test_appointment_rejects_invalid_inputs | If invalid participants, status or date/time values are provided then a ValueError is raised | Passed | Student |
| FR-06 | AC-05.1 (Partial Domain Evidence) | TEST-08 | Positive | tests/test_domain.py::test_cancel_changes_status | The status is changed from SCHEDULED to CANCELLED | Passed | Student |
| FR-06 | AC-05.3 (Partial Domain Evidence) | TEST-09 | Negative | tests/test_domain.py::test_repeated_cancel_is_rejected | If cancelled again then a ValueError is raised. The appointment remains in the CANCELLED status. | Passed | Student |
| FR-06 | "Only SCHEDULED can be cancelled" (BR-06/07) | TEST-10 | Negative | tests/test_domain.py::test_completed_appointment_cannot_be_cancelled | If cancelled when in the COMPLETED status then a ValueError is raised. The appointment remains in the COMPLETED status. | Passed | Student |
| FR-01 & FR-02 | AC-01.1 & AC-02.1 | TEST-11 | Positive | tests/test_services.py::test_find_patient_returns_registered_patient | find_patient returns the same registered object with the provided name | Passed | Student |
| FR-01 | AC-01.2 | TEST-12 | Boundary | tests/test_services.py::test_trimmed_duplicate_patient_id_is_rejected | If the ID is ‘ P1 ’ then it is stored as ‘P1’. If ‘P1’ is registered then a ValueError is raised. The original patient is retained. | Passed | Student |
| FR-02 | AC-02.2 & "IDs are strings, trimmed, non-blank and case-sensitive." | TEST-13 | Negative & Boundary | tests/test_services.py::test_find_patient_rejects_invalid_id | If the ID is unknown or the case does not match then a LookupError is raised. If the ID is empty then a ValueError is raised. No patient is created. | Passed | Student |
| FR-03 | "Practitioner lookup is a supporting operation." | TEST-14 | Positive | tests/test_services.py::test_find_practitioner_returns_registered_practitioner | find_practitioner returns the same registered object. | Passed | Student |
| FR-03 | "A valid unknown service lookup raises LookupError" | TEST-15 | Negative & Boundary | tests/test_services.py::test_find_practitioner_rejects_invalid_id | If the ID is unknown then a LookupError is raised. If the ID is empty then a ValueError is raised. No practitioner is created. | Passed | Student |
| FR-04 & FR-08 | AC-03.1 & AC-06.1 | TEST-16 | Positive | tests/test_services.py::test_book_stores_and_finds_scheduled_appointment | find_appointment returns the same object. The appointment is associated with the registered participants and is in the SCHEDULED status. | Passed | Student |
| FR-04 | AC-03.2 | TEST-17 | Negative | tests/test_services.py::test_book_unknown_practitioner_is_rejected | If the practitioner is unknown then a LookupError is raised. Nothing is stored. | Passed | Student |
| FR-05 | AC-04.1 | TEST-18 | Negative | tests/test_services.py::test_same_practitioner_same_time_conflicts | If the same practitioner is used at the same time but with a different patient then a ValueError is raised. Only the original is stored. | Passed | Student |
| FR-05 | "No patient-conflict, duration-overlap, past-date, clinic-hours or clinical rules are invented." | TEST-19 | Boundary | tests/test_services.py::test_same_practitioner_one_minute_later_is_allowed | If the appointment is booked one minute later then it is allowed. | Passed | Student |
| FR-05 | "Same practitioner + exact time + SCHEDULED conflicts" (BR-05) | TEST-20 | Boundary | tests/test_services.py::test_cancelled_booking_frees_slot | The slot can be booked again. The cancelled appointment remains stored in the CANCELLED status. | Passed | Student |
| FR-06 & FR-08 | "A valid unknown service lookup raises LookupError" | TEST-21 | Negative | tests/test_services.py::test_unknown_appointment_id_raises_lookup_error | If the appointment is looked up or cancelled and the ID is unknown then a LookupError is raised. The appointments remain stored. | Passed | Student |
| FR-06 & FR-07 | AC-05.1 & AC-05.2 | TEST-22 | Positive | tests/test_services.py::test_cancel_retains_same_appointment | cancel returns the same object in the CANCELLED status. The appointment can still be looked up and appears in list_appointments(). | Passed | Student |
| FR-06 | AC-05.3 | TEST-23 | Negative | tests/test_services.py::test_repeated_service_cancel_is_rejected | If cancelled again then a ValueError is raised. The appointment remains stored in the CANCELLED status. | Passed | Student |
| FR-06 & FR-07 | AC-05.2 | TEST-24 | Boundary | tests/test_services.py::test_cancelled_appointment_is_retrievable_among_others | Cancelled appointment can still be found and listed as cancelled. Another appointment remains scheduled. | Passed | Student (Modified from Copilot candidate 5) |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| TEST-01 | FR-01 | AC-01.1 (Partial Domain Evidence) | Positive | A valid patient has their fields preserved | ID and name will be trimmed | Not checked in current tests |
| TEST-02 | FR-01 | "IDs are strings, trimmed, non-blank and case-sensitive." | Negative/Boundary | Blank patient ID's are rejected | ValueErrors occur for '' and whitespace. | Covers empty ID case |
| TEST-03 | FR-01 | "Required names and specialty are non-blank." | Boundary | Whitespace only name is rejected | ValueError | Not checked in current tests |
| TEST-04 | FR-03 | "Required names and specialty are non-blank." | Positive | A valid practitioner will have their fields preserved | ID, name, and specialty are correct | All fields are directly tested |
| TEST-05 | FR-03 | "Required names and specialty are non-blank." | Negative/Boundary | Any blank fields are rejected | ValueErrors occur for each field | Only specialty field is tested in current tests |
| TEST-06 | FR-04 | AC-03.1 (Partial Domain Evidence) | Positive | A new appointment will be initialised correctly | Appointment will be SCHEDULED with specified participants and time | Testing initialisation with no services |
| TEST-07 | FR-04 | "Invalid inputs, duplicate IDs, conflicts and illegal transitions raise ValueError." "Timezone-aware values and nonzero seconds/microseconds are invalid." | Negative/Boundary | Invalid appointment values are rejected | ValueError occurs for each value. | Values not covered in current tests |
| TEST-08 | FR-06 | AC-05.1 (Partial Domain Evidence) | Positive | Booking cancelled will update status | Appointment will be CANCELLED | Reference intention is kept as its own test |
| TEST-09 | FR-06 | AC-05.3 (Partial Domain Evidence) | Negative | Double cancellation will be rejected | ValueError occurs. Status remains as CANCELLED. | Reference intention is kept as its own test |
| TEST-10 | FR-06 | "Only SCHEDULED can be cancelled" (BR-06/07) | Negative | Appointment with status COMPLETED cannot be cancelled | ValueError occurs. Status remains as COMPLETED. | COMPLETED not checked in current tests |
| TEST-11 | FR-01 and FR-02 | AC-01.1 and AC-02.1 | Positive | Patient will be found | Same object and name | Complete lookup function from stage 6 |
| TEST-12 | FR-01 | AC-01.2 | Boundary | Duplicate ID will be rejected after trimming | ValueError occurs. Original is retained. | Only identical ID used in current tests |
| TEST-13 | FR-02 | AC-02.2 and "IDs are strings, trimmed, non-blank and case-sensitive." | Negative/Boundary | Invalid patient lookup | LookupError or ValueError. No patient added. | Complete lookup function from stage 6 |
| TEST-14 | FR-03 | "Practitioner lookup is a supporting operation." | Positive | Practitioner will be found | Same object | Complete lookup function from stage 6 |
| TEST-15 | FR-03 | "A valid unknown service lookup raises LookupError" | Negative/Boundary | Invalid practitioner lookup | LookupError or ValueError. No practitioner added. | Complete lookup function from stage 6 |
| TEST-16 | FR-04 and FR-08 | AC-03.1 and AC-06.1 | Positive | Booking can be found | Same object, participants and SCHEDULED | Focuses on booking and finding |
| TEST-17 | FR-04 | AC-03.2 | Negative | Can't book unknown practitioner | LookupError. Nothing is stored. | Only unknown patient used in current tests |
| TEST-18 | FR-05 | AC-04.1 | Negative | Conflict with same time | ValueError. Only original stored. | Different patient added. State checked |
| TEST-19 | FR-05 | "No patient-conflict, duration-overlap, past-date, clinic-hours or clinical rules are invented." | Boundary | Later by 1 minute is accepted | Both stored. Second is SCHEDULED. | Tests edge of exact time rule |
| TEST-20 | FR-05 | "Same practitioner + exact time + SCHEDULED conflicts" (BR-05) | Boundary | Cancelled booking will free up time | Booking can be made. Old booking remains as CANCELLED. | Tests SCHEDULED section of rule |
| TEST-21 | FR-06 and FR-08 | "A valid unknown service lookup raises LookupError" | Negative | Unknown appointment IDs are rejected | LookupError. Appointment remains unchanged. | Complete cancellation function from stage 6 |
| TEST-22 | FR-06 and FR-07 | AC-05.1 and AC-05.2 | Positive | Cancellation will preserve record | Same object. Status is CANCELLED. Still found and listed. | Cancellation using service |
| TEST-23 | FR-06 | AC-05.3 | Negative | Double cancellation using service will be rejected | ValueError. Record remains as CANCELLED. | Cancellation using service |
| TEST-24 | FR-06 & FR-07 | AC-05.2 | Boundary | Cancellation of one appointment out of many keeps it and leaves the other the same | Same object found with status cancelled. Other appointment remains scheduled. Both are listed. | Current tests don’t check other appointment remains the same. |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| TEST-01 | Values with spaces around | Create Patient | ID and name are trimmed | Fails if values are not stored and trimmed |
| TEST-02 | '' and whitespace ID's | Create Patient | pytest.raises(ValueError) | Fails if blank ID's are accepted |
| TEST-03 | Whitespace only name | Create Patient | pytest.raises(ValueError) | Fails if blank name is accepted |
| TEST-04 | Valid practitioner values | Create Practitioner | ID, name and specialty are correct | Fails if any values are lost or swapped |
| TEST-05 | One blank field | Create Practitioner | pytest.raises(ValueError) | Fails if any required fields are not validated |
| TEST-06 | Patient, practitioner and time | Create Appointment | Appointment will be SCHEDULED. Correct participants and time. | Fails if incorrect status is set or linked to |
| TEST-07 | One invalid value | Create Appointment | pytest.raises(ValueError) | Fails if any invalid values are accepted |
| TEST-08 | New appointment | cancel() | Status is CANCELLED | Fails if status is not updated |
| TEST-09 | Cancelled appointment | cancel() | ValueError. Status remains as CANCELLED. | Fails if double cancellation is accepted |
| TEST-10 | COMPLETED appointment | cancel() | ValueError. Status remains as COMPLETED. | Fails if status has no guard |
| TEST-11 | Registered patient | find_patient('P1') | Same object. Correct name. | Using `is` to show that the actual object is returned |
| TEST-12 | Patient registered as ' P1 ' | Register 'P1' | ValueError. Original remains as only patient. | Fails if trimming or duplicate check fails |
| TEST-13 | P1 registered | find_patient with each invalid ID | Expected error. Patient list unchanged. | Fails if incorrect error or record created |
| TEST-14 | Practitioner registered | find_practitioner('D1') | Same object. | Using `is` to show actual object is returned |
| TEST-15 | D1 registered | find_practitioner with each invalid ID | Expected error. Practitioner list unchanged. | Fails if incorrect error or record created |
| TEST-16 | P1 and D1 registered | book_appointment | Same object returned. Correct links. SCHEDULED. | Shows it is being stored through workflow |
| TEST-17 | P1 registered | Book with unknown practitioner | LookupError. No appointments. | Fails if partial record is stored |
| TEST-18 | P1, P2, D1 and A1 booked | Book A2 with D1 at same time | ValueError. Only A1 stored. | Shows it is rejected and remains unchanged |
| TEST-19 | P1, P2, D1 and appointment at 09:00 | Book D1 at 09:01 | SCHEDULED. Both stored. | Fails if overlap rule is made up |
| TEST-20 | P1, P2, D1 and A1 cancelled | Book A2 at same time | A2 is SCHEDULED. A1 is CANCELLED. Both stored. | Fails if cancelled appointments still conflict or are deleted |
| TEST-21 | A1 booked | Find and cancel unknown 'A9' | LookupError. A1 remains unchanged. | Fails if incorrect error or record changed |
| TEST-22 | A1 booked | cancel_appointment('A1') | Same object. CANCELLED. Found. Listed. | Fails if record replaced/deleted (AC-05.2) |
| TEST-23 | A1 cancelled | Cancel A1 | ValueError. CANCELLED. Still stored. | Fails if double cancellation accepted or record changed |
| TEST-24 | A1 and A2 booked | cancel_appointment('A1') | Same object. A1 cancelled. A2 scheduled. Both are listed. | Fails if record removed or another appointment is changed (AC-05.2) |


## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| TEST-01 | Patient fields valid | tests/test_domain.py::test_patient_stores_valid_fields | Passed |
| TEST-02 | Blank patient id rejected (intention) | tests/test_domain.py::test_blank_patient_id_is_rejected | Passed (2 cases) |
| TEST-03 | Patient name with whitespace only rejected | tests/test_domain.py::test_whitespace_patient_name_is_rejected | Passed |
| TEST-04 | Practitioner fields valid | tests/test_domain.py::test_practitioner_stores_valid_fields | Passed |
| TEST-05 | Blank practitioner fields rejected | tests/test_domain.py::test_blank_practitioner_fields_are_rejected | Passed (3 cases) |
| TEST-06 | New appointment starts scheduled (intention) | tests/test_domain.py::test_new_appointment_starts_scheduled | Passed |
| TEST-07 | Appointment rejects invalid inputs | tests/test_domain.py::test_appointment_rejects_invalid_inputs | Passed (7 cases) |
| TEST-08 | Cancellation changes status (intention) | tests/test_domain.py::test_cancel_changes_status | Passed |
| TEST-09 | Multiple cancellation rejected (intention) | tests/test_domain.py::test_repeated_cancel_is_rejected | Passed |
| TEST-10 | Completed can’t be cancelled | tests/test_domain.py::test_completed_appointment_cannot_be_cancelled | Passed |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| TEST-11 | Find registered patient | FR-01, FR-02 / AC-01.1, AC-02.1 | tests/test_services.py::test_find_patient_returns_registered_patient | Passed |
| TEST-12 | Trimming patient id rejected | FR-01 / AC-01.2 | tests/test_services.py::test_trimmed_duplicate_patient_id_is_rejected | Passed |
| TEST-13 | Invalid patient lookup rejected | FR-02 / AC-02.2 | tests/test_services.py::test_find_patient_rejects_invalid_id | Passed (4 cases) |
| TEST-14 | Find registered practitioner | FR-03 / "Practitioner lookup is a supporting operation." | tests/test_services.py::test_find_practitioner_returns_registered_practitioner | Passed |
| TEST-15 | Invalid practitioner lookup rejected | FR-03 / "A valid unknown service lookup raises LookupError" | tests/test_services.py::test_find_practitioner_rejects_invalid_id | Passed (3 cases) |
| TEST-16 | Booking stored and found | FR-04, FR-08 / AC-03.1, AC-06.1 | tests/test_services.py::test_book_stores_and_finds_scheduled_appointment | Passed |
| TEST-17 | Unknown practitioner rejected | FR-04 / AC-03.2 | tests/test_services.py::test_book_unknown_practitioner_is_rejected | Passed |
| TEST-18 | Same time conflict | FR-05 / AC-04.1 | tests/test_services.py::test_same_practitioner_same_time_conflicts | Passed |
| TEST-19 | One minute later is allowed | FR-05 / "No patient-conflict, duration-overlap, past-date, clinic-hours or clinical rules are invented." | tests/test_services.py::test_same_practitioner_one_minute_later_is_allowed | Passed |
| TEST-20 | Cancelled booking frees slot | FR-05 / "Same practitioner + exact time + SCHEDULED conflicts" (BR-05) | tests/test_services.py::test_cancelled_booking_frees_slot | Passed |
| TEST-21 | Unknown appointment id | FR-06, FR-08 / "A valid unknown service lookup raises LookupError" | tests/test_services.py::test_unknown_appointment_id_raises_lookup_error | Passed |
| TEST-22 | Cancelled appointment kept | FR-06, FR-07 / AC-05.1, AC-05.2 | tests/test_services.py::test_cancel_retains_same_appointment | Passed |
| TEST-23 | Multiple service cancellation rejected | FR-06 / AC-05.3 | tests/test_services.py::test_repeated_service_cancel_is_rejected | Passed |
| TEST-24 | Cancelled appointment can be found amongst others | FR-06, FR-07 / AC-05.2 | tests/test_services.py::test_cancelled_appointment_is_retrievable_among_others | Passed |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| Validate Patient ID | '' or whitespace only | ValueError | TEST-02 |
| Validate Patient Name | Whitespace only | ValueError | TEST-03 |
| Validate Practitioner Fields | Blank ID, whitespace name, blank specialty | ValueError | TEST-05 |
| Validate Appointment Values | Invalid participants/status, text date/time, seconds, microseconds or timezone | ValueError | TEST-07 |
| Double cancellation | Appointment is already CANCELLED | ValueError. Status remains as CANCELLED. | TEST-09, TEST-23 |
| Status guard | Appointment is COMPLETED | ValueError. Status remains as COMPLETED. | TEST-10 |
| Duplicate trimmed ID | ' P1 ', then 'P1' | ValueError. Original is retained. | TEST-12 |
| Patient lookup | Unknown ID or incorrect case 'p1' | LookupError. Patient list unchanged. | TEST-13 |
| Patient lookup | '' or whitespace ID | ValueError. Patient list unchanged. | TEST-13 |
| Practitioner lookup | Unknown ID, '' or whitespace | LookupError or ValueError. Practitioner list unchanged. | TEST-15 |
| Unknown participant | Unknown practitioner | LookupError. Nothing stored. | TEST-17 |
| Practitioner conflict | Same practitioner, exact time, different patient | ValueError. Only original stored. | TEST-18 |
| Edge of conflict rule | Same practitioner, 1 minute later | Accepted. Both stored. | TEST-19 |
| Edge of conflict rule | Exact time, previous booking CANCELLED | Accepted. Cancelled booking stored. | TEST-20 |
| Unknown appointment | Find or cancel 'A9' | LookupError. A1 unchanged. | TEST-21 |


## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: FR-07 Retain the same appointment with CANCELLED status in current-session history.
Acceptance criterion: AC-05.2 "Cancelled history remains retrievable in the current session."
Behaviour to test: The same Appointment should remain in the system, can be found and is listed as CANCELLED after being cancelled.
Human-first test idea/categories: Valid: After a booked Appointment is cancelled, it can still be found and listed as CANCELLED. Invalid: If cancellation fails when attempting to cancel multiple times, Appointment remains in storage. Boundary: If Appointment has been cancelled but its slot has been rebooked, Appointment remains in storage.
Prompt and purpose: Create some test cases to critique from AC-05.2. Prompt used: Prompt from Part F of the Stage 7 handout, with requirement and acceptance criterion stated above. Tool used: Microsoft Copilot (browser). 

For each significant candidate, copy this entry as needed:
Candidate 1
- Copilot test idea/candidate: test_cancelled_appointment_is_retrievable_from_current_session_history
- What it claims to verify: Ensures the same appointment can still be found in the current session history with a status of CANCELLED.
- Requirement trace: FR-07, AC-05.2
- Assertion quality: Poor. Tests that there is a record with an id and compares status to a string of 'CANCELLED'. This means it could be passed if a copy was made and status doesn’t match our AppointmentStatus enum.
- Human critique: Uses client, fixtures and helper functions which SmartCare doesn’t have. Duplicate of TEST-22.
- Decision: Reject
- Reason: Fake API. Duplicate.
- Final test reference if accepted/modified: Not retained
- Actual verification result: Not run. Can’t be run on SmartCare.

Candidate 2
- Copilot test idea/candidate: test_non_cancelled_history_entry_does_not_satisfy_cancelled_history_requirement
- What it claims to verify: Ensures non cancelled appointments aren’t counted as cancelled history.
- Requirement trace: States it relates to FR-07 but neither FR-07 or AC-05.2 define what a cancelled history record is.
- Assertion quality: Unclear. No assertion provided. Relies on history which SmartCare doesn’t have.
- Human critique: All appointments are kept in the same list in SmartCare. Not a meaningful invalid case. Already tested in TEST-24 that another appointment remains scheduled.
- Decision: Reject
- Reason: Fake behaviour.
- Final test reference if accepted/modified: Not retained
- Actual verification result: Not run.

Candidate 3
- Copilot test idea/candidate: test_single_cancelled_appointment_remains_retrievable_when_it_is_the_only_history_entry
- What it claims to verify: Ensures a cancelled appointment can still be found when there is only one appointment stored.
- Requirement trace: FR-07, AC-05.2
- Assertion quality: No assertion provided. Scenario is valid but didn’t provide any assertion.
- Human critique: Already covered in TEST-22 with one appointment and same object, status, search and list assertions.
- Decision: Reject
- Reason: Duplicate of TEST-22.
- Final test reference if accepted/modified: Not retained
- Actual verification result: Not run.

Candidate 4
- Copilot test idea/candidate: test_latest_action_is_cancellation_and_cancelled_appointment_remains_retrievable
- What it claims to verify: Ensures appointment can be found immediately after it has been cancelled.
- Requirement trace: FR-07, AC-05.2
- Assertion quality: No assertion provided. No time rules to test. ‘Immediately’ isn’t a real boundary.
- Human critique: Already tested in TEST-22 that it can be found immediately.
- Decision: Reject
- Reason: Not a real boundary.
- Final test reference if accepted/modified: Not retained
- Actual verification result: Not run.

Candidate 5
- Copilot test idea/candidate: test_cancelled_appointment_remains_retrievable_among_multiple_current_session_history_entries
- What it claims to verify: Ensures the cancelled appointment can still be found when there are multiple appointments stored.
- Requirement trace: FR-07, AC-05.2
- Assertion quality: No assertion provided. We added precise assertions to ensure it was the same object, status and stored in the list.
- Human critique: Adds a useful scenario that hasn’t been directly tested in previous tests. Cancelling one appointment should mean it is kept and another isn’t changed. Modified to use SmartCare services.
- Decision: Modify
- Reason: Added useful scenario.
- Final test reference if accepted/modified: tests/test_services.py::test_cancelled_appointment_is_retrievable_among_others (TEST-24)
- Actual verification result: Passed

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? Candidate 1: test_cancelled_appointment_is_retrievable_from_current_session_history. Clearly defined arrange act assert sections. Traced to AC-05.2.
Why was it weak? Used client, fixtures and helper functions which SmartCare doesn’t have. Only one assertion that checks status is a string of CANCELLED. Didn’t check that same object was kept.
How did you strengthen it? Not kept as it is covered by TEST-22 using SmartCare services. Uses ‘is’ to check same object. Checks status is AppointmentStatus.CANCELLED. Checks lookup and list_appointments().
Accepted / modified / rejected test decisions and evidence: See Part H. Candidates 1-4 were rejected. Candidate 5 was changed to become TEST-24. None were accepted.

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| python -m pytest | project/ | 0d154fdf56076a28115aebe06dd39574f6c11b98 | 46 | 0 | None | None | Full accumulated suite on main after PR #8 (https://github.com/Oliver11233211/ST1_Assingment_3/pull/8): 8 supplied, 19 domain and 19 service test cases all pass. |

Individual test runs and changed-order independence evidence: Running the tests individually on main (commit 0d154fd): python -m pytest tests/test_domain.py::test_cancel_changes_status → 1 test passed. Running the tests in a different order (service test first): python -m pytest tests/test_services.py::test_cancelled_appointment_is_retrievable_among_others tests/test_domain.py::test_cancel_changes_status → 2 tests passed. Each test has its own independent setup.
Optional tutor-led demonstration notes: 
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: FR-01 to FR-08 → TEST-12 to TEST-20. First run of tests on branch feature/stage07-tests → 6 tests failed. 27 tests passed. Error: NameError: name 'build_services' is not defined. Test error: Test file test_services.py only had the new tests from stage 7 added as the stage 6 file wasn’t on main yet. Fixed by removing the incomplete file, merging in feature/stage06-service-tests and adding the stage 7 tests again. No changes to production code. 45 tests passed. After TEST-24 (https://github.com/Oliver11233211/ST1_Assingment_3/pull/8) 46 tests passed.

## K What the Suite Still Does Not Prove

What does your test suite still not prove? We have proven that the scenarios we tested perform correctly, however we have not tested the console menu or Stage 9 queries. The tests also cannot prove SmartCare fulfils the actual needs of the clinic staff (validation).
Coverage if used: Not used.
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? We have no measurement of coverage. The console and stage 9 features are also important as they are not tested. Knowing the coverage percentage will not tell us if our assertion proves the correct behaviour.
Optional fixtures/parametrisation used and why, if any: Parametrisation has been used within TEST-02, 05, 07, 13 and 15 to allow testing of a single behaviour using multiple meaningful inputs. Fixtures have not been used however there are small helper functions to build the services and appointment which create new states for every test.

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| Stage 7 Activity 2 (no issue) | stage07-edits | https://github.com/Oliver11233211/ST1_Assingment_3/pull/1 | None recorded | None recorded | Merged by Unavailable-11 (68354f9). PR #2 merged main back into this branch by mistake; no files changed |
| https://github.com/Oliver11233211/ST1_Assingment_3/issues/3 Add Stage 6 service tests | feature/stage06-service-tests | https://github.com/Oliver11233211/ST1_Assingment_3/pull/4 | Josh-Uni1 | No review submitted; merged without approval | Merged by Josh-Uni1 (d821f29) |
| https://github.com/Oliver11233211/ST1_Assingment_3/issues/5 Stage 7 test planning and written responses | stage07-planning-pre-test | https://github.com/Oliver11233211/ST1_Assingment_3/pull/6 | Josh-Uni1 | Approved ("Approve") | Merged by Josh-Uni1 (9331306) |
| https://github.com/Oliver11233211/ST1_Assingment_3/issues/7 Add Stage 7 domain and service tests | feature/stage07-tests | https://github.com/Oliver11233211/ST1_Assingment_3/pull/8 | Josh-Uni1 | Approved with no comment | Merged by Josh-Uni1 (0d154fd) |
| https://github.com/Oliver11233211/ST1_Assingment_3/issues/9 Complete Stage 7 evidence record | feature/stage07-completion | https://github.com/Oliver11233211/ST1_Assingment_3/pull/10 | <<reviewer>> | <<their feedback>> | <<merged, with SHA>> |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| Unavailable-11 (Abdullah Omer) | Stage 7 record (Parts A to O), test design and traceability, Stage 6 and Stage 7 tests, Copilot critique, diagnosis of the NameError setup failure, and integration. | https://github.com/Oliver11233211/ST1_Assingment_3/pull/4, https://github.com/Oliver11233211/ST1_Assingment_3/pull/6, https://github.com/Oliver11233211/ST1_Assingment_3/pull/8 |
| Josh-Uni1 | Reviewed and merged PRs #4, #6 and #8; approved #6 and #8. | https://github.com/Oliver11233211/ST1_Assingment_3/pull/6, https://github.com/Oliver11233211/ST1_Assingment_3/pull/8 |

## N Formative Questions

1. What question does verification answer?

Verification answers the question "Has the system been developed to the requirements?" This is done through testing.

2. What question does validation answer?

Validation answers the question "Does the product fulfil its purpose?" This cannot be done through testing as the requirements might not be the right ones to fulfil the needs of the clinicians.

3. What is a unit test?

They test individual elements of a piece of functionality. They set up their own state, do one thing and make an assertion.

4. What is a pytest fixture?

Reusable setup functions. You can use them easily by using a simple function scope so that a new instance is created for each test ensuring the tests are independent.

```python
@pytest.fixture
def data_store():
    return SmartCareDataStore()
```

5. What is parametrisation in pytest?

It allows you to run the same test with many meaningful inputs. You can do this by using @pytest.mark.parametrize.

```python
@pytest.mark.parametrize('blank_id', ['', ' '])
def test_blank_patient_id_is_rejected(blank_id):
    with pytest.raises(ValueError):
        Patient(blank_id, 'Alex Example')
```

6. What is regression testing?

Testing all the tests that have been built up to ensure previous behaviour still works. Previous tests are kept.

7. What does code coverage tell us, and what does it not prove?

Tells us which parts of our code have been executed in the tests. This can help identify where we have left parts of the code untested. However it will not show us that the code meets the requirements, all requirements have been tested or that the assertions are good.

8. What makes an assertion weak?

An assertion is poor if it passes when the required behaviour has failed. For example assert True will always pass. assert appointment is not None will not show us that the correct appointment has been returned. Good assertions should check for the exact value, identity, status or exception.

9. What is the appropriate role of GitHub Copilot as a test assistant?

Copilot should be used to suggest tests. We should design our own tests however. Each test should be checked to ensure it relates to a requirement, can fail for the right reasons and no new rules are made up. We can then decide whether to use, change or ignore the suggested test. Only tests that have been run will count as verified.

10. What is the Stage 7 engineering rule?

A passing test only shows that the behaviour being tested for has been met. Every test should relate to a requirement and be able to fail for the correct reasons.

## O Stage Completion

Tested Stage 7 main SHA: 0d154fdf56076a28115aebe06dd39574f6c11b98
Full-suite result: All tests passed with command 'python -m pytest' executed in the project directory. (46 tests passed)
Unresolved defects and effect on baseline: No outstanding bugs affecting baseline.
Clean working tree and integration evidence: Working tree clean. Integration has been completed. Merged PR#8 into main (SHA: 0d154fd). Unavailable-11 pulled main branch and ran all tests which passed at this commit. (Josh-Uni1: All tests passed (46) at 0d154fd).
Stage 8 handover status: Stage8 is ready to be handed over. Once we have the setup tool from our tutor we will continue to develop on the main branch at commit 0d154fd. No tasks assigned for stage8.
All tutorial/formative responses and traceability/Copilot decisions complete: All tutorial/formative questions have been answered. Traceability/copilot decisions have been made.
