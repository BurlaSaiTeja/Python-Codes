"""
Create an array of 5 integers [2,3,3,3,4]. Access the first individual items through indexes.
Append a new item, 8 to the end of the array.
Reverse the items in the array.
Output the length in bytes of one array item in the internal representation.
Output the current memory address and the length in elements of the buffer used to hold an array.
Find number of occurences of 3 in the array.
Append the iterable lst = [8,6,48] to the array.
Create another integer array with values [14,15,16] and append to array.
Insert 1 before the 1st element in the array.
Remove the first occurrence of 3 from the array.
Pop the element with index, 4 from the array.
Print the array.
"""

import array as a
arr1 = a.array('i',[2,3,3,3,3,4])
print("Array printed using indexing : ")
for i in range(0,6):
    print(arr1[i])
arr1.append(8)
print("Array after appending 8 at the end :",arr1)
arr1.reverse()
print("Array after reversing :",arr1)
print("The length in bytes of one array item in the internal representation :",arr1.itemsize)
print("The current memory address and the length in elements of the buffer :",arr1.buffer_info())
print("The number of 3's in current array :",arr1.count(3))
lst = [8,6,48] 
for j in lst:
    arr1.append(j)
print("Array after appending the list :",arr1)
arr2 = a.array('i',[14,15,16])
arr=arr1+arr2
print("Array after appending another array to it :",arr)
arr.insert(0,1)
print("Array after inserting 1 at the beginning :",arr)
arr.remove(3)
print("Array after removing the first occurance of element 3 :",arr)
arr.pop(4)
print("Array after popping element at index 4 :",arr)

"""
Output:
Array printed using indexing : 
2
3
3
3
3
4
Array after appending 8 at the end : array('i', [2, 3, 3, 3, 3, 4, 8])
Array after reversing : array('i', [8, 4, 3, 3, 3, 3, 2])
The length in bytes of one array item in the internal representation : 4
The current memory address and the length in elements of the buffer : (4418430616, 7)
The number of 3's in current array : 4
Array after appending the list : array('i', [8, 4, 3, 3, 3, 3, 2, 8, 6, 48])
Array after appending another array to it : array('i', [8, 4, 3, 3, 3, 3, 2, 8, 6, 48, 14, 15, 16])
Array after inserting 1 at the beginning : array('i', [1, 8, 4, 3, 3, 3, 3, 2, 8, 6, 48, 14, 15, 16])
Array after removing the first occurance of element 3 : array('i', [1, 8, 4, 3, 3, 3, 2, 8, 6, 48, 14, 15, 16])
Array after popping element at index 4 : array('i', [1, 8, 4, 3, 3, 2, 8, 6, 48, 14, 15, 16])
"""
