# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Thursday 2:30 - 4:30 Group 5 \
Members: u3298756, u3327693, u3299455, u3334456\
Stage 8 integrated SHA: 32d8f09 \
Command: python3 -m pytest -q \
Working directory: st1-assignment-3\
Actual result: 48 passed in 0.09s

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason                                               |
|---|-------------------------|---------------------------------------------------------------------|
| Patient identity | Required session/domain | Required to identify the registered patients                        |
| Appointment history | Required session/domain | Required to identify the scheduled or past appointments             |
| Temporary menu choice | Transient               | Used of actions                                                     |
| Practitioner specialty | Required session/domain | Required for practitioner information                               |
| Debug print output | Transient               | Used for finding problems in the program                            |
| Appointment status | Required session/domain | Required to see if appointment is scheduled, cancelled or completed |

What is intentionally lost on exit? \
On exit, all records of patients, practitioners, and appointments are lost as the program only stores information temporarily.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types                   | Outputs                 | Responsibility and validation                            | Domain source / existing constraint               |
|---|---------------------------------------------|-------------------------|----------------------------------------------------------|---------------------------------------------------|
| appointment_sort_key | Appointment object                          | Date and appointment ID | Sorting key that does not change appointment             | date_time and appointment_id from Appointment     |
| select_appointments | List of appointments and appointment status | New appointments        | Filters appointments without changing list               | Practitioner objects associated with appointments |
| Service listing | Practitioner ID                             | List of appointments    | Validates practitioner and status prior to calling query | SmartCareDataStore and select_appointments        |
| Console | Input from user                             | Shows error messages    | Display information and collect input data               | SmartCare services and  rules             |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: \
patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status are related as these objects need to be referenced with each other to confirm and validate appointments in SmartCare.

### A3 Responsibility violations

| Conceptual case | Violation                                | Correct boundary and reason                                                                  |
|---|------------------------------------------|----------------------------------------------------------------------------------------------|
| Appointment.cancel reads input | Appointment is interacting with user     | Input should be collect by the console and Appointment.cancel applies rules for cancellation |
| Service prints/reads the menu | User tasks performed by service          | Services should handle operations and console should read menu                               |
| Query sorts its source in place | Appointment list is changed by the query | The original appointment list should remain the same as query uses sorted()                  |
| Store prints Appointment saved | Data store information displayed to user | Saved appointments should be returned by store while console prints message                  |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. \
appointments.sort(key=appointment_sort_key): list is changed to a sorted order, returns nothing, sorts list\
result = sorted(appointments, key=appointment_sort_key): list remains unchanged, returns a sorted new list, new list with same objects\

Give a meaningful mutation check:\
original = appointments.copy()\
result = sorted(appointments, key=appointment_sort_key)\
assert appointments == original\
assert results is not appointments

Score-example prediction and explanation of passing the named key: 



### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: \
When an appointment is cancelled it will remain in the system showing the appointment status as cancelled. However, deletion would delete the appointment from the system. For SmartCare the cancelled appointments need to remain in the system under a cancelled status. \
Same-session would be checked by cancelling an appointment (A1) and checking to see if it remains in the system and is now under a cancelled status.\
All-status listing can be checked by checking if the appointment (A1) is still in the system when search through all appointments in the list.\
SCHEDULED-only can be checked filtering appointments by 'SCHEDULED' and checking it is not listed due to its cancelled status.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- response -->

| Requirement | Input / session data                               | Operation and responsible component                                | Expected result or error                                                  | Test / evidence                                                           |
|--------|----------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| QRY-01 | Practitioner ID, appointment list                  | select_appointments() and filter by practitioner                   | Returns appointments for specific practitioner                            | Create appointments for practitioners and test filter by one practitioner |
| QRY-02 | Appointment list                                   | select_appointments() and filter by status                         | Returns all appointment statuses                                          | Test appointment status filter for scheduled, cancelled, and completed    |
| QRY-03 | Appointment ID, date_time                          | select_appointments(), appointments.sort(key=appointment_sort_key) | Returns appointments ordered by date_time                                 | Test appointment times                                                    |
| QRY-04 | Practitioner ID                                    | practitioner_appointments                                          | Returns practitioner list if valid, otherwise error is raised             | Test practitioner ID                                                      |
| FP-01  | Appointment ID                                     | pure query function passes                                         | Returns results that has unchanged inputs                                 | Check code for side effects                                               |
| FP-02  | Appointment list                                   | new sorted list                                                    | Returns original list                                                     | Check mutation                                                            |
| FP-03  | Appointment object                                 | appointments.sort(key=appointment_sort_key)                        | Returns appointment ID and date_time                                      | Test sorting key                                                          |
| UI-01  | Patient, practitioner, and appointment information | display booking, cancellation, lists                               | Reject conflicting appointments and keep cancelled appointments on record | Run menu and check outputs                                                |
| UI-02  | Appointment status, date_time, conflicts           | identifies errors                                                  | Returns error                                                             | Check error return                                                        |
Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: \
A registered practioner with no patients will return an empty list whereas, an unknown practitioner will raise a LookupError. The enum conversion converts text into enum and the actual object identity avoids duplicating objects by referencing registered objects. Error handling returns an error and displays a message and an unchanged state on rejection means invalid requests won't change records that already exist within the system.  

## C. Implementation and query verification

| Requirement / test ID       | Code location                                       | Case and meaningful assertion                                                          | Actual result                                                                                                                          | Evidence link              |
|-----------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| QRY-01 isolate practitioner | select_appointments()                               | Create appointments for D1 and D2 and assert filter by filtering D1                    | PASS - only D1's appointment returned                                                                                                  | project/tests/test_queries |
| QRY-02 default statuses     | select_appointments()                               | Assert, scheduled, cancelled, completed statuses                                       | PASS - SCHEDULED, CANCELLED, COMPLETED filters worked                                                                                  | project/tests/test_queries |
| QRY-03 date/time ordering   | select_appointments(), appointments.sort(key=appointment_sort_key)                             | Assert appointments are sorted and ordered from earliest to latest                     | PASS - fields unchanged as date/time sorts appointments                                                                                | project/tests/test_queries              |
| QRY-04 unknown ID           | AppointmentService.list_practitioner_appointments() | Enter an unvalid practitioner ID and assert a LookupError is returned                  | PASS - empty list returned for practitioners with no appointments, LookupError for unknown practitioner, and ValueError for invalid ID | project/tests/test_queries               |
| FP-01 no side effects       | select_appointments()                               | Check code for global state                                                            | PASS - same ordered results                                                                                                            | project/tests/test_queries              |
| FP-02 unchanged objects     | select_appointments()                               | After the query, check that both original list order and field values remain unchanged | PASS - unchanged fields and original order                                                                                             | project/tests/test_queries             |
| FP-03 named key             | appointments.sort(key=appointment_sort_key)         | Key returns, appointment ID, date_time and sorts using key                             | PASS - date/time and sorting order are correct                                                                                         | project/tests/test_queries       |


Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- response -->
What the tests do and do not establish: <!-- response -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | | | | |
| UI-02 invalid-input recovery | | | | |
| Automated service workflow | | | | |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: <!-- paste or accessible reference -->
Actual response: <!-- accessible reference -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| | | | | | |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
