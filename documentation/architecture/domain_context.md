# Domain Context Model

* Help capture domain knowledge by modeling concepts and associations among the concepts
* Software-independent model
* Models things/concepts that exist in the real-world problem domain

Guidelines on selecting concepts:

* Use the vocabulary or terminology of the domain
* Do not rename concepts and attributes (map makers do not rename cities in creating a map)
* Exclude irrelevant concepts
* Do not add anything not in the problem domain

Strategies to identify concepts and relationships:

* Noun based approach
	* Finding Concepts
		* Identify nouns (i.e., potential concepts) in stakeholder profiles and interview notes
		* Identify nouns in requirements documentation
		* Identify nouns in other textual descriptions of the problem domain
		* Filter out nouns that are:
			* Attributes or properties of a single other concept or object (in the real world)
			* Concepts that are clearly out of scope of the problem domain
	* Finding relationships
		* Find the linking words (verbs or verb phrases)
		* The linking words will help you decide on and label association lines between concepts
* Concept Checklist
	* Physical or tangible objects
	* Specifications or descriptions of things (e.g., ProductDescription)
	* Places
	* Transactions (e.g., sale, payment)
	* Transaction line items (e.g., SalesLineItem)
	* Roles of People (e.g., Cashier, Clerk, Guest)
	* Container of things (e.g., store, bin, airplane)
	* Things in a container (e.g., item, passenger)
	* Other systems
	* organizations
	* events (Sale, meeting, flight)
	* Catalogs
	* Records of finance, work, contracts, and legal matters
	* Financial instruments and services

## Diagram

* UML class diagram or SysML block diagram
* Use <<concept>> stereotype

Modeling Guidelines:

* Associations model relationships among concepts
	* Shown as connecting lines between concepts
	* Roles may be named, and may or may not have multiplicities specified
* Model may contain attributes, if they are significant, but they do not need to be typed
* Operations are NOT used (remember - modeling information in the domain, not class or component implementations)

## Concept Catalogue

* Capture concepts and identify relationships between them in the usage domain
