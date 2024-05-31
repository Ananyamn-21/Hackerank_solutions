# Task
# The students of District College have subscriptions to English
# and French newspapers. Some students have subscribed only to English, 
# some have subscribed to only French and some have subscribed to both newspapers.

# You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper, and the other set is
# subscribed to the French newspaper. The same student could be in both sets. Your task is to find the 
# total number of students who have subscribed to at least one newspaper.

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_english_subscribers= int(input())
student_english_susbcribers = set(map(int, input().split()))
num_french_subscribers = int(input())
student_french_subscribers = set(map(int, input().split()))

u = student_english_susbcribers.union(student_french_subscribers) 
#print(u)
print(len(u))