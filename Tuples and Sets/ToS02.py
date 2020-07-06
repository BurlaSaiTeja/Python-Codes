"""
Write a Python program to sort a tuple by its float element. 
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
"""

a=[('item1','12.20'),('item2','15.10'),('item3','24.5')]
print(sorted(a,key=lambda b : float(b[1]),reverse=True))

"""
Output:
[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""
