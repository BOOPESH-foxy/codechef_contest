t = int(input())
if(t<=25 and t>=1):
    for _ in range(t):
        n = int(input())
        if (n>=2 and n<=100):
            empty_lst = []
            score_list = []
            for _ in range(n):
                name , score = input().split()
                float(score)
                if(float(score)>=0.0 and float(score)<=100.0):
                    score_list.append([score,name])
            score_list.sort(reverse=True)
            score_top = score_list[0][0] 
        for _ in range(len(score_list)):
            if(score_top == score_list[_][0]):
                empty_lst.append(score_list[_][1])
        empty_lst.sort()
        for _ in range(len(empty_lst)):
            print(empty_lst[_])