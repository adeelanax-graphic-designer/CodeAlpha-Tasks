"""
Task 3: Task Automation with Python Scripts
Objective:
Extract all email addresses from a text file and save them into another file.

Author: Adeela Naz
"""

import re
import os

def extract_emails(input_file, output_file):
    """
    Extracts email addresses from a text file
    and writes them to a new file.
    """

    # Check if input file exists
    if not os.path.exists(input_file):
        print(" Error: Input file does not exist.")
        return

    # Read content from input file
    with open(input_file, "r") as file:
        content = file.read()

    # Regular expression pattern for email extraction
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find all email addresses
    emails = re.findall(email_pattern, content)

    # Remove duplicate emails
    unique_emails = sorted(set(emails))

    # Write extracted emails to output file
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f" Success: {len(unique_emails)} emails extracted.")
    print(f" Output saved in '{output_file}'")


# Main execution
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "emails.txt"
    extract_emails(input_file, output_file)

