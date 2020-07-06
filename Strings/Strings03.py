"""
Write a program to check if two given strings are anagram or not.
"""

def Anagram(str1, str2):   
    n1 = len(str1)  
    n2 = len(str2)  
    if n1 != n2:  
        return 0
    str1 = sorted(str1) 
    str2 = sorted(str2)  
    for i in range(0, n1):  
        if str1[i] != str2[i]:  
            return 0
    return 1
if __name__ == "__main__": 
    str1 = input("Enter String 1 : ")
    str2 = input("Enter String 2 : ")
    if Anagram(str1, str2):  
        print ("The two strings are anagram of each other") 
    else:  
        print ("The two strings are not anagram of each other")

"""
Output:
Enter String 1 : test
Enter String 2 : estt
The two strings are anagram of each other
"""
