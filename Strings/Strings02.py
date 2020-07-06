"""
Write a program to find a Permutation of a given string.
"""

from itertools import permutations 
def allPerm(str): 
     permList = permutations(str) 
     for perm in list(permList): 
         print (''.join(perm)) 
if __name__ == "__main__": 
    str = input("Enter the string : ")
    allPerm(str) 
    
"""
Output:
Enter the string : abc
abc
acb
bac
bca
cab
cba
"""
