# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Group 5 Thursday tutorial
- Members, GitHub usernames and cohorts: u3298756 (github: Oliver11233211), u3327693 (github: Unavailable-11), (github: kathryn-n1), u3334456 (github: Josh-Uni1)  - All members are undergraduate 4483
- Repository URL: https://github.com/Oliver11233211/ST1_Assingment_3
- Starting SHA: e617468

## A Requirement to issue activities

### FR-02 Patient Search

- Title: find_patient
- Context: The workers for the clinic need to find specific patient details upon request.
- Requirement: When entering a valid patient id it must return with that patient's details
- Acceptance criteria: Raises errors when invalid ID entered, doesn't create new patient entry, retrieves correct details.
- Scope: Allows staff to look up and view patient details
- Definition of Done: When valid id entered, patient details are returned without creating new entry. Errors raised when invalid or empty id entered
- Owner: Thursday 2:30 PM Group 5
- Actual issue link:  services.py - class PractitionerService - https://github.com/Oliver11233211/ST1_Assingment_3/blob/main/project/smartcare/services.py

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: cancel_appointment
- Context: The clinic workers need to be able to cancel appointments at request, however they need to ability to look at past canceled appointments.
- Requirement: The function needs cancel the appointment through domain method but retain the appointment.
- Acceptance criteria: Cancels appointments in the domain whilst retaining them for future.
- Scope: Clinic workers have to cancel appointments in the system to notify practitioners at clients request. Records of the appointment must be retained.
- Definition of Done: existing appointments can be marked as canceled through the function, however it appointment can still be found after searching and is marked as canceled.
- Owner: Thursday 2:30 PM Group 5
- Actual issue link: services.py - class PractitionerService - https://github.com/Oliver11233211/ST1_Assingment_3/blob/main/project/smartcare/services.py

## B Commit quality

| Original example                               | Strong or Weak | Reason                                                                   |
|------------------------------------------------|----------------|--------------------------------------------------------------------------|
| changes                                        | Strong         | All changes that were made were double checked and implemented correctly |
| final version                                  | Weak           | Not all of the sections have been completed yet, so it is currently weak |
| Add patient search by ID                       | strong         | The code is simple but it does what is required                          |
| fix stuff                                      | weak           | Nothing was fixed as of yet as no issues have been found in this stage   |
| Prevent cancellation of completed appointments | weak           | There is no definition of completed appointmnets yet.                    |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: This pull request goes out of scope by creating new dependencies, changing unnecessary code and patient fields
- Responsibility and architecture concerns: This pull request could interfere with other parts of the code creating programing issues.
- Testing and review concerns: Could complicate testing and make code unnecessary complex.
- Changes to remove or separate, with reasons: No need to rename unrelated patient fields, or restructure unrelated code. Adding a new dependency for canceled appointment could be useful however may just end up making code too complex.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: What tests were completed
- Follow-up review question 1: Was the software functional?
- Follow-up review question 2: Is the software user-friendly?
- Follow-up review question 3: What tests were used and what specifically was tested/
- Follow-up review question 4: How was the software performance
- Follow-up review question 5: Suggestions for improvement
- Additional questions if useful: nil

## E Team workflow agreement

| Practice                             | Team agreement                                                     |
|--------------------------------------|--------------------------------------------------------------------|
| Branch naming                        | Keep it simple, but explain what it does                           |
| Commit message convention            | Keep simple and explain what was done                              |
| PR size                              | For large PRs, let team members know                               |
| Another-member review requirement    | All members will review all stages before final submission         |
| Merge rule                           | Code must contribute and be functional, all suggestions legitimate |
| Significant Copilot disclosure rule  | Copiolot can only be used for checking and learning. No cheating.  |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link          | Requirement                                                    | Owner                     | Acceptance criteria or precise link                 | Status   |
|---------------------|----------------------------------------------------------------|---------------------------|-----------------------------------------------------|----------|
| Practitioner-lookup | The program needed to search and return a specific file.       | Thursday 2:30 PM Group 5  | Raises errors under user error and retrieves data.  | Complete |
| Patient-lookup      | The program needed to search and return a specific fil         | Thursday 2:30 PM Group 5  | Raises errors under user error and retrieves data.  | Complete |
| Appointment-cancel  | The pregram needed to cancel an appointment, but not delete it | Thursday 2:30 PM Group 5  | Raises errors under user error and retrieves data.  | Complete |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

_No pull requests were made in this stage_

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: u3298756 - asked copilot to provide a short review of the current code
- Prompt/purpose and relevant issue/diff: please provide a short review of the above code, ignore comments.
- Summary of output: "The code is well-structured and mostly correct. The main issues are inconsistent input validation, missing validation in find_appointment(), and a few consistency improvements around error messages and lookup checks. These are relatively minor and the overall design is solid." - Microsoft copilot
- Human check against actual code, requirements and tests: Consistency was checked, and issues raised by AI were realised. 
- Decision — Accept / Modify / Reject: Modify
- Reason: Modifying input validation for find_appointment was raised, validation was then fixed.
- Verification/evidence: Issue fixed, line 147-147 services.py.

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: There were a few missing steps, however we could not find the root cause.
- Copilot noticed: Missing validation in find_..
- Overlap: The root cause of the missing steps I found were highlighted by the AI
- What did the human reviewer notice that Copilot did not: 
- What did Copilot identify that the human reviewer initially missed: Missing validation in find_appointment
- Unsupported or incorrect Copilot suggestion: none identified with explanation
- Human judgement accepted, modified or rejected, and why: Judgement from both parties were considered and implemented as they helped patch small issues
- Which evidence justified merge approval: nil

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: u3298756
- Implementation: stage_06 .md and stage_06 services.py work
- Testing: All code runs and raises no errors when implemented properly
- Review: Reviewed by Copilot and myself
- Issue refinement: Fixed verification
- Design and responsibility discussion: I was tasked with completing stage_06
- Debugging or integration: nil
- Documentation or team support: nil

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

It may have just been many commits of very little work

## L Stage 6 formative questions

1. What is version control?

A system that tracks and manages changes over time.

2. Why is a feature branch useful?

Developers can implement new codee or a bug fix without affecting the rest of the code

3. What makes a commit a good engineering commit?

It contains meaning full changes, good justification and is well communicated to future developers or the rest of the team.

4. What is a pull request?

A proposal to merge code from one branch to another

5. What is the purpose of code review?

To review elements of the code to determine if it mets requirements.

6. What does a Git diff show?

It shows what is in the program but not uploaded to the github.

7. What is a Definition of Done?

The point of when the program needs no further modification to be implemented.

8. What is the appropriate role of GitHub Copilot in pull-request review?

It can identify any potential bugs or security risks that may be overlooked by human eyes.

9. Why should individual contribution not be judged only by commit count?

As contribution also depends on quality of the commits, rather than many commits of poor quality.

10. What is the Stage 6 engineering rule?

Communication regarding commits and class based programming

## M Completion and handover

- Starting SHA: e617468
- Final Stage 6 code SHA: 16c58ab
- Test command: exec.read()
- Working directory: Project
- Observed result: test passed
- PR and another-member reviewer: nil
- Unresolved issue or none: nil
- Stage 7 handover status: ready for tutor checkpoint
- Final submitted SHA if later than tested SHA: nil

- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [x] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [x] Human-first review and required Copilot comparison recorded.
- [x] Feedback resolved and approval recorded before merge.
- [x] Everyone pulled main and integrated checks passed.
- [x] Required activities, quiz responses and contribution notes completed.
- [x] Only synthetic data included; confidential peer material kept out.
- [x] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.