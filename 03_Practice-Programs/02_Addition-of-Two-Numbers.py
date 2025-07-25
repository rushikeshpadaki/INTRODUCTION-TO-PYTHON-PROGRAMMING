"""
Title: Addition of Two Floating-Point Numbers
Author: Rushikesh Padaki
Date: 25 July 2025

Description:
This program adds two floating-point numbers and prints the result.
- Demonstrates basic arithmetic operations using Python.
- Emphasizes the use of float data types and the addition operator.

Algorithm:
1. Assign the first number (floating-point) to variable num1.
2. Assign the second number (floating-point) to variable num2.
3. Compute the sum of num1 and num2, and store it in the variable total.
4. Print the value of total.

Time Complexity:
- O(1) — Constant time operation as it involves a single arithmetic operation.

Space Complexity:
- O(1) — Uses only three variables to store float values.

Sample Execution:

Case 1: Standard input values
Input:
num1 = 1.5
num2 = 6.3
Output:
7.8

Case 2: Negative and positive values
Input:
num1 = -2.5
num2 = 3.1
Output:
0.6

Case 3: Both values are zero
Input:
num1 = 0.0
num2 = 0.0
Output:
0.0

Case 4: Very small decimal values
Input:
num1 = 0.0001
num2 = 0.0002
Output:
0.0003
"""

num1 = 1.5
num2 = 6.3

total = num1 + num2

print(total)