"""
Title: Swap Two Numbers Using a Temporary Variable
Author: Rushikesh Padaki
Date: 25 July 2025

Description:
This program reads two integers from the user, swaps their values using a temporary variable,
and displays the values before and after swapping.
- Demonstrates use of input(), variable assignment, and basic swapping logic.
- Useful for beginners learning variable manipulation and memory assignment in Python.

Algorithm:
1. Prompt the user to enter the first number and store it in variable x.
2. Prompt the user to enter the second number and store it in variable y.
3. Display the original values of x and y.
4. Create a temporary variable temp and assign it the value of x.
5. Assign the value of y to x.
6. Assign the value of temp to y.
7. Display the swapped values of x and y.

Time Complexity:
- O(1) — Swapping involves a fixed number of operations.

Space Complexity:
- O(1) — Uses one extra variable for temporary storage.

Sample Execution:

Case 1: Normal positive integers
Input:
Enter first number: 10
Enter second number: 20
Output:
Numbers before swapping:
x =  10
y =  20
Numbers after swapping:
x =  20
y =  10

Case 2: One positive and one negative number
Input:
Enter first number: -5
Enter second number: 15
Output:
Numbers before swapping:
x =  -5
y =  15
Numbers after swapping:
x =  15
y =  -5

Case 3: Both numbers are zero
Input:
Enter first number: 0
Enter second number: 0
Output:
Numbers before swapping:
x =  0
y =  0
Numbers after swapping:
x =  0
y =  0
"""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Numbers before swapping:")
print("x = ", x)
print("y = ", y)

temp = x
x = y
y = temp

print("Numbers after swapping:")
print("x = ", x)
print("y = ", y)
