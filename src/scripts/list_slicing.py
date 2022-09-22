# cook your dish here
# def  list_fun_perform(*lst):
    
#     print(*lst.reverse())



t = int(input())
if(t>=1 and t<=25):
    l = int(input())
    lst = []
    if(l<=50 and l>=2):
        for _ in range(l):
            element = int(input())
            if(element>=-100 and element<=100):
                lst.append(element)
    print(lst)
