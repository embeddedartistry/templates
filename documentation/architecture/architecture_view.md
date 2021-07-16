# Architecture View: Template

* Briefly describe the architecture view here. Rename "Template" above to give it a name.

**Table of Contents:**

1. [Primary Presentation](architecture_view.md#primary-presentation)
2. [Context Diagram](architecture_view.md#context-diagram)
3. [Element Catalog](architecture_view.md#element-catalog)
4. [Variability Guide](architecture_view.md#variability-guide)
5. [Rationale](architecture_view.md#rationale)
6. [Related Views](architecture_view.md#related-views)

## Primary Presentation

* Add here the diagram (or non-graphical representation) that shows the elements and relations in this view
* Indicate the language or notation being used
* If it's not a standard notation such as UML, add a notation key

<center>

| ![XX View of the System](XXView.jpg) |
|:--:|
| *Figure 1. X View for Y.* |

</center>

## Context Diagram

* Add here a context diagram that graphically shows the scope of the part of the system represented by this view
* A context diagram typically shows the part of the system as a single, distinguished box in the middle surrounded by other boxes that are the external entities
* Lines show the relations between the part of the system and the external entities

<center>

| ![Context for the Y](Context.jpg) |
|:--:|
| *Figure 3. Software System Context Diagram for Z* |

</center>

## Element Catalog

* This section can be organized as a dictionary where each entry is an element of the Primary Presentation
* For each element, provide additional information and properties that the readers would need that would not fit in the Primary Presentation
* Optionally, you can add interface specifications and behavior diagrams (e.g., UML sequence diagrams, statecharts)

## Variability Guide

* Describe here any variability mechanisms used in the portion of the system shown in this view, along with how and when (build time, deploy time, run time) those mechanisms may be exercised
* Examples of variability include:
	* optional components (e.g., plug-ins, add-ons)
	* configurable replication of components and connectors
	selection among different implementations of an element or different vendors
	parameterized values set in build flags, .properties files, .ini files, or other config files

## Rationale

* Describe here the rationale for any significant design decisions whose scope is limited to this view
* Also describe any significant rejected alternatives
* This section may also indicate assumptions, constraints, results of analysis and experiments, and architecturally significant requirements that affect the view

## Related Views

* Add here links to the parent view and to any children (i.e., refined) views, if they exist.
