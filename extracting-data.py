#!/usr/bin/python3
import re

def extract_data(text):
    values = {
        "emails": r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}",
        "urls": r"https?://(?:www\.)?[\w.-]+(?:\.[a-zA-Z]{2,6})+(?:/\S*)?",
        "phone_numbers": r"(?:\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]\d{4}",
        "credit_cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
        "time_12h": r"\b(1[0-2]|0?[1-9]):([0-5][0-9])\s?(AM|PM)\b",
        "time_24h": r"\b([01]?[0-9]|2[0-3]):([0-5][0-9])\b",
        "html_tags": r"<([a-zA-Z]+)[^>]*>",
        "hashtags": r"#\w+",
        "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    }

    extracted_data = {key: re.findall(value, text) for key, value in values.items()}

    return extracted_data

test_text = """
    Contact us on Email: user@example.com or firstname.lastname@company.co.uk
    Visit our site: https://www.example.com/ or http://subdomain.example.org/page
    Phone numbers (various formats):(123) 456-7890 ,123-456-7890 ,123.456.7890
    Credit card numbers:1234 5678 9012 3456 ,1234-5678-9012-3456
    Time formats: 14:30 , 2:30 PM
    HTML tags: <p>Welcome!</p> <div class="example">Content</div>
    Hashtags: #example #ThisIsAHashtag
    Currency amounts: $19.99, $1,234.56
"""

data = extract_data(test_text)

for key, values in data.items():
    print(f"{key.capitalize()}:")
    for value in values:
        print(f"  - {value}")
