# Understanding the Problem
The problem at hand is to determine whether a given integer $𝑛$ is an "ugly number." In this context, an ugly number is defined as a positive number whose prime factors are limited to 2, 3, and 5. If  $𝑛$ is a positive integer and can be expressed as a product of these primes, then it is considered ugly. If  $𝑛$ contains any other prime factors, it is not ugly.

# Approach Taken
To solve this problem, the approach involves iterating over the prime factors 2, 3, and 5, and repeatedly dividing $𝑛$ by these primes if $𝑛$ is divisible by them. The steps are as follows:

1. **Initial Check**: If $𝑛$ is less than or equal to 0, return `False` because ugly numbers are positive integers.  
2. **Prime Factors Loop**: Initialize a list of the relevant prime factors: [2, 3, 5]. Use a counter to iterate through these primes.
    - As long as $𝑛$ is greater than or equal to 1, check if $𝑛$ is divisible by the current prime factor.
    - If $𝑛$  is divisible by the current prime factor, divide $𝑛$ by this factor and continue the process.
    - If $𝑛$ is not divisible by the current prime factor, move to the next prime factor by incrementing the counter.  
  3. **Final Check**: If the counter exceeds the length of the prime factors list, return `False` since it means $𝑛$ has a prime factor other than 2, 3, or 5. If the loop completes with $𝑛$ being 1, return `True`.

This approach ensures that the algorithm efficiently checks for the prime factors and accurately determines whether $𝑛$ is an ugly number, all while maintaining $𝑂(1)$ space complexity and $O(logn)$ time complexity due to repeated divisions