# CRC-R: Template

**Component Responsibility Card (CRC-R) Template**

What is a component?

* In general: a module in modular systems
* More precise definition for component that is part of a component-based arch:
	* A component is a self-contained, usually concurrent, object with a well-defined interface, capable of being used in different applications from that for which it was originally designed.
	* In distributed applications, a component is a basic unit of deployment and distribution.

To fully specify a component, it is necessary to define it in terms of the operations it provides and the operations it requires. Such a definition is in contrast to traditional OO approaches, which only describe provided operations.

First-pass component and responsibility generation:

* Work with components and responsibilities in both directions - start with a first cut notion of the components the system will need. Identify and allocate responsibilities to them.
* Start with responsibilities evident from how the system should act. Then factor to find components.

**Table of Contents:**

1. [Responsibilities](component.md#responsibilities)
2. [Requirements](component.md#requirements)
3. [Collaborators](component.md#collaborators)
4. [Rationale](component.md#rationale)
5. [Source Links](component.md#source-links)
6. [Related Documents](component.md#related-documents)
7. [Notes](component.md#notes)

## Responsibilities

* What are the responsibilities of this component?

These lists of responsibilities are a powerful and largely overlooked/underused tool in the architect's tool belt. If the responsibilities don't cohere within an overarching responsibility/purpose, that should trip the architect's boundary bleed detectors. We may need to refactor responsibilities, and discover new components in the process.

Continue to update the responsibilities for each component, as more is learned as the system is explored and built out.

## Requirements

What other APIs or features does this component require?

## Collaborators

* What other components does it work with?

## Rationale

* Why this component split this way?
* Why these collaborators?
* Why these responsibilities?

## Source Links

* Where in the code base is this component defined?
* Any notable usage examples?

## Related Documents

* What other documents are related to this component?
	* Interfaces
	* Use cases
	* User stories
	* Images

## Notes

Any open questions, issues, or related information?
