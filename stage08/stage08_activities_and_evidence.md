# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [Thursday 2:30 - 4:30 Group 5]
Members and UG/PG cohorts: [Oliver11233211, Unavailable-11 (Abdullah Omer), kathryn-n1, Josh-Uni1 (GitHub usernames)]. All members are undergrad
Record owner / contribution links for each member: [https://github.com/Oliver11233211/ST1_Assingment_3]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: 
1. "Appointment disappears after cancellation" - symptom. It describes what a user sees, not why.
2. "The data-store removal path is probably being called" - hypothesis. It is a guess at the cause.
3. "The failing test shows store.find_appointment('A1) returns None" - evidence. It is an observable and repeatable result.
4. "The service layer is badly designed" - opinion. It is a vague judgement
5. Trackback points to smartcare/services.py" - evidence

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: 
1. Expected: After A1 is cancelled, find_appointment('A1) returns the same object with status CANCELLED
2. Observed: Cancel_appointment('A1) returns A1 as CANCELLED, but a later find_appointment('A1') raises LookupError: Appointment not found, and store.find_appointment('A1') returns None.
3. Minimal reproduction: new SmartCareDataStore → register P1 and D1 → book A1 at 2026-10-01 09:00 → cancel_appointment('A1') → store.find_appointment('A1')
4. Initial hypothesis, cancellation deletes A1 from the store
5. Evidence to inspect: Whether A1 is still in list_appointments() after cancelling
6. Outcome: List_appointments() still contained A1 as CANCELLED, which disproved deletion.
 
### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: The test is defective and should be changed. Expected behaviour comes from the requriements, and FR-07 and BR-07 say cancellation keeps the record. The product must not be changed to delete records just to make that test pass. The corrected test should assert that the same object is found and listed with status CANCELLED.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: 
1. Long method: Split it into small named steps
2. Duplicate status strings: These are magic strings
3. Direct collection manipulation
4. Printing: This mixes input/output with workflow logic.
5. Validation in the service: This duplicates domain rules
6. Four nested conditionals

Classification:
1. Rename appt to appointment: Refactoring
2. extract a repeated conflict helper: refactoring
3. add rescheduling: feature
4. Restore retained cancellation lookup: repair
5. Replace a magic status string with the existing enum: refactoring

Behaviour that must not change includes, returned object identity, exception types, unchanged stored state after a rejecttion

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: Failure:
1. exception: LookupError: Appointment not found.
2. expected: find_appointment('A1) is appointment, with status CANCELLED
3. Call path: test -> AppointmentService.find_appointment('A1) -> SmartCareDataStore.find_appointment('A1) returns None -> the service raises LookupError

Ranked causes:
1. The store lookup skips cancelled appointments. Check: after cancelling, A1 is in list_appointments()
2. Cancellation removes A2 from _appointments . Check: whether A1 is missing from list_appointments()
3. Lookup key mismatch. Check: store.find_appointment('A1') before cancelling.

Why a traceback is not enough? It shows where the exception was raised, not where the wrong value came from.

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: Without a reproduction and a tested hypothesis, it's guesswork. A quick edit can hide the symptom without fixing the cause.


Classification responses (1–5, each with reason): [see A.1]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [see A.3]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [see A.5]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [0d154fd (PR #8 merge), SmartCare A3 Requirements Baseline 2026, revision 2.]
- Baseline test command / working directory / observed result / evidence: [python -m pytest -q / project/ / 46 passed, 0 failed. Rerun on eb2b92c also gave 46 passed (Python 3.13, pytest 8.3.5).]
- Clean preparation SHA if a record-only commit followed Stage 7: [eb2b92c (PR #10: only the stage07 record changed)]
- Branch and preparer / how teammates obtained this branch: [debug/stage08, prepared by Unavailable-11 and pushed to origin]
- Downloaded tool version, source SHA256 and --check outcome: [prepare_debugging.py v1.1]
- --apply and --verify output summaries / artefact references: [preparer: summary of --apply and -- verify output]
- Bounded diff inspected and recovery location (not committed): [git diff 7d81d3a 1f3e496 -- project]
- Prepared faulty-state commit SHA: [1f3e496]
- Preparation or recovery issues and resolution, if any: [preparer to complete, or "none"]
- Initial prepared full-suite command / result / key failures: [python -m pytest -q in project/ → 5 failed, 41 passed. Conflict failures: test_starter.py::test_conflict_rule_and_different_practitioner and test_services.py::test_same_practitioner_same_time_conflicts (DID NOT RAISE ValueError). Cancelled-lookup failures: test_services.py::test_cancel_retains_same_appointment, test_repeated_service_cancel_is_rejected and test_cancelled_appointment_is_retrievable_among_others (LookupError: Appointment not found). After adding tests/test_regressions.py: 7 failed, 41 passed.]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [The same practitioner can be double booked]
- Expected behaviour and requirement: [Same practitioner + exact tiem + scheduled -> ValueError]
- Minimal synthetic reproduction steps: [Register P1, P2, D1, D2]
- Meaningful failing test path/name and exact relevant failure: [tests/test_regressions.py::test_f8_01_same_practitioner_same_time_rejected_other_allowed → Failed: DID NOT RAISE <class 'ValueError'>]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [in SmartCareDataStore.has_practitioner_conflict, the practitioner comparison is != instead of ==]
- Smallest justified fix / diff / why other behaviour is preserved: [change the one operator != → ==]
- Repair SHA / focused verification result: [4c850aa. The F8-01 regression test, both conflict tests, one-minute-later and cancelled slot -> 5 passed. Full suite: 44 passed, 4 failed]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [After cancellation the appointment disapears.]
- Expected behaviour and requirement: [The same object is kept with status CANCELLED]
- Minimal synthetic reproduction steps: [Register P1, D1 -> book A1]
- Meaningful failing test path/name and exact relevant failure: [tests/test_regressions.py::test_f8_02_cancelled_appointment_remains_retrievable → assert None is <Appointment> where None = find_appointment('A1')]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [SmartCareDataStore.find_appointment was changed from a dictionary lookup to a loop]
- Smallest justified fix / diff / why other behaviour is preserved: [Restore the contract lookup]
- Repair SHA / focused verification result: [cb7a991. F8-02 regression test, the three service cancellation tests and the unknown ID test -> 5 passed. Full suite: 48 passed]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [The conflict check compares the practitioner incorrectly. This is plausible because same-practitioner bookings are accepted]
Evidence intended to inspect / competing explanation / discriminating check: [Inspect each condition in has_practitioner_conflict]
Member and saved sequence/time or commit showing this preceded consultation: [Josh-Uni1, 07/11/26, 6:30 committed before Copilot]

### F8-02 human entry
Likely cause and why plausible: [Cancellation deletes the appointment from the store. This is plausible because the symptom is "not found" immediatley after cancel]
Evidence intended to inspect / competing explanation / discriminating check: [Inspect list_appointments() The record is kept but the lookup filters it out. Check: if A1 is still listed after cancel, deletion is ruled out]
Member and saved sequence/time or commit showing this preceded consultation: [Josh-Uni1 07/11/26, 6:30]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [Prompt: Handout section 7 structure, filled for F8-01. Output: C:\stage8-files\copilot_F8-01.txt (https://github.com/Oliver11233211/ST1_Assingment_3/issues/11#issuecomment-6707160036) / Josh-Uni1]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [Inverted practitioner comparison: data_store.py:110 uses != so the check matches every other practitioner / check: compare the stored practitioner ID with the argument for D1 and D2 / observed: has_practitioner_conflict('D1', 09:00) = False and ('D2', 09:00) = True, exactly inverted; changing != to == made the F8-01 test and both conflict tests pass / correct / accept – matches our direct store evidence and the one-operator fix.]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [Booking passes a different practitioner ID or uses a different store from the direct check / check: trace the ID passed at services.py:131 and confirm one SmartCareDataStore instance / observed: services.py:131 passes practitioner.practitioner_id from the same store; the direct store call is already wrong with no service involved / wrong / reject – the fault reproduces at store level, and services.py was never changed yet all tests pass after the store fix.]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [Datetime or status condition (data_store.py:111–112) does not match A1 / check: inspect A1's date_time, status.value and exclude_appointment_id / observed: the D2 call returned True, so the time and status conditions did match; test_same_practitioner_one_minute_later_is_allowed and test_cancelled_booking_frees_slot passed even in the faulty state / wrong / reject – time and status filters behave correctly; only the practitioner operator was changed.]
Final human conclusion and comparison with initial hypothesis: [the initial hypothesis (practitioner comparison wrong) was supported and narrowed to `!=` instead of `==`. The direct D1/D2 check confirmed it (C). Copilot ranked the same cause first as our hypothesis and correctly ranked the service and store-instance explanations lower]

### F8-02 Copilot review
Actual prompt / output reference and member: [Prompt: Handout section 7 structure, filled for F8-02. Output: C:\stage8-files\copilot_F8-02.txt (https://github.com/Oliver11233211/ST1_Assingment_3/issues/12#issuecomment-6707179065) \ Josh-Uni1]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [Store lookup filters out cancelled appointments: find_appointment only returns a match when status.value != "cancelled" / check: compare A1's status after cancel with the lookup condition / observed: after cancel, A1 is CANCELLED and still in list_appointments(), but store.find_appointment('A1') returns None (test_regressions.py:60) / correct / accept – restoring the dictionary lookup made all 5 F8-02-related tests pass.]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [Service turns None into LookupError, so a repeat cancel never reaches Appointment.cancel() / check: trace the store lookup in both service calls; call appointment.cancel() directly a second time / observed: services.py:151–152 and 162–164 raise LookupError when the store returns None; a direct second cancel() raises ValueError as expected / partly correct / modify – accurate explanation of why the symptom is LookupError not ValueError, but it is a consequence of cause 1, not a separate cause; services.py was not changed and passed after the store fix.]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [Code runs against a different store instance or implementation / check: confirm the test and service share one store and check the module path / observed: the regression test uses a single store; list_appointments() and find_appointment() on that same store disagree (A1 listed, lookup None) / wrong / reject – no evidence for it; fixing find_appointment alone resolved the failure.]
Final human conclusion and comparison with initial hypothesis: [the initial hypothesis (deletion) was disproved: A1 was still in `list_appointments()`. The supported cause is the status filter in `find_appointment` (D). Copilot ranked the status filter first, which contradicted our initial deletion hypothesis; our list_appointments() check had already ruled deletion out, so Copilot's ranking agreed with our final diagnosis.]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [63b3ce3] | [ python -m pytest -q tests/test_regressions.py / project/] | [F8-01 test failed: DID NOT RAISE ValueError] |
| F8-01 after repair | [4c850aa] | [python -m pytest -q / project/] | [ F8-01 test passes; full suite 44 passed, 4 failed] |
| F8-02 before repair | [4c850aa] | [python -m pytest -q tests/test_regressions.py / project/] | F8-02 test failed: assert None is <Appointment> |
| F8-02 after repair | [cb7a991] | [python -m pytest -q / project/] | [48 passed] |
| Full suite after both repairs, before refactor | [cb7a991] | [python -m pytest -q / project/] | [48 passed, 0 failed] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [F8-01: The test needs a ValueError for the same practitioner at the same time and checks only A1 is stored, then checks a different practitioner can still book. An inverted check fails one half or the other. F8-02: The test checks the cancelled appointment is the same object, is CANCELLED, is still listed, and is found by both the store and the service, then that a second cancel raises ValueError. All 46 earlier tests were kept, so earlier behaviour is protected]
Unrelated failures investigated / resolution: [Not applicable. All failures came from the two prepared faults]

## H. Refactoring decision and before/after verification

Smell and exact location: [Magic status string in project/smartcare/data_store.py, has _practitioner_conflict: appointment.status.value == "scheduled". It repeats the AppointmentStatus enum as a string, so a typo would silently never match]
Small proposed structural change / why justified: [Use appointment.status is AppointmentStatus.SCHEDULED and restore the docstring]
External behaviour to preserve / relevant tests: [Same True/False result for every input. Only SCHEDULED appointments confict. Tests: Both regression tests, test_conflict_rule_and_different_practitioner, test_same_practitioner_same_time_conflicts, test_same_practitioner_one_minute_later_is_allowed, test_cancelled_booking_frees_slot.]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [ac590a8]
Focused and full after-refactor commands / working directory / results / evidence: [python -m pytest -q / project/ -> 48 passed. python main.py demo output unchanged]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [Accepted. The same tests passed before and after with no test changes, so behaviour is preserved]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [F8-01 #11 (Josh-Uni1), F8-02 #12 (Josh-Uni1), refactor #13 (Josh-Uni1) - https://github.com/Oliver11233211/ST1_Assingment_3/issues ]
Branch / prepared, repair and refactor checkpoints: [debug/stage08: prepared 1f3e496 → Part E af2edff → tests 63b3ce3 → F8-01 repair 4c850aa → F8-02 repair cb7a991 → refactor ac590a8]
PR link and another member's reviewer identity: [(https://github.com/Oliver11233211/ST1_Assingment_3/pull/14), Unavailable-11]
Key human feedback, difference from Copilot findings and response/outcome: [The human feedback was just an approval of what was already completed]
Actual review approval / merge evidence: [Approved by Unavailable-11, merged by Josh-Uni1]
Integrated code SHA and team pull/retest command / working directory / result: [git pull then python -m pytest -q / project/ / Josh-Uni1 48 passed; Oliver11233211 48 passed; kathryn-n1 48 passed; Unavailable-11 48 passed]
Evidence-only later SHA / explanation if different: [This stage08-evidence commit changes only this record]
Each member's substantive contribution and artefact: [Every member of the group ran the code and all got the 48 passed message.]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [F8-02 suggestion 3 (a different store instance or implementation) sounded convincing because it used technical detail about runtime module paths but it had no supporting evidence. F8-01 suggestion 2 was similar, plausible in general, but contradicted by the store-level reproduction. Neither was accepted without a check]
2. What evidence changed your group's view? [Our F8-02 hypothesis was that cancellation deletes the record. The regression test showed that cancel_appointment returned A1 as CANCELLED and that A1 was still in list_appointments(), while store.find_appointment('A1') returned None. The record had been kept and the lookup was hiding it, sowe inspected find_appointment rather than cancel()]
3. How did regression tests protect the refactoring? [We refactored only after all 48 tests passed. The same unchanged tests, including both regression tests and the one-minute-later, cancelled-slot and different-practitioner cases passed again afterwards. If replacing "scheduled" with AppointmentStatus.SCHEDULED had changed which appointments count as conflicts, one of those tests would have failed.]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [Reproduce it and record the expected behaviour, the observed behaviour, a minimal reproduction and the failing test. Then form a hypothesis and check it against evidence before editing]

2. Where should expected behaviour come from during debugging?

Response: [From the requirements baseline, not from what the code currently does.]

3. What is a debugging hypothesis?

Response: [A specific and testable explanation of the cause of a failure]

4. What is a regression test and why is it retained?

Response: [A test that would have caught a defect, kept in the suite after the fix. It stays so the defect doesn't come back]

5. What is meant by root cause?

Response: [A root cause is the actual reason behind a symptom]

6. What is refactoring?

Response: [Changing the code's structure to make it clearer or easier to maintain without changin its external behaviour]

7. What is a swallowed exception?

Response: [An exception that is caught and then ignored or hidden.]

8. What is a code smell?

Response: [A sign in the code that suggests a design problem]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [As hypotheses to test and not to be taken as conclusions]

10. What is the Stage 8 engineering rule?

Response: [Diagnose before changing]

## L. Completion and handover

- [X] Existing project, earlier tests and stage records preserved.
- [X] Passing Stage 7 SHA and safe preparation details recorded.
- [X] Both defects reproduced with meaningful failing tests.
- [X] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [X] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [X] One genuine refactor verified under passing before/after tests.
- [X] Human PR review, feedback resolution and integrated retest recorded.
- [X] Tutorial, three reflections and ten formative responses complete.
- [X] Local recovery metadata excluded from submitted source.
- [X] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [863e5f4. The later stage08-evidence commit changes only this record]
Unresolved issues or incomplete checks / owner / next action: [None. All checks complete and no unresolved code defects]
Handover note: [Both faults repaired, regression tests added and refactor verified]