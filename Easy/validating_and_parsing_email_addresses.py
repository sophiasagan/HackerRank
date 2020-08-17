import re
n = int(input())

for _ in range(n):
    username, useremail = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', useremail)
    if m:
        print(username, useremail)