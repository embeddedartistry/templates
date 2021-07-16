# System Overview

Describe the system, why it's built, etc.

**Table of Contents:**
1. [Motivation](system_overview.md#motivation)
2. [Scope Summary](system_overview.md#scope-summary)
3. [Functionality](system_overview.md#functionality)
	1. [Key Capabilities](system_overview.md#key-capabilities)
	2. [High-level Use Cases](system_overview.md#high-level-use-cases)
4. [Architectural Challenges](system_overview.md#architectural-challenges)
5. [Quality Attribute Requirements](system_overview.md#quality-attribute-requirements)
	1. [Key Quality Attribute Scenarios](system_overview.md#key-quality-attribute-scenarios)

## Motivation

* Include the background information or motivation for designing this product

## Scope Summary

* Create a short description (1 page) of the purpose of the architecture and fundamental system capabilities
* Create a rich picture or informal diagram of the system and its relationships to other systems
* Record capabilities ruled out of scope, and provide rationale for doing so

## Functionality

* What functionality does the system provide?

### Key Capabilities

* Include key capabilities as a summary. Review/revise periodically.

### High-level Use Cases

* What are basic use cases? (link for futher info)
* Include high-level use case diagram

<center>

| ![High-level framework use cases](images/HighLevelUseCases.jpg) |
|:--:|
| *Figure 1. View of high-level use cases for the embedded framework.* |

</center>

## Architectural Challenges

## Quality Attribute Requirements

* What are the important quality attributes?

### Key Quality Attribute Scenarios

* What are the most important Quality Attribute Scenarios (QAS)?

The quality attribute scenarios (QAS) are listed below, separated by quality attribute.

Example:

```
Modifiability
* QAS1. A new business partner (airline, lodging, or activity provider) that uses its own web services interface is added to the system in no more than 10 person-days of effort for the implementation. The business goal is easy integration with new business partners.
Performance
* QAS2. A user places an order for an adventure travel package to the Consumer Web site. The user is notified on screen that the order has been successfully submitted and is being processed in less than five seconds.
* QAS3. Up to 500 users click to see the catalog of adventure packages following a random distribution over 1 minute; the system is under normal operating conditions; the maximal latency to serve the first page of content is under 5 seconds; average latency for same is less than 2 seconds.
Reliability
* QAS4. The Consumer Web site sent a purchase order request to the order processing center (OPC). The OPC processed that request but didn’t reply to Consumer Web site within five seconds, so the Consumer Web site resends the request to the OPC. The OPC receives the duplicate request, but the consumer is not double-charged, data remains in a consistent state, and the Consumer Web site is notified that the original request was successful in one hundred percent of the times.
Security
* QAS5. Credit approval and payment processing are requested for a new order. In one hundred percent of the cases, the transaction is completed securely and cannot be repudiated by either party. The business goals are to provide customers and business partners confidence in security and to meet contractual, legal, and regulatory obligations for secure credit transactions.
* QAS6. The OPC experiences a flood of calls through the Web Service Broker endpoint that do not correspond to any current orders. In one hundred percent of the times, the system detects the abnormal level of activity, notifies the system administrator, and continues to service requests in a degraded mode.
Availability
* QAS7. The Consumer Web site is available to the user 24x7. If an instance of OPC application fails, the fault is detected and the system administrator is notified in 30 seconds; the system continues taking order requests; another OPC instance is created; and data remains in consistent state.
```
