if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second = sorted(set([x[1] for x in records]))[1]
    print("\n".join(sorted([x[0] for x in records if x[1] == second])))
        

# l= [[input(), float(input())] for _ in range(int(input()))]
# sh = sorted(list(set([m for name, m in l])))[1]
# print('\n'.join([a for a,b in sorted(l) if b == sh]))

# if __name__ == '__main__':
#     records=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append((name,score))
#     second=sorted(list(set([x[1] for x in records])))[1]
#     results=sorted([k for k,v in records if v==second])
#     for k in results:
#         print(k)