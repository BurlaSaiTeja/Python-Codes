"""
Write a program for string slicing to check if a string can become empty by recursive deletion of a substring.
"""

def checkIfEmpty(string, substr): 
    if len(string)== 0: 
         return 1
    while (len(string) != 0): 
          index = string.find(substr) 
          if (index ==(-1)): 
              return 0
          string = string[0:index] + string[index + len(substr):]              
    return 1
if __name__ == "__main__": 
    string = input("Enter the string : ")
    substr = input("Enter the substring : ")
    if checkIfEmpty(string, substr):
       print("Yes, the string can become empty by recursive deletion.")
    else:
       print("No, the string cant become empty by recursive deletion.")

"""
Output:
Enter the string : MONMONKEYKEY
Enter the substring : MONKEY
Yes, the string can become empty by recursive deletion.
"""
