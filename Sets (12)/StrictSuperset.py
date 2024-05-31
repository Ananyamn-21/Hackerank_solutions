# You are given a set  and  other sets.
# Your job is to find whether set  is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

A = set(map(int, input().split()))

for i in range(int(input())):
    B = set(map(int, input().split()))
    if not A.issuperset(B) or len(A) == len(B):
        print(False)
        exit()
        
print(True)