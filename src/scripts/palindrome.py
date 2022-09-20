t=int(input())
if (t>=1 and t<=25):
    for _ in range(t):
        string = input().lower()
        if(len(string)>=2 and (len(string)<=100)):
            if string == string[ : : -1]:
                print("It is a palindrome")
            else:
                print("It is not a palindrome")
