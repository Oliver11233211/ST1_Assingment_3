# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Group 5 Thursday tutorial
Members and UG/PG applicability: u3298756 (github: Oliver11233211), u3327693 (github: Unavailable-11), (github: kathryn-n1), u3334456 (github: Josh-Uni1)  - All members are undergraduate 4483


## A Release scope and starting SHA

Release label/version and requirements baseline: Common UG, FR-01–FR-09; current QRY-01–04, FP-01–03 and UI requirements;
accumulated common tests; register/find patients and practitioners; valid
booking and conflict rules; cancellation/history; appointment lookup and
practitioner listing; console recovery; current-session data only. 

Common starting SHA / branch / applicable members: 5a9e389d054f8db43c9bdca4965f46e4a0f14eea

PG starting SHA / branch / applicable members or not applicable: Not applicable

Working-state review and approved integration: reviewed

Protected common candidate and PG differences: Nil PG

Feature freeze / owner / verifier: Feature freeze


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: Release with conditions and continue development and bug fixes based on customer feedback, as long as the product is functional.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope                   | Evidence                                              | Location/link and SHA | Reviewer   | Sufficient? | Gap/action |
|-------------------------------------------------------|-------------------------------------------------------|----------------------|------------|-------------|------------|
| Cancellation history works                            | services.py                                           | [response]           | [response] | [response]  | [response] |
| Architecture responsibilities are appropriate         | All functions are separated by class with inheritance | [response]           | [response] | [response]  | [response] |
| Rescheduling is safe — PG only                        | nil                                                   | nil                  | nil        | nil    | nil   |
| AI use is responsible — common recheck / PG assurance | AI use was responsible and correctly documented       | [response]           | [response] | [response]  | [response] |
| System is maintainable                                | Pragram is correctly labeled and easy to maintain     | [response]           | [response] | [response]  | [response] |
| FR-01–03 register/find and validation                 | Validation is sufficient                              | [response]           | [response] | [response]  | [response] |
| FR-04–05 booking/conflict rules                       | Raise errors in place to prevent conflicts            | [response]           | [response] | [response]  | [response] |
| FR-06–08 cancellation/history/find                    | validated and raises errors                           | [response]           | [response] | [response]  | [response] |
| FR-09 and QRY/FP listing/filter/order/purity          | validates                                             | [response]           | [response] | [response]  | [response] |
| UI full console sequence and error recovery           | [response]                                            | [response]           | [response] | [response]  | [response] |
| Session-only scope / FR-10 retired                    | [response]                                            | [response]           | [response] | [response]  | [response] |
| PG RES and assurance integration                      | nil                                                   | nil  |  nil       | nil    | nil   |


## C Full regression results

| Suite/scope                              | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|------------------------------------------|---------------------|-------------------------------|------------|---------------|---------------|
| Complete common                          | [response]          | [response]                    | [response] | [response]    | [response]    |
| Complete PG if applicable                | [response]          | [response]                    | [response] | [response]    | [response]    |
| Affected focused checks after correction | [response]          | [response]                    | [response] | [response]    | [response]    |
| Full integrated recheck                  | [response]          | [response]                    | [response] | [response]    | [response]    |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step                                                        | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|------------------------------------------------------------------|-----------------------|----------------------|-----------------|---------------|
| Problem and stakeholders                                         | [response]            | [response]           | [response]      | [response]    |
| Register and find Patient and two Practitioners                  | [response]            | [response]           | [response]      | [response]    |
| Valid booking                                                    | [response]            | [response]           | [response]      | [response]    |
| Same practitioner exact-time conflict rejected                   | [response]            | [response]           | [response]      | [response]    |
| Different practitioner same time allowed                         | [response]            | [response]           | [response]      | [response]    |
| Cancel SCHEDULED and retain/find CANCELLED object                | [response]            | [response]           | [response]      | [response]    |
| Invalid/repeated cancellation rejected                           | [response]            | [response]           | [response]      | [response]    |
| Default all-status listing                                       | [response]            | [response]           | [response]      | [response]    |
| Explicit filtering / empty vs unknown / deterministic order      | [response]            | [response]           | [response]      | [response]    |
| Invalid date/status/menu/lookup recovery and continued operation | [response]            | [response]           | [response]      | [response]    |
| Session-only limitation and normal exit                          | [response]            | [response]           | [response]      | [response]    |
| One meaningful requirement-linked pytest test explained          | [response]            | [response]           | [response]      | [response]    |
| Architecture and one actual AI decision / known limitation       | [response]            | [response]           | [response]      | [response]    |
| PG reschedule identity/participants/time and no-op               | [response]            | [response]           | [response]      | [response]    |
| PG conflict/invalid status/failure non-mutation                  | [response]            | [response]           | [response]      | [response]    |
| PG old slot / current lookup/list ordering / assurance risks     | [response]            | [response]           | [response]      | [response]    |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area                                                     | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|-----------------------------------------------------------------|------------------------|-----------------------|----------------------------------|
| OOP responsibilities and pure-query boundaries                  | [response]             | [response]            | [response]                       |
| PascalCase and snake_case naming                                | [response]             | [response]            | [response]                       |
| Useful type hints and meaningful docstrings                     | [response]             | [response]            | [response]                       |
| Four-space indentation and imports/layout                       | [response]             | [response]            | [response]                       |
| Focused methods / duplication / dead or commented code          | [response]             | [response]            | [response]                       |
| Globals / leakage / unnecessary inheritance or frameworks       | [response]             | [response]            | [response]                       |
| No SQLite/persistence/repository ABCs/speculative features      | [response]             | [response]            | [response]                       |
| Synthetic data / secrets / dependencies / provenance            | [response]             | [response]            | [response]                       |
| Significant common Copilot contributions and human verification | [response]             | [response]            | [response]                       |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST           | [response]             | [response]            | [response]                       |

