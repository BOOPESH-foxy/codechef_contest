t = int(input())
for _ in range(t):
    str_1 = str(input())
    i = 0
    count = 0
    for i in range(len(str_1)):
        if(str_1[i] == ' '):
            print(count,end="")
            print(',',end="")
            count = 0
        else:
            count+=1