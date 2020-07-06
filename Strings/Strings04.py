"""
Write a program to check if the substring is present in a given string.
"""

word = input("Enter the string : ")
subword = input("Enter the substring : ")
result = word.find(subword) 
if (result != -1): 
    print ("Contains given substring ") 
else: 
    print ("Doesn't contains given substring") 

"""
Enter the string : seriously
Enter the substring : rio
Contains given substring 
"""
