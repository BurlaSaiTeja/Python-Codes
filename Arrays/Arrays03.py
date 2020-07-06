"""
Write a Python program to find the first duplicate element in a given array of integers. 
Return -1 If there are no such elements.
"""

import array as a
a1 = a.array("i", [1,11,12,1,1,11,12])
a2 = a.array("i", [])
flag = True
for i in a1:
    if i not in a2:
        a2.append(i)
    else:
        print("Duplicate:", i)
        flag = False
        break
if flag:
    print("No duplicates : -1")
    
"""
Output:
Duplicate: 1
"""
