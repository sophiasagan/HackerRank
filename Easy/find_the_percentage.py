if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total_marks = sum(student_marks[query_name]) # add all scores of student queried
    average_marks = total_marks/3 # take average of scores

    print("%.2f"%(average_marks)) # printing logic round to two digits
