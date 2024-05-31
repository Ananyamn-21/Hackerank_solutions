# The defaultdict tool is a container in the collections 
# class of Python. It's similar to the usual dictionary 
# (dict) container, but the only difference is that a
# defaultdict will have a default value if that key has not been set yet. If you 
# didn't use a defaultdict you'd have to check to see 
# if that key exists, and if it doesn't, set it to what you want.
# # For example:

# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
# This prints:

# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])
# In this challenge, you will be given  integers,  and .
#  There are  words, which might repeat, in word group . 
# There are  words belonging to word group . For each 
# words, check whether the word has appeared in group  or not. Print the 
# indices of each occurrence of  in group . If it does not appear, print .

n,m=map(int,input().split())
A=[input() for _ in range(n)]
B=[input() for _ in range(m)]

for i in range(len(B)):
    if B[i] not in A:
        print(-1)
    elif B[i] in A:
        for j in range(len(A)):
            if B[i]==A[j]:
                print(j+1,end=" ")
        print("")
