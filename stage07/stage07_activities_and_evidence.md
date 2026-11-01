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
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

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

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
