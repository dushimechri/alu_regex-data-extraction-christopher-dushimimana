Regex Data Extraction

Project Overview

This project utilizes Regular Expressions (Regex) in Python to extract structured data, including email addresses, URLs, phone numbers, credit card numbers, and time formats, from unstructured text.

Key Features

Extracts emails, URLs, phone numbers, credit card numbers, and time formats from text.
Implements Python's re module for regular expression matching.
Organized into separate, modular functions for each type of data extraction.
Structured as a Python package, making it easy to integrate into other projects.

How to Use

Sample Input Data

python
Copy
input_data = """ Contact us at support@example.com or visit our site https://www.example.com. 
Call (123) 456-7890 or 123-456-7890 for assistance. Your credit card 1234-5678-9012-3456 is charged $19.99. 
Meeting at 14:30 and another at 2:30 PM. """
Function Calls and Output

python
Copy
from Regex_Data_Extraction import extract_emails, extract_urls, extract_phone_numbers, extract_credit_cards, extract_time

print("Emails:", extract_emails(input_data))

print("URLs:", extract_urls(input_data))

print("Phone Numbers:", extract_phone_numbers(input_data))

print("Credit Cards:", extract_credit_cards(input_data))

print("Time Formats:", extract_time(input_data))
Expected Output

python
Copy
Emails: ['support@example.com']

URLs: ['https://www.example.com']

Phone Numbers: ['(123) 456-7890', '123-456-7890']

Credit Cards: ['1234-5678-9012-3456']

Time Formats: ['14:30', '2:30 PM']
