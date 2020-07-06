"""
Write a program to reverse only words in a string.
"""

s = input("Enter the string : ")
r = ' '.join(reversed(s.split(' ')))
print("After reversing : "+r)

"""
Output:
Enter the string : I Love Food
After reversing : Food Love I
"""
