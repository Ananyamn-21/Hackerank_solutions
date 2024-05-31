# You are given  words. Some words may repeat. 
# For each word, output its number of occurrences. 
# The output order should correspond with the input
#  order of appearance of the word. See the sample input/output for clarification.

# Note: Each input line ends with a "\n" character.

from collections import Counter

mylist = []

for i in range (int(input())):
    mylist.append(input())
    
count = Counter(mylist)

print(len(count.keys()))
print(' '.join(list(map(str,list(count.values())))))