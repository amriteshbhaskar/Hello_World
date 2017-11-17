import re

s=r"My roll number is IIT2017088 and date of  AZ birth is 05/06/1998 and phone number is 8700783753 and 9999999999 and my email is tipra2614@gmail.com and my blood group is B+"

match_roll=r"((I|L)IT)(\d{7})"

match_dob=r"\d{2}(-|/)\d{2}(-|/)\d{2,4}"

match_number=r"\s\d{10}\s"

match_email=r"([\w\.]+)@([\w\.]+)(\.[\w\.]+)"

match_bg=r"\w{1,2}(\+|-)"

match_two=r"\W([a-z]{2}|[A-Z]{2})\W"

roll_check=re.search(match_roll,s)
if roll_check:
	print("Roll number-",roll_check.group())


dob_check=re.search(match_dob,s)
if dob_check:
	print("Date of Birth-",dob_check.group())

print(re.findall(match_number,s))


email_check=re.search(match_email,s)
if email_check:
	print("Email-",email_check.group())

bg_check=re.search(match_bg,s)
if bg_check:
	print("Blood Group- ",bg_check.group())



print(re.findall(match_two,s))





