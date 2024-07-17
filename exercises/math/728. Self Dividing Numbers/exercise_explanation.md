# Understanding the Problem
The problem requires identifying all self-dividing numbers within a given range [left, right]. A self-dividing number is defined as a number that is divisible by each of its digits. For instance, the number 128 is self-dividing because it satisfies the conditions:

- `128 % 1 == 0`
- `128 % 2 == 0`
- `128 % 8 == 0`

Furthermore, a self-dividing number cannot contain the digit zero since division by zero is undefined.

Given two integers, `left` and `right`, the task is to return a list of all self-dividing numbers within the inclusive range from `left` to `right`.

# Approach Taken
To solve this problem efficiently, the approach involves iterating through each number in the given range and checking whether it qualifies as a self-dividing number using the following steps:

1. **Helper Function** `is_self_dividing`: A dedicated function is defined to determine if a number is self-dividing.  
    - **Extract Digits**: For a given number, extract each digit by using modulus and integer division.  
    - **Check Conditions**: Ensure that none of the digits are zero and that the original number is divisible by each digit.  
    - **Return Result**: If the number meets all the criteria, return True; otherwise, return False.  
2. **Iterate Through Range**: Loop through each number from `left` to `right` and apply the helper function to check if it is self-dividing.  
3. **Collect Results**: Append all numbers that satisfy the self-dividing condition to a result list.