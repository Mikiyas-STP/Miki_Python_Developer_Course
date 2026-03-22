# Challenge A: The Email Sanitizer (List Comprehension)
# You have a list of user-submitted emails. Some are empty (None), some have extra spaces, and some are uppercase.
# code
# Python
# raw_emails = [" ALICE@gmail.com ", None, "bob@TEST.com", "  ", "CHARLIE@DEV.IO"]
# Task: Write a function clean_emails(emails: list) -> list that:
# Filters out any emails that are None or just empty whitespace strings. (Hint: .strip() on an empty string " " makes it "falsy").
# Returns a list where all remaining emails are lowercase and stripped of whitespace.

def clean_emails(emails: list) -> list:
    return [
        email.strip().lower()
        for email in emails
        if email and email.strip()
    ]

raw_emails = [" ALICE@gmail.com ", None, "bob@TEST.com", "  ", "CHARLIE@DEV.IO"]

print(clean_emails(raw_emails))