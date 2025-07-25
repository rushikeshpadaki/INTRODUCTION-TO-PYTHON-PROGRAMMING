"""
Title: Addition of Two User-Input Floating-Point Numbers
Author: Rushikesh Padaki
Date: 25 July 2025

Description:
This program reads two numbers from the user as input, converts them to floating-point numbers,
adds them, and prints the formatted result.
- Demonstrates how to read input using input().
- Shows how to perform type conversion from string to float.
- Uses the format() function to print output in a user-friendly message.

Algorithm:
1. Prompt the user to enter the first number and store it in variable num1.
2. Prompt the user to enter the second number and store it in variable num2.
3. Convert both num1 and num2 from string to float.
4. Compute the sum and store it in the variable total.
5. Use string formatting to print the result in a readable message.

Time Complexity:
- O(1) — Constant time for two input reads, conversion, addition, and printing.

Space Complexity:
- O(1) — Constant space used for three variables.

Sample Execution:

Case 1: Normal float inputs
Input:
Enter first number: 4.5
Enter second number: 3.2
Output:
The sum of 4.5 and 3.2 is 7.7

Case 2: Integer inputs (implicitly converted to float)
Input:
Enter first number: 5
Enter second number: 8
Output:
The sum of 5 and 8 is 13.0

Case 3: Negative values
Input:
Enter first number: -2.5
Enter second number: 4.0
Output:
The sum of -2.5 and 4.0 is 1.5

Case 4: Invalid input (non-numeric)
Input:
Enter first number: abc
Enter second number: 2.0
Output:
ValueError: could not convert string to float: 'abc'
(Note: This scenario results in a runtime error unless handled using try-except.)
"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

total = float(num1) + float(num2)

print("The sum of {0} and {1} is {2}".format(num1, num2, total))
