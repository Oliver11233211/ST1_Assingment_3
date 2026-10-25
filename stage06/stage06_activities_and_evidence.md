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
- Owner: [response]     #### Not too sure what to put in these two!!!
- Actual issue link: [response]

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: cancel_appointment
- Context: The clinic workers need to be able to cancel appointments at request, however they need to ability to look at past canceled appointments.
- Requirement: The function needs cancel the appointment through domain method but retain the appointment.
- Acceptance criteria: Cancels appointments in the domain whilst retaining them for future.
- Scope: Clinic workers have to cancel appointments in the system to notify practitioners at clients request. Records of the appointment must be retained.
- Definition of Done: existing appointments can be marked as canceled through the function, however it appointment can still be found after searching and is marked as canceled.
- Owner: [response] ####### Not too sure what to put in these two!!!
- Actual issue link: [response]

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

| Practice                            | Team agreement |
|-------------------------------------|----------------|
| Branch naming                       | [response]     |
| Commit message convention           | [response]     |
| PR size                             | [response]     |
| Another-member review requirement   | [response]     |
| Merge rule                          | [response]     |
| Significant Copilot disclosure rule | [response]     |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner      | Acceptance criteria or precise link | Status     |
|------------|-------------|------------|-------------------------------------|------------|
| [issue 1]  | [response]  | [response] | [response]                          | [response] |
| [issue 2]  | [response]  | [response] | [response]                          | [response] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

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

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: u3298756
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[response]

## L Stage 6 formative questions

1. What is version control?

[response]

2. Why is a feature branch useful?

[response]

3. What makes a commit a good engineering commit?

[response]

4. What is a pull request?

[response]

5. What is the purpose of code review?

[response]

6. What does a Git diff show?

[response]

7. What is a Definition of Done?

[response]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[response]

9. Why should individual contribution not be judged only by commit count?

[response]

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
