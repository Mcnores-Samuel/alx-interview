# 0x00-pascal_triangle

## Description

This project is about creating a function that returns a list of lists of integers representing the Pascal’s triangle of n.
The pascale triangle is a mathematical concept that is represented as a triangle of numbers where the first and last numbers of each row are 1 and each number in the triangle is the sum of the two numbers directly above it in the previous row.

## Challenge

- The challenge is to create a function that returns a list of lists of integers representing the Pascal’s triangle of n.
- he function should be able to handle edge cases such as when n is less than or equal to 0.
- The function should also be able to handle edge cases such as when n is equal to 1.

## Solution
The solution to this problem is to create a function that takes an integer n as an argument and returns a list of lists of integers representing the Pascal’s triangle of n. The function should be able to handle edge cases such as when n is less than or equal to 0 and when n is equal to 1. The function should also be able to handle edge cases such as when n is equal to 1.

The function should be able to generate the Pascal’s triangle of n by using a nested loop to iterate through the rows and columns of the triangle. The function should be able to calculate the value of each number in the triangle by using the formula C(n, k) = C(n-1, k-1) + C(n-1, k) where C(n, k) is the value of the number at row n and column k in the triangle.

The function should be able to return the Pascal’s triangle of n as a list of lists of integers where each list represents a row in the triangle and each integer in the list represents a number in the row.

The time complexity of this solution is O(n^2) where n is the number of rows in the Pascal’s triangle of n.

## Author
- Mcnores Samuel
