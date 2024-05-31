# Task

# You are the manager of a supermarket.
# You have a list of  items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

from collections import OrderedDict
N = input()
value = 0
od = OrderedDict()
for row in range(0,int(N)):
    kargs = input().split()
    item_name = " ".join(kargs[:-1])
    net_price = int(kargs[-1])
    value = od.get(item_name,0)
    od[item_name] = net_price +value
    
for key,value in od.items():
    print(key,value)