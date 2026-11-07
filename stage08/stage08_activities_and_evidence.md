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
- Repair SHA / focused verification result: [the F8-01 regression test, both confilct tests, one-minute-later and cancelled slot -> 5 passed. Full suite: 44 passed, 4 failed]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [After cancellation the appointment disapears.]
- Expected behaviour and requirement: [The same object is kept with status CANCELLED]
- Minimal synthetic reproduction steps: [Register P1, D1 -> book A1]
- Meaningful failing test path/name and exact relevant failure: [tests/test_regressions.py::test_f8_02_cancelled_appointment_remains_retrievable → assert None is <Appointment> where None = find_appointment('A1')]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [SmartCareDataStore.find_appointment was changed from a dictionary lookup to a loop]
- Smallest justified fix / diff / why other behaviour is preserved: [Restore the contract lookup]
- Repair SHA / focused verification result: [F8-02 regression test, the three service cancellation tests and the unknown ID test -> 5 passed.]

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
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [complete] | [complete] | [complete] |
| F8-01 after repair | [complete] | [complete] | [complete] |
| F8-02 before repair | [complete] | [complete] | [complete] |
| F8-02 after repair | [complete] | [complete] | [complete] |
| Full suite after both repairs, before refactor | [complete] | [complete] | [complete] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]