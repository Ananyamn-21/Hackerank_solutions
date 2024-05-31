# Task
# Students of District College have subscriptions to English
# \ and French newspapers. Some students have subscribed to
# \ English only, some have subscribed to French only, and
# some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has 
# subscribed to the English newspaper, and one set has subscribed
# to the French newspaper. Your task is to find the total number of students who
# have subscribed to either the English or the French newspaper but not both.


_ = input()
set_a = {int(e) for e in input().split(' ')}
_ = input()
set_b = {int(e) for e in input().split(' ')}

print(len(set_a.symmetric_difference(set_b)))
