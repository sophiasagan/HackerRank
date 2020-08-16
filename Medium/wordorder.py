from collections import Counter, OrderedDict
# https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/


class OrderedCounter(Counter, OrderedDict): # create class
    pass

N = int(input())
word_count = OrderedCounter(
    [input() for _ in range(N)]
)

print(len(word_count)) # logic for printing
print(*word_count.values()) #unpack values


from collections import OrderedDict
#define empty ordered dictionary, which counts occurences
dict = OrderedDict()

for i in range(int(input())):
    #If input not in the dictionary, then add it
    #else increment the counter
    key = input()
    if not key in dict.keys():
        dict.update({key : 1})
        continue
    dict[key] += 1

print(len(dict.keys()))
print(*dict.values())