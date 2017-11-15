import re

s=r"My roll number is IIT2017088 and date of birth is 05/06/1998 and phone number is 8700783753 and my email is tipra2614@gmail.com and my blood group is AB-"

match_roll=r"(IIT)(\d{7})"

match_dob=r"\d{2}(-|/)\d{2}(-|/)\d{2,4}"

match_number=r"\s\d{10}\s"

match_email=r"([\w\.]+)@([\w\.]+)(\.[\w\.]+)"

match_bg=r"\w{1,2}(\+|-)"

roll_check=re.search(match_roll,s)
if roll_check:
	print("Roll number-",roll_check.group())


dob_check=re.search(match_dob,s)
if dob_check:
	print("Date of Birth-",dob_check.group())

phone_check=re.search(match_number,s)
if phone_check:
	print("Phone number-  ",phone_check.group())

email_check=re.search(match_email,s)
if email_check:
	print("Email-",email_check.group())

bg_check=re.search(match_bg,s)
if bg_check:
	print("Blood Group- ",bg_check.group())





