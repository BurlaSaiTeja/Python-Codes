"""
Use python set to check if string is panagram, i.e., a sentence that uses every letter in the alphabet.
"""

import string
def pangram(str): 
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabets: 
        if i not in str.lower(): 
            return False
    return True
s = input("Enter the string : ")
if(pangram(s) == True): 
    print("Yes it is Pangram!!!") 
else: 
    print("No it is not Pangram!!!")
    
"""
Output:
Enter the string : Sixty zippers were quickly picked from the woven jute bag
Yes it is Pangram!!!
"""