| AI claim   | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|------------|---------------------------|-------------|---------------------------------|------------------------------------|
| [response] | [response]                | [response]  | [response]                      | [response]                         |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item                                                   | Location   | Verifier   | Result/gap |
|---------------------------------------------------------------|------------|------------|------------|
| Purpose and included common/PG scope                          | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations               | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands        | [response] | [response] | [response] |
| Repository structure and architecture responsibilities        | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule                  | [response] | [response] | [response] |
| Release label/version and SHA links                           | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item  | Impact     | Priority   | Future action | Accepted? / release rationale |
|------------|------------|------------|---------------|-------------------------------|
| [response] | [response] | [response] | [response]    | [response]                    |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|-------------------|--------------------------|-----------------|--------------|-----------------|----------------------|----------------|
| [response]        | [response]               | [response]      | [response]   | [response]      | [response]           | [response]     |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? Version of software that is considered ready for release.

2. What is feature freeze and why is it used? The point where no new features can be added to the software to allow engineers to stabilise the program.

3. What is regression testing in a release context? Re running of tests after making any changes.

4. What is a known limitation? A documented defect in the software

5. What is technical debt? The future cost of choosing a quicker or simpler solution

6. What are release notes? Documents that summarise version changes.

7. What is software maintenance? ongoing support and changes after the software has been released.

8. What is the purpose of the individual demonstration/viva? to verify the student understands what they have created

9. What should the final responsible-AI check establish before release? Ensure any AI work has been verified by a human engineer

10. What is the main course conclusion about AI and the role of the software engineer? AI is a useful and powerful tool however responsibility falls upon the engineer.


## N Reflection viva and handover

Strongest evidence SmartCare is ready: Appointments and people in system are validated and stored correctly

Weakest area: Human interaction with software

How AI use changed from Stage 1 to Stage 12: Used more as a tool rather than a guide

Start doing — engineering and AI use: treat AI like a tool not an instruction paper

Stop doing — engineering and AI use: Letting AI make the decisions for the software engineer

Continue doing — engineering and AI use: Using it as a tool

What worked / caused rework / future delivery improvement: Document changes amongst peers better for those who didn't work on specific sections.

One paragraph — If AI can write code why do we still need software engineers: Writing the code is only part of the job. A software engineer has to design a program base on functional requirenemnts from the client and build the software from that. While AI is capable of writing the code to do those, an engineer is still required to review, test, de-bug and assure that functional requirements are met. Furthermore, an AI agent cannot leaise with the client to update any features or any changes.

| Preparation item                                                                  | Own explanation and evidence link |
|-----------------------------------------------------------------------------------|-----------------------------------|
| Problem and stakeholders                                                          | [response]                        |
| Two requirements and acceptance criteria                                          | [response]                        |
| Domain model and architecture                                                     | [response]                        |
| Design trade-off                                                                  | [response]                        |
| Meaningful test and its limits / 100 percent coverage                             | [response]                        |
| Diagnosed defect and verification                                                 | [response]                        |
| Shared store and session-state/query responsibilities                             | [response]                        |
| What would break if session-state lookup/query responsibilities changed?          | [response]                        |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response]                        |
| FR-07 retained history test                                                       | [response]                        |
| Actual AI change rejected/modified or honestly accepted with verification         | [response]                        |
| Unresolved limitation / future production work                                    | [response]                        |
| Personal implementation contribution                                              | [response]                        |
| Personal test/review/design/integration contribution                              | [response]                        |
| PG agentic change and rescheduling verification                                   | [response]                        |
| PG responsible-AI risk/remediation or supported no finding                        | [response]                        |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
