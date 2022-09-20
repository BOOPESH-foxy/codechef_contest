t = int(input())
if(t<=25 and t>=1):
    for i in range(t):
        n = int(input())
        if((n<=100 and n>=0)):
            for i in range(n):
                if(i == 0):
                    print('3', end = " ")
                elif(i%2 == 0 ):
                    print(2*i , end=" ")
                elif(i%2 == 1):
                    print(i**2 , end=" ")
            print("")