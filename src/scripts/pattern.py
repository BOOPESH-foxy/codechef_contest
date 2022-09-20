t = int(input())
if(t>=1 and t<=25):
    for _ in range(t):
        n = int(input())
        if(n>=1 and n<=100):
            for _ in range(n):
                i =1
                for i in range(n+1):
                    if(i == 0):
                        print(end="")
                    elif(i%5):
                        print('*',end="")
                    else:
                        print("#",end="")
                print("")
                n -=1