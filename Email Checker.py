"""
Using RegEx
STEP -1 
IMPORT A MODULE re
STEP -2
"""
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Your Email = ")

if re.search(email_condition,user_email):
    print("Your Email Is Correct....")
else:
    print("Your Email Is Wrong....")