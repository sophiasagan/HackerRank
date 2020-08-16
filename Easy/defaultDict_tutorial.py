# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

# example:
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)

#prints:
('python', ['awesome', 'language'])
('something-else', ['not relevant'])


from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split(' '))

for i in range(1, n+1):
    d[input()].append(str(i))

for i in range(m):
    print(' '.join(d[input()]) or -1)





from collections import defaultdict

# Inputs
# ------
n, m = map(int, input().split(' '))

# Let's get the groups as lists
# -----------------------------
#input1 = ['a', 'a', 'b', 'a', 'b']
#input2 = ['a', 'b']
input1 = list()
for i in range(n):
    input1.append(input())

    input2 = list()
for i in range(m):
    input2.append(input())

# Calculate Output
# ----------------
d = defaultdict(list)

# Fill d with input1 values
for i in range(n):
    d[input1[i]].append(i+1)
#print(d) --> defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

# Apply the logic for printing
for i in input2:    
    if i in d:
        print(*d[i])
    else:
        print(-1)