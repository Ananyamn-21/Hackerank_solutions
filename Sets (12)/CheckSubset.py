# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.
T=int(input('')) 
b=[] 
for i in range(T): 
    n=int(input('')) 
    a1=set(map(int, input().split(' '))) 
    m=int(input('')) 
    a2=set(map(int, input().split(' '))) 
    if a1.issubset(a2): 
        b.append('True') 
    else: 
        b.append('False')

for i in b: 
    print(i)

