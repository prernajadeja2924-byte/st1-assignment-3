# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: [response]
- Members, GitHub usernames and cohorts: [response]
- Repository URL: [response]
- Starting SHA: [response]

## A Requirement to issue activities

### FR-02 Patient Search

- Title:  Implement patient lookup by ID (FR-02)
- Context: SmartCare requires a service operation to retrieve an existing registered patient using their patient ID.
- Requirement: FR-02 – Find a patient by patient ID.
- Acceptance criteria: A valid registered ID returns the existing patient object; an unknown ID raises LookupError; a blank or invalid ID raises ValueError; stored patient records remain unchanged.
- Scope: Implement PatientService.find_patient() in project/smartcare/services.py and relevant automated tests in project/tests/test_services.py.

- Definition of Done:  Implementation completed, tests passing, code committed, and required review completed before merging.
- Owner: Prerna Jadeja
- Actual issue link:https://github.com/prernajadeja2924-byte/st1-assignment-3/issues/1

### FR-06 Appointment Cancellation with FR-07 retained history

- Title:  Implement appointment cancellation and retain history
- Context: SmartCare must support cancellation of scheduled appointments while preserving their records.
- Requirement:  FR-06 – Appointment cancellation; FR-07 – Retained appointment history.
- Acceptance criteria: Scheduled appointments can be cancelled; unknown IDs raise LookupError; invalid IDs and illegal status transitions raise ValueError; cancelled appointments remain stored.
- Scope: Implement AppointmentService.cancel_appointment() and five automated cancellation tests.
- Definition of Done: Implementation and automated tests completed; review and merge evidence remain pending.
- Owner: Prerna Jadeja
- Actual issue link: Pending verification or creation.

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|---|---|
| changes | Weak | 

Does not explain what was changed. |
| final version | Weak | 

Does not identify the feature or purpose.|
| Add patient search by ID | Strong | Clearly identifies the functionality implemented |
| fix stuff | Weak | Too vague to explain the correction. |
| Prevent cancellation of completed appointments | Strong | 

Describes a specific business rule being enforced. |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns:The pull request includes unrelated changes that increase complexity and make review difficult.
- Responsibility and architecture concerns: Renaming unrelated patient fields and restructuring other components may affect existing interfaces and responsibilities.
- Testing and review concerns: Unrelated changes increase regression risk and require additional testing beyond appointment cancellation.
- Changes to remove or separate, with reasons:  Keep cancellation functionality and its tests in the cancellation PR. Move unrelated refactoring, field renaming, and dependency changes into separate issues and pull requests.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: The statement "Looks good, tests pass" does not demonstrate that the requirements, code changes, edge cases, and test results were independently checked.
- Follow-up review question 1: Does cancellation reject unknown appointment IDs?
- Follow-up review question 2: Are completed or already cancelled appointments protected against invalid cancellation?
- Follow-up review question 3: Does the cancelled appointment remain available in stored history?
- Follow-up review question 4: Were all original starter tests preserved and executed?
- Follow-up review question 5: Does the pull request contain only changes relevant to its linked requirement?


- Additional questions if useful: Are exception types consistent with the acceptance criteria, and is there sufficient evidence of test execution?

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | 

Use descriptive feature branches such as feature/patient-lookup, feature/practitioner-lookup and feature/appointment-cancellation. |
| Commit message convention |

Use short, descriptive messages identifying the functionality implemented or corrected. |
| PR size | Keep pull requests focused on one requirement or related feature. |
| Another-member review requirement | Pending. Currently working individually and awaiting tutor guidance on group allocation or individual submission. |
| Merge rule | Merge only after tests pass and the required independent review and approval have been completed. |
| Significant Copilot disclosure rule |

