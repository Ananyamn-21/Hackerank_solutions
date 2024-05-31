# There is an array of  integers. There are also  disjoint sets,  
# and , each containing  integers. You like all the integers in set 
# and dislike all the integers in set . Your initial happiness is . 
# For each  integer in the array, if , you add  to your happiness.
#  If , you add  to your happiness. Otherwise, your happiness does not 
#  change. Output your final happiness at the end.

# Note: Since  and  are sets, they have no repeated elements. However, 
# the array might contain duplicate elements.

n_and_m = input().split()
n = n_and_m[0]
m = n_and_m[1]
arr = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in arr:
    if i in set_a:
        happiness +=1
    if i in set_b:
        happiness-=1
print(happiness)
