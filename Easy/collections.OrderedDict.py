from collections import OrderedDict
d = OrderedDict() #set dict

N = int(input()) # input as N
for i in range(N): # for each element in in input
    item,space,price = input().rpartition(" ") # split input
    if item not in d: # if item not in dict
        d[item] = int(price) # add item to dict k/v item/price
    else:
        d[item] += int(price) # otherwise add to price of item

for item_name, net_price in d.items(): # logic for printing 
    print(item_name, net_price)