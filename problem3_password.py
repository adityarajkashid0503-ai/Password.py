import re

# At least 8 chars, 1 uppercase, 1 digit, 1 special character
pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!]).{8,}$"

passwords = ["Python@123", "python123"]

for p in passwords:
    if re.match(pattern, p):
        print(p, "- Valid password")
    else:
        print(p, "- Invalid password")
