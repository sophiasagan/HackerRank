import re

n = int(input())

for i in range(n):
    match = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input(), re.IGNORECASE)
    for m in match:
        print(m)



