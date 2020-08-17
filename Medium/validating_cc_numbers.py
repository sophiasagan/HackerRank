import re

def check(card):
    if not re.search("^[456]\d{3}(-?\d{4}){3}$",card) or re.search(r"(\d)\1{3}", re.sub("-", "",card)):
        return False
    return True

n = int(input())
for i in range(n):
    print("Valid" if check(input()) else "Invalid")