Record meaningful Copilot interactions, including the purpose, suggestions, human verification, and decisions. No Copilot review has been recorded yet |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| [issue 1] | (https://github.com/prernajadeja2924-byte/st1-assignment-3/issues/1) | FR-02 Patient Search |  Prerna Jadeja | Valid patient ID returns the existing patient; unknown ID raises LookupError; blank or invalid ID raises ValueError; stored records remain unchanged. | Implementation completed; 5 tests passed; review pending. |
| [issue 2] |Link pending verification | FR-06 Appointment Cancellation and FR-07 Retained History | Prerna Jadeja | Scheduled appointments can be cancelled; unknown IDs raise LookupError; invalid IDs and illegal transitions raise ValueError; cancelled appointments remain stored. | Implementation completed; 5 tests passed; issue and review pending verification. | | Practitioner lookup issue - Not yet created | Practitioner Lookup | Prerna Jadeja | Valid practitioner ID returns the existing practitioner; unknown ID raises LookupError; blank or invalid ID raises ValueError; stored records remain unchanged. | Implementation completed; 5 tests passed; issue and review pending. |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

###Pull Request 1 – Patient Lookup (FR-02)

-PR link: https://github.com/prernajadeja2924-byte/st1-assignment-3/pull/3
- PR title: Implement patient lookup and tests for issue #1
- Linked issue: https://github.com/prernajadeja2924-byte/st1-assignment-3/issues/1
- Branch: feature/patient-lookup
- Commit: 56697e2
- Implementation: Implemented PatientService.find_patient() to retrieve registered patients by ID.
- Testing: Added five automated tests covering successful lookup, object identity, unknown IDs, invalid IDs and preservation of stored records.
- Test command: python -m pytest
- Working directory: project
- Test result: 13 tests passed at the patient lookup stage.
- Human reviewer: Not yet assigned.
- Review status: Awaiting independent review.
- Merge status: PR #3 is open and has not been merged into main.

###Pull Request 2 – Practitioner Lookup

-PR title: Implement practitioner lookup
PR link: https://github.com/prernajadeja2924-byte/st1-assignment-3/pull/4
Branch: feature/practitioner-lookup

Commit: 54eea3e

Implementation: Implemented PractitionerService.find_practitioner() to retrieve registered practitioners by ID.

Testing: Added five automated tests covering successful lookup, object identity, unknown IDs, blank IDs and preservation of existing records.

Test result: 18 tests passed at the practitioner lookup stage.

Test command: python -m pytest

Working directory: project

Human reviewer: Not yet assigned.

Review status: Awaiting independent human review.

PR creation:  Confirmed. Pull Request #4 created.

Merge status: Not merged into main.

###Pull Request 3 – Appointment Cancellation (FR-06 and FR-07)

PR title: Implement appointment cancellation and tests for issue #2

PR link: https://github.com/prernajadeja2924-byte/st1-assignment-3/pull/5

Related issue: Issue #2 – (https://github.com/prernajadeja2924-byte/st1-assignment-3/issues/2)

Branch: feature/appointment-cancellation

Commit: 0f79ea2

Implementation: Implemented AppointmentService.cancel_appointment() using the existing appointment domain cancellation method.

Testing: Added five automated tests covering successful cancellation, retained history, unknown IDs, invalid IDs and repeated cancellation.

Test result: 23 tests passed across the complete test suite.

Test command: python -m pytest

Working directory: project

Human reviewer: Awaiting independent human review.

Review status: Pending.

PR creation: Confirmed. Pull Request #5 created.

Merge status: Not merged into main.

Review and integration summary

The three service implementations and their automated tests have been completed and pushed to GitHub feature branches.

The full test suite passed with 23 tests. However, independent human review and approval have not been completed because the assignment is currently being undertaken individually.

Tutor guidance is required regarding group allocation and the peer-review requirement.

No unperformed review, approval or merge is claimed as completed.

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

Member and task: Prerna Jadeja – Reviewing and verifying the completed SmartCare Stage 6 implementation, including patient lookup, practitioner lookup and appointment cancellation.

Prompt/purpose and relevant issue/diff: GitHub Copilot was asked to review the completed Python service methods and automated tests against the SmartCare requirements. The purpose was to double-check code correctness, input validation, exception handling, appointment cancellation rules and test coverage. The relevant requirements were FR-02 Patient Search, FR-06 Appointment Cancellation and FR-07 Retained History.

Summary of output: Copilot provided feedback on the completed implementation, highlighting the importance of validating patient and practitioner IDs, handling unknown records correctly, preventing invalid appointment cancellation transitions and maintaining appropriate automated test coverage.

Human check against actual code, requirements and tests: The implementation was completed before requesting AI feedback. Copilot's observations were compared with the existing service methods, domain rules and assignment requirements. Automated tests were executed using python -m pytest, with 23 tests passing.

Decision – Accept / Modify / Reject: Accept and Modify.

Reason: Relevant feedback was accepted where it matched the assignment requirements and existing implementation. Suggestions were evaluated independently rather than automatically applied. The code was retained or modified only where justified by the requirements and test results.

Verification/evidence:

Patient lookup commit: 56697e2

Practitioner lookup commit: 54eea3e

Appointment cancellation commit: 0f79ea2

Test command: python -m pytest

Working directory: project

Observed result: 23 tests passed.

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: I reviewed the completed patient lookup, practitioner lookup and appointment cancellation implementations. I checked that valid IDs returned the correct records, invalid IDs produced appropriate errors and cancelled appointments remained in the system. I also ran the automated tests to verify the expected behaviour.

Copilot noticed: GitHub Copilot reviewed the completed implementation and highlighted the importance of input validation, exception handling and testing appointment cancellation transitions.

Overlap: Both reviews focused on correct functionality, handling invalid inputs, preserving existing records and ensuring the automated tests covered the main requirements.

What did the human reviewer notice that Copilot did not: The human review considered the assignment's specific functional requirements and whether the completed work matched the SmartCare project expectations.

What did Copilot identify that the human reviewer initially missed: Copilot suggested checking whether an already-cancelled appointment could be cancelled again and whether this behaviour was covered by an automated test.

Unsupported or incorrect Copilot suggestion: None identified during the review. Any suggestions would need to be verified against the actual project requirements before acceptance.

Human judgement accepted, modified or rejected, and why: The suggestions relating to validation and cancellation testing were accepted where they matched the existing requirements. The final judgement was based on the actual implementation and automated test results rather than Copilot's feedback alone.

Which evidence justified merge approval: The completed implementations, relevant Git commits and successful execution of python -m pytest, with 23 tests passing, provided technical evidence supporting the changes. Formal merge approval would additionally require a documented review by another group member.

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: Prerna Jadeja
- Implementation: Implemented PatientService.find_patient(), PractitionerService.find_practitioner() and AppointmentService.cancel_appointment() in the SmartCare project.
- Testing: Added 15 automated tests covering successful operations, invalid inputs, unknown records, object identity, retained appointment history and invalid cancellation transitions. Confirmed that all 23 tests passed using python -m pytest.
- Review: 
Independently checked the implementation and test results. Review by another group member has not yet been completed or confirmed.
- Issue refinement: Created GitHub Issue #1 for patient lookup (FR-02), including the requirement, acceptance criteria and expected behaviour. Identified the remaining appointment cancellation and practitioner lookup work.
- Design and responsibility discussion: 
Considered how the new service methods should work with the existing data store and domain classes, including preserving records and using the existing appointment cancellation rules
- Debugging or integration: Resolved test setup issues involving appointment date and time validation. Checked the completed implementation using the full automated test suite.
- Documentation or team support: Prepared Stage 6 evidence, recorded GitHub commits and test results, and documented the use of AI for post-implementation verification.

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

A high commit count does not necessarily indicate a strong individual contribution because the number of commits does not reflect the quality, complexity or importance of the work completed.

A developer may make many small commits containing minor changes, while another developer may make fewer commits that include significant functionality, comprehensive testing or important bug fixes.

Individual contributions should be evaluated based on the quality of implementation, understanding of requirements, meaningful code changes, testing, debugging, code reviews and collaboration.

In the SmartCare Stage 6 project, meaningful contribution is better demonstrated through the completed service methods, automated tests, GitHub evidence and successful test results rather than commit count alone.

## L Stage 6 formative questions

1. What is version control?

Version control is a system used to track and manage changes made to project files over time. It allows developers to maintain a history of modifications, restore previous versions and collaborate without losing important work. In the SmartCare project, Git was used to track changes to the Python implementation and automated tests.

2. Why is a feature branch useful?

A feature branch allows developers to work on a specific function or improvement without directly changing the main branch. This makes it easier to develop, test and review changes before merging them into the main project. In SmartCare, separate feature branches were used for patient lookup, practitioner lookup and appointment cancellation.

3. What makes a commit a good engineering commit?

A good engineering commit contains a focused, meaningful change and has a clear message explaining what was modified. It should be small enough to understand and review, relate to a specific requirement or issue, and avoid unrelated changes. Where appropriate, it should include tests that verify the new functionality.

4. What is a pull request?

A pull request is a request to merge changes from one branch into another, usually the main branch. It allows developers to review the code differences, discuss possible improvements, examine test results and approve changes before integration.

5. What is the purpose of code review?

The purpose of code review is to improve software quality by identifying errors, checking compliance with requirements and ensuring that the code is understandable and maintainable. It also encourages knowledge sharing and helps developers identify problems that automated tests might not detect.

6. What does a Git diff show?

A Git diff shows the differences between versions of files, commits or branches. It highlights lines that have been added, removed or modified. Developers use Git diffs to understand changes and evaluate whether they are relevant, correct and appropriately scoped.

7. What is a Definition of Done?

A Definition of Done is a set of conditions that must be satisfied before a task can be considered complete. It may include implementing the required functionality, meeting acceptance criteria, passing automated tests, updating documentation and completing code review. It helps ensure that work is completed to an agreed quality standard.

8. What is the appropriate role of GitHub Copilot in pull-request review?

GitHub Copilot can assist with reviewing pull requests by suggesting possible improvements, identifying potential bugs and highlighting missing test cases. However, its suggestions must be checked against the actual code, requirements and test results. Copilot should support human reviewers rather than replace their judgement or approval.

9. Why should individual contribution not be judged only by commit count?

Commit count does not necessarily represent the quality or significance of a developer's contribution. Some developers make many small commits, while others make fewer commits containing substantial functionality or important fixes. Contributions should also be evaluated through implementation quality, testing, debugging, code review, documentation and collaboration.

10. What is the Stage 6 engineering rule?

The key engineering principle demonstrated in Stage 6 is that software changes should be focused, traceable, tested and reviewed before integration. Each change should relate to a clear requirement, have supporting evidence and be checked through appropriate testing and human review. Passing tests alone does not replace the need for a meaningful code review.

## M Completion and handover

Starting SHA: b5d399535ae860f32be1b3ec6e80585ac2ac0ed0

Final Stage 6 code SHA: 0f79ea2bcc3ae5c9e00ad3b22011c546f44dd026

Test command: python -m pytest

Working directory: project

Observed result: 23 tests passed, including the original 8 supplied tests and 15 additional tests covering patient lookup, practitioner lookup and appointment cancellation.

PR and another-member reviewer: Feature branches have been pushed to GitHub. Pull-request creation and review links require verification. An independent reviewer has not yet been confirmed.

Unresolved issue or none: Independent peer review, GitHub Copilot comparison, pull-request approval and merging into the main branch remain unresolved. Tutor guidance is required regarding the group-review requirement because the work has been undertaken individually.

Stage 7 handover status: Unresolved work. All three Stage 6 service implementations and their automated tests are complete, but review and integration requirements remain outstanding.

- Final submitted SHA if later than tested SHA: 3575ee0a78f3f0458b79c5cd1de6b7f1659f6904
- Evidence-only difference: This commit records the Stage 6 documentation updates after the original implementation commit. The full test suite was rerun successfully after the documentation commit, with 23 tests passing.

- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
