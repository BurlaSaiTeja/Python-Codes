"""
Write a program that reads a file and prints the letters with its frequency.
Your program should convert all the input to lower case and only count the letters a-z.
"""

import re
filename = input("Enter filename: ")
letters = dict()
with open(filename, "r") as file:
  for line in file:
    line = line.lower()
    line = line.split()
    for t in line:
      word = list(t)
      for letter in word:
        if re.match('[a-z]', letter):
          letters[letter] = letters.get(letter,0) + 1
  letterlist = []
  for letter, count in letters.items():
    letterlist.append( (letter, count) )
  for letter, count in sorted(letterlist):
    print(letter, count)

"""
Output:
Enter filename: file_name.txt
a 475
b 105
.
.
.
y 142
z 3
"""
