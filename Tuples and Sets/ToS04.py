"""
Use python set to check if two lists have at-least one element common element.
"""

list1 = [54,24,79,4] 
list2 = [86,54] 
flag = 0
for i in list1: 
    if i in list2: 
        flag = 1
if flag == 1: 
    print("Yes")  
else : 
    print("No") 
    
"""
Output:
Yes
"""
