"""
Write a program to check the validity of password read by users.  The following criteria should be used to check for validity.
Password should have at least
i) One lowercase letter
ii)One Digit
iii) One uppercase letter
iv) One special character from[$#@!] 
v)length of six characters
Your program should accept a password and check the validity using the above criteria and print "valid" or "invalid" as the case may be.
"""

import re
p = input("Input your password : ")
i = True
while i:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@!]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password!!!")
        i=False
        break
if i:
    print("Invalid Password")
    
"""
Output:
Input your password : Teja@19#2000
Valid Password!!!
"""
