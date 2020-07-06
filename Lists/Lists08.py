"""
Write a Python program to get the frequency of the elements in a list.
"""

import collections
lists = [10,20,20,30,30,30,40,40,40,40,50,50,50,50,50]
print("Original List : ",lists)
count = collections.Counter(lists)
print("Frequency of the elements in the List : ",count)

"""
Output:
Original List :  [10, 20, 20, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50, 50]
Frequency of the elements in the List :  Counter({50: 5, 40: 4, 30: 3, 20: 2, 10: 1})
"""
