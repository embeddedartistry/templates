# Quality Requirement: Template

* Name: (Replace template above)
* Reference Number: Optional
* Parent: Optional, link to parent
* Children: Optional, link to child qualities (refined qualities)
* Category: Optional

**Table of Contents:**

1. [Description](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#description)
2. [Scenario](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#scenario)
3. [Test Cases](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#test-cases)
4. [Landing Zones](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#landing-zones)
5. [Context](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#context)
6. [Tradeoff Notes](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#tradeoff-notes)
7. [Related Qualities](0%20Embedded%20Artistry/1.%20Projects%20-%20Deferred/Courses/%5BPriority%5D%20Modern%20Documentation/doc-templates/architecture/quality.md#related-qualities)

## Description

* Statement of the requirement
* The quality requirement is stated as a general scenario
	* e.g., Modifiability: "must be able to support new hardware with minimal impact"
* The general scenario can apply to many systems, not just the one we are designing

Non-functional requirements are in the form of "system shall be <requirement>". A non-functional requirement is an overall property of the system as a whole or of a particular aspect. It is not a specific function. The system's overall properties commonly mark the difference between whether the development project has succeeded or failed.

## Scenario

* We refine the statement further with sub-quality-examples and scenarios
	* e.g.,, defining the types of hardware changes we want to make the architecture robust to
		* Adding new probes
		* Porting to new processor
* Scenario: <source of stimulus> <stimulus> <part of system> <observable response>
	* For each quality, define quality attribute scenarios and/or test cases
	* Describe the specific expected or anticipated demands ont he architecture during development/evolutiona nd run-time
* Example Scenario:
	* Input Stimulus: arrival rate of 1000-1500 requests/minute
	* Environment: 2-CPU app server and 5-10 lightweight queries
	* Expected result: Sustain > 20 electronic payments/second for 8 hrs

Make your qualities "SMART":

* Specific: without ambiguity, using consistent terminology, uncomplicated, and at the appropriate level of detail
* Measurable: is it possible to verify that this requirement has been met?
	* What tests must be performed or criteria met to verify meeting the requirement?
* Attainable: Technically feasible
* Realizable: realistic, given the resources
	* do you have the staffing?
	* With the necessary skillsets?
	* Do you have access to the infrastructure neede?
	* Do you have enough time?
* Traceable: linked from its conception through its specification to its subsequent design, implementation, and test

## Test Cases

* Provide clear, testable characterizations of the quality requirements
* One or more test cases to make the requirements clear
* Provide concrete cases to assess the architecture, design, and executing system against
* Quantify where reasonable

### Landing Zones

Key quality attributes are not always absolute. We can have targets:

| Quality | Measurement | Minimum | Target | Oustanding |
|---------|-------------|---------|--------|------------|
| Performance | throughput (txns/day) | 50,000 | 70,000 | 90,000 |
| Performance | avg txn time | 2s | 1s | < 1s |
| Data Quality | accuracy | 97% | 99% | > 99% |

## Context

* What context does this quality apply to?
* What is the environmental context or state of the system? (peak load, normal cases)

## Tradeoff Notes

* Provide indications of conflicting qualities where tradeoffs may have to be made
* E.g. modularity and encapsulation increase reusability but may decrease performance and increase communication/coordination

## Related Qualities

* What other qualities relate to this one?
* What other qualities does this quality depend on?
	* E.g. Reusability depends on weak coupling
	* Modifiability depends on modularization and encapsulation
