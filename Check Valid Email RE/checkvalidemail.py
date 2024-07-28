#a-z aouncheema@gmail.com
#0-9
# . _ time 1
# @ time 1
# . 2,3 last

import re

# Define the email validation pattern
email_condition = r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

# Prompt the user to enter their email
user_email = input("Enter Your Email: ")

# Check if the entered email matches the pattern
if re.search(email_condition, user_email):
    print("Valid Email")
else:
    print("Invalid Email")
