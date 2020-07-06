"""
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""

lists = [58,38,75,78,39,20,48,57,84,32,45,23,42] 
for n in lists: 
    if n % 2 != 0: 
       print(n, end = " ")
       
"""
Output:
75 39 57 45 23
"""
