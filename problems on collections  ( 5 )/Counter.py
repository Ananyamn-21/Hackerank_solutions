# Task

#  is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money
#  only if they get the shoe of their desired size.

# Your task is to compute how much money  earned

import sys
from collections import Counter

(X, S, _, *cust) = [[float(n) for n in l.rstrip().split(" ")] for l in sys.stdin]

stock = Counter(S)
earn = 0.0
for i, (s, m) in enumerate(cust):
    bought = Counter([size for (size, _) in cust[:i+1]])
    if bought[s] <= stock[s]:
        earn += m
    
print(int(earn))