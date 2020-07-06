"""
Write a program to count vowels in a given string.
"""

def Vowels(ch): 
    return ch.lower() in ['a', 'e', 'i', 'o', 'u'] 
def countVowels(str): 
    count = 0
    for i in range(len(str)): 
        if Vowels(str[i]): 
            count += 1
    return count 
if __name__ == "__main__": 
    str = input("Enter the string : ")
    print(countVowels(str)) 

"""
Output:
Enter the string : Discombobulated
6
"""
