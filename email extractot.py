import re

text = """
Hello John,

Contact us at support@gmail.com
or admin@yahoo.com

Thank you.
"""

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Extracted Emails:")
for email in emails:
    print(email)

print("\nEmails saved to emails.txt")
