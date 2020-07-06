"""
Write a Python program to replace last value of tuples in a list.  
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
"""

l=[(10,20,40),(40,50,60),(70,80,90)]
print([x[:-1]+(100,)for x in l])

"""
Output:
[(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
