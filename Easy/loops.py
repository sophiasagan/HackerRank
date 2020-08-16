# The provided code stub reads an integer, n , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than n=3 is [0, 1, 2] . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

# The first and only line contains the integer,n .

# Constraints
# 1 <= n <= 20

# Output Format

# Print n lines, one corresponding to each i.

if __name__ == '__main__':
    n = int(input())

i = 0
while i < n:
    print(i**2)
    i += 1

# another option: 

for i in range(0, n):
    print(i**2)