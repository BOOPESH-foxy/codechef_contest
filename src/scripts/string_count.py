from curses.ascii import isalpha
from turtle import st


t = int(input())
for _ in range(t):
    str_1 = str(input())
    i = 0
    count = 0
    for i in range(len(str_1)):
        isal = str_1[i].isalpha() | str_1[i].isspace()
        if(isal == 1 ):
            if(str_1[i] == ' '):
                print(count,end="")
                print(',',end="")
                count = 0
            else:
                count+=1
        else:
            count = count + 0
    print(count)