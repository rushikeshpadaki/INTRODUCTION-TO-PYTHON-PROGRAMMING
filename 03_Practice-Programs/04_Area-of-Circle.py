"""
Title: Area of a Circle
Author: Rushikesh Padaki
Date: 25 July 2025

Description:
This program calculates the area of a circle based on the radius entered by the user.
- It uses the mathematical formula: Area = π * r²
- Demonstrates input handling, type conversion, use of the math library, and formatted output.

Algorithm:
1. Import the math module to access the value of π (math.pi).
2. Prompt the user to enter the radius of the circle.
3. Convert the radius from string to float.
4. Use the formula: area = π * radius².
5. Print the result rounded to six decimal places using formatted string output.

Time Complexity:
- O(1) — All operations are done once and independently of input size.

Space Complexity:
- O(1) — Constant space for radius and area variables.

Sample Execution:

Case 1: Normal float input
Input:
Enter the radius of the circle (in cm): 3.0
Output:
Area of circle = 28.274334 sq.cm

Case 2: Integer input
Input:
Enter the radius of the circle (in cm): 5
Output:
Area of circle = 78.539816 sq.cm

Case 3: Zero as input
Input:
Enter the radius of the circle (in cm): 0
Output:
Area of circle = 0.000000 sq.cm

Case 4: Invalid (non-numeric) input
Input:
Enter the radius of the circle (in cm): abc
Output:
ValueError: could not convert string to float: 'abc'
(Note: To prevent this, exception handling is needed.)
"""

import math

radius = input("Enter the radius of the circle (in cm): ")

area = math.pi * float(radius) ** 2

print("Area of circle = %.6f sq.cm" % area)
