# TASK
# You are given a set  and  number of other sets. 
# These  number of sets have to perform some specific mutation operations on set .

# Your task is to execute those operations and print the sum of elements from set .


n = int(input())
set_A = set(map(int, input().split()))

num_operations = int(input())

for _ in range(num_operations):
    operation, num_elements = input().split()
    num_elements = int(num_elements)
    
    other_set = set(map(int, input().split()))
    
    temp_set_A = set_A.copy()
    if operation == 'intersection_update':
        temp_set_A.intersection_update(other_set)
    elif operation == 'update':
        temp_set_A.update(other_set)
    elif operation == 'symmetric_difference_update':
        temp_set_A.symmetric_difference_update(other_set)
    elif operation == 'difference_update':
        temp_set_A.difference_update(other_set)    
    set_A = temp_set_A #aggiorna il set con la copia modificata

print(sum(set_A))