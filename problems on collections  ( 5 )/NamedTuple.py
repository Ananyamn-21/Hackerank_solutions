# Task

# Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .

# Your task is to help Dr. Wesley calculate the average marks of the students.

from collections import namedtuple

n, student_info, students, total = int(input()), namedtuple('student_info', input().split()), [], 0
for i in range(n):
    students.append(student_info(*input().split()))
    total += int(students[i].MARKS)

print(total/n)