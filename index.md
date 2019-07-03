## Knapsack Solution for Cash Withdrawal Problem of ATM

Most ATMs today on cash depletion displays messages such as "Unable to dispense cash" or "Enter in multiples of 500 2000". Our project solves this problem by recalculating the amount that can be dispensed against that entered by the bank customer.

### Problem

- When there is cash depletion in the ATM, the ATM is unable to dispense cash.
- Cash depletion occurs due 2 conditions:
  1. Insufficient funds
  2. Insufficient denominations
  
**Insufficient Funds**
This situation occurs if the amount entered by the customer is greater than what is present in the ATMs.
For e.g, if the ATM has only 35,000 left in it and the customer requests for 39,000.

**Insufficient Denominations**
It is when the denominations are not available to meet the customer requested amount. 
For e.g, if the ATM has only 500 notes and the customer requests 800 then the ATM is unable to dispense the amount due to the unavailability of the required denominations.

### Solution
To solve the above mentioned problem, we have developed a Python program that is able to recalculate the amount to be withdrawn and dispenses the same if the customer wants to continue the transaction with the newly calculated withdrawal amount.

This was done using the **knapsack algorithm** with the greedy approach. The condition for this algorithm is that the amount calculated should be less than the customer entered amount.
