"""
Write a python program to count the number of vowels and consonants in a file.
"""

import re

with open("test.txt", "w") as file:
    file.write("This is the story of our lifes in quarantine!!!")

with open("test.txt", "r") as file:
    f = file.read()
    total=len(re.findall("[A-Za-z]", f))
    vowels = len(re.findall("[aeiouAEIOU]", f))
    print("Vowels: ", vowels)
    print("Consonant: ", total-vowels)
    
"""
Output:
Vowels:  15
Consonant:  21
"""
