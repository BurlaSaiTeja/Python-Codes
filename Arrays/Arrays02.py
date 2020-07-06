"""
Write a Python program to find whether a given array of integers contains any duplicate element. 
Return true if any value appears at least twice in the said array and return false if every element is distinct.
"""

import array as a
a1 = a.array("i", [12,1,11,12,1,1,11,12])
flag = False
for i in range(0,len(a1)):
    for j in range(i+1,len(a1)):
        if(a1[i]==a1[j]):
            flag = True
print(flag)

"""
Output:
True
"""
