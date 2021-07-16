# BDD Story: Business Driven Development (BDD) Story Template

* Category: Story | Epic
* Group: Optional Grouping Name (replace template above)
* Reference Number: Optional ID

## Story

* As an [x], where X is the person/role who benefits
* I want [y], where Y is some feature
* so that [Z], where Z is the benefit or value of the feature
* Given some initial context (the givens)
* When an event occurs
* Then ensure some outcomes

### Example

```
As an Account Holder
I want to withdraw cash from an ATM
So that I can get money when the bank is closed

Scenario 1: Account has sufficient funds
Given the account balance is $100
And the card is valid
And the machine contains enough money
When the account holder requests $20
Then the ATM should dispense $20
And the account balance should be $80
And the card should be returned

Scenario 2: Account has insufficient funds
Given the account balance is $10
And the card is valid
And the machine contains enough money
When the account holder requests $20
Then the ATM should dispense no money
Then the ATM should say there are insufficient funds
And the account balance should be $10
And the card should be returned

Scenario 3: Card has been disabled
Given the card is disabled
When the Account Holder requests $20
Then the ATM should retain the card
And the ATM should say the card has been retained

Scenario 4: The ATM has insufficient funds
...
```
