from collections import namedtuple

n = int(input())
a = input()
markAve = 0
Student = namedtuple('Student', a)

for _ in range(n):
    student = Student(*input().split())
    markAve += int(student.MARKS)
print('{:.2f}'.format(markAve/n))