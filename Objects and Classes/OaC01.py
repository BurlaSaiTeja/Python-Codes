"""
Write a definition for Student class
Define __init__(self, marks=[]) for the Student class
Define add_marks(self,lst) that appends mark to the marks list
Create two students, s1 and s2.
Add [25,45,65] to s1
Print marks of s1 and s2
Observe what happens?
Fix the code.
"""

class Student:
  def __init__(self, marks=None):
    if marks is not None:
      self.marks = marks
    else:
      self.marks = []
  
  def add_marks(self, lst):
    self.marks.append(lst)

  def __str__(self):
    return str(self.marks)


s1 = Student()
s2 = Student()

print("Marks of S1:", s1)
print("Marks of S2:", s2)

s1.add_marks([25,45,65])

print("Marks of S1 after add_marks: ", s1)
print("Marks of S2 after add_marks: ", s2)

"""
Output:
Marks of S1: []
Marks of S2: []
Marks of S1 after add_marks:  [[25, 45, 65]]
Marks of S2 after add_marks:  []
"""
