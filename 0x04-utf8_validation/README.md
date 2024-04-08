# 0x04-utf8_validation

## Description
This is the repository for the ALX School project 0x04-utf8_validation.
This project is about writing a method that determines if a given data set represents a valid UTF-8 encoding.
The method should return 1 if the data set is a valid UTF-8 encoding, and 0 if it is not.

## challenge
Write a method that determines if a given data set represents a valid UTF-8 encoding.
- Prototype: def validUTF8(data)
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
