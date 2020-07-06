"""
For all classes include __init__ and __str__
Write a program that has a class called Person.
Attributes of person class : usn, name,dob, gender
Inside __init__
Validate USN (1CR15CS104) before setting the private value usn
Validate date by trying to create a valid date object from the string.
If date is valid, calculate age and store it in the age instance variable.
** use assert or exceptions to display unsuccessful object creations.

Write a method called time_to_bday() that returns the days to the Persons next b’day. Use the date, timedelta.

Inherit a class Student from Person which also has a class MarksAttendance

Attributes for student class : branch, year, MA
__init__ should receive (usn, name, dob, gender, branch, year, ma)
Should call super().__init__ to initialize usn, name, dob and gender
Should initialize year, branch and ma
ma is an object of the MarksAttendance class
__str__ should return a printable student class with all the details

MarksAttendance class
Class Attribute : max_mark:80, max_classes:62
Attributes : marks, attendance, marks_dict, att_dict
__init__ should receive a list of subjects, list of marks and list of attendance
Validate that lengths of al 3 lists are equal
Create a dictionary object for marks_dict, assigning marks to subjects
Create a dictionary object for att_dict, assigning attendance to subject
Calculate marks and attendance by calling methods
__str__ should return a printable student class with all the details
Calculate and return average marks by using the class attribute max_marks
Calculate and return average percentage by using class attribute max_classes
"""

from datetime import date, datetime
import re


class Person:

    def __init__(self, usn='', name='', dob=None, gender=''):
        if self.validate_usn(usn) and self.validate_dob(dob):
            self.usn = usn
            self.dob = dob
        else:
            """ Object creation should fail with appropriate error msg"""
            print("Incorrect USN or DOB")
            exit(0)
        self.name = name
        self.gender = gender
        self.age = self.calculate_age()

    def __str__(self):
        """ should return in the form, 1CR14CS015 Arjun 1990-11-2 M """
        return "{} {} {} {}\n".format(self.usn, self.name, self.dob, self.gender)

    def validate_usn(self, usn):
        """ use regular expression to validate usn of form 1CR14CS015 """
        if re.match("1(cr|CR)\d{2}\w{2}\d{3}", usn):
            return True
        return False

    def validate_dob(self, dob):
        """ create a date object """
        try:
            if re.match("\d{4}-\d{2}-\d{2}", dob):
                y, m, d = map(int, dob.split('-'))
                date(y, m, d)
                return True
        except:
            return False

    def calculate_age(self):
        """ calculate and extract from timedelta object or by calculating difference between years"""
        today = date.today()
        y, m, d = map(int, self.dob.split('-'))
        return today.year - y - ((today.month, today.day) < (m, d))

    def get_age(self):
        """ return age """
        return self.calculate_age()

    def time_to_bday(self):
        """ get today from the date module
        use a variable bday_this_year and set year of b'day to current year.
        if today is <= bday_this_year calculate the time difference between today and dob, extract days from timedelta
        if today is past, then set year in bday_this_year to next year and calculate
        return time delta object """

        t = datetime.now()
        y, m, d = map(int, self.dob.split('-'))
        return (datetime(t.year, m, d) - t.today()).days


class MA:
    max_marks = 80  # for each subject
    max_classes = 62  # for each class

    def __init__(self, subject_list, marks_list, att_list):
        """ validate lengths
        self.marks_dict, self.att_dict
          self.marks = calculate_avg_marks()
          self.att = calculate_avg_att()"""
        if len(subject_list) == len(marks_list) == len(att_list):
            self.marks_dict = dict(zip(subject_list, marks_list))
            self.att_dict = dict(zip(subject_list, att_list))
            self.marks = self.calculate_avg_marks(marks_list)
            self.att = self.calculate_avg_att(att_list)

    def __str__(self):
        """ return in the form for each subject, subjectname : marks - 85%, attendance - 95%"""
        return '\n'.join('{} : marks - {}%, attendance - {}%'.format(subject, mark, attendance) for subject, mark, attendance in zip(subject_lst, marks_lst, att_lst))

    def calculate_avg_marks(self, mark):
        return sum(mark) / len(mark)

    def calculate_avg_att(self, att):
        return sum(att) / len(att)


class Student(Person):
    def __init__(self, usn, name, dob, gender, branch, year, ma):
        """ call superclass init and pass usn, name dob, gender """
        """ assign branch year and MA"""
        super().__init__(usn, name, dob, gender)
        self.branch = branch
        self.year = year
        self.ma = ma

    def __str__(self):
        """ combine string representations of Person object with student object and ma object and return all details of a
            student in printable string version """
        return "{}Branch: {}\nYear: {}\n\n{}\n".format(super().__str__(), self.branch, self.year, ma.__str__())


# Driver Code

subject_lst = ['OS', 'SSCD', 'PAP', 'CG']
marks_lst = [65, 60, 55, 50]
att_lst = [42, 50, 60, 58]

ma = MA(subject_lst, marks_lst, att_lst)
student = Student('1CR14CS015', 'Arjun', '1990-11-04', 'M', 'CSE', 4, ma)

print(student)
print("Age", student.get_age())
print("Time to next birthday", student.time_to_bday())

"""
Output:
1CR14CS015 Arjun 1990-11-04 M
Branch: CSE
Year: 4

OS : marks - 65%, attendance - 42%
SSCD : marks - 60%, attendance - 50%
PAP : marks - 55%, attendance - 60%
CG : marks - 50%, attendance - 58%

Age 29
Time to next birthday 178
"""

