# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands 
# where each command will be of the  types listed above. Iterate through each command in
# order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0,N) :
        x = input().split()
        if x[0] == 'insert' :
            lst.insert(int(x[1]),int(x[2]))
        if x[0] == 'print' :
            print(lst)
        if x[0] == 'remove' :
             lst.remove(int(x[1]))
        if x[0] == 'append' :
            lst.append(int(x[1]))
        if x[0] == 'sort' :
            lst.sort()
        if x[0] == 'pop' :
            lst.pop(-1)
        if x[0] == 'reverse' :
            lst.reverse()