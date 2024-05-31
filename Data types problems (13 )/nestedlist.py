#  Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) having the 
# second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
   all_students = [] 
   all_score = [] 
   filtred_score = [] 
   second_students = [] 
for _ in range(int(input())): 
     name = input() 
     score = float(input()) 
     one_student = [name,score]
     all_students.append(one_student)


for student in (all_students):
    all_score.append(student[1])

all_score.sort()

for score in all_score:
    if score != min(all_score):
        filtred_score.append(score)

second_score = filtred_score[0]

for name, score in all_students:
    if score == second_score:
        second_students.append(name)

second_students.sort()
for student in second_students:
    print(student)
