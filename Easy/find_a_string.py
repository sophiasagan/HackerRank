def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)+1):
            if(string[i:j]==sub_string):
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


    # another option

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count