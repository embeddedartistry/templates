# Use Case: Template

* Name: Use case name (also replace template with name)
* Number: Optional reference number

**Table of Contents:**
1. [Description](use_case.md#description)
2. [Actors](use_case.md#actors)
3. [Preconditions](use_case.md#preconditions)
4. [Postconditions](use_case.md#postconditions)
5. [Assumptions](use_case.md#assumptions)
6. [Steps](use_case.md#steps)
7. [Variations](use_case.md#variations)
8. [Non-functionals](use_case.md#non-functionals)
9. [Business Rules](use_case.md#business-rules)
10. [Architectural Mechanisms](use_case.md#architectural-mechanisms)
11. [Issues](use_case.md#issues)
12. [Related Use Cases](use_case.md#related-use-cases)

## Description

* Goal to be achieved by use case and sources for requirement

## Actors

* List of actors involved in use case

## Preconditions

* Conditions that must be true when the use case is initiated

## Post-conditions

* State of the system when the use case terminates

## Assumptions

* Optional entry
* Use if the use case depends on any other assumptions (than pre/post conditions)
* E.g.: assumptions about resources, about the environment

## Steps

* Interactions between actors and system that are necessary to achieve goal
* This section represents the "happy case" i.e., default actions
* A step completes when all its component interactions have completed.
* Steps are in the form:
	* <sequence number> <interaction>
* If there are multiple steps, then each step must have an integer sequence number showing its position in the list of steps.
* Steps are initiated in order, in accordance with their sequence number.
* The default assumption is that each step is completed before the next is started
* Steps may be represented visually in UML activity or sequence diagrams

1. interaction a
2. interaction b

## Variations

* Any variations in the steps of a use case
* Capture all alternative paths here
* Capture all exceptions here (e.g., error cases)
* The alternative paths make use of the numbering of the primary steps to show at which point they differ from the basic scenario, and if appropriate, where they rejoin. Don't repeat information unnecessarily.

1. The system recognizes cookie on user's machine.
2. Go to step 4 (main path)

Or:

1. The system does not recognize the user's login information
2. Go to step 1 (main path)

## Non-functionals

* List any non-functional requirements that the use case must meet
* Link to relevant qualities, constraints, and principles

## Business Rules

* Optional entry
* If the business rule applies to multiple use cases, you can add a use case name field to the business rules catalogue

## Architectural Mechanisms

* What architectural mechanisms are associated with the use case?

## Issues

* List of issues that remain to be solved

## Related Use Cases

* Link to any related use cases
