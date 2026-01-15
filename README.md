Outdated

A Python program that converts dates entered in different formats into a standardized YYYY-MM-DD format.

This project is part of CS50’s Introduction to Programming with Python and focuses on parsing user input, validating data, and handling errors gracefully.

What It Does

The program prompts the user for a date and accepts two formats:

MM/DD/YYYY (e.g. 9/8/1636)

Month Day, Year (e.g. September 8, 1636)

If the input is valid, the program outputs the date in ISO format:

YYYY-MM-DD


Invalid input is rejected, and the user is re-prompted until a valid date is entered.

Concepts Used

String manipulation and parsing

Lists and indexing

Input validation

Loops (while True)

Exception handling (try / except)

Formatted string output

How to Run
python outdated.py


Then enter a date when prompted.

Example

Input:

September 8, 1636


Output:

1636-09-08

Notes

This program demonstrates defensive programming techniques to ensure incorrect input does not crash the application.
