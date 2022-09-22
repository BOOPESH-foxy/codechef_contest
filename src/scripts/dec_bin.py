import numpy as arr
def dec_to_binary(n):
    if n>1:
        dec_to_binary(n//2)
    empty_list.append(n%2)
    return empty_list

t = int(input())
if(t>=1 and t<=25):
    bin_lst = []
    for _ in range(t):
        empty_list = []
        dec_data = int(input())
        if dec_data == 0:
            for _ in range(0,8):
                print("0",end="")
        elif(dec_data>=1 and dec_data<=255):
            bin_lst = dec_to_binary(dec_data)
            d_0 = 8 - len(bin_lst)
            for _ in range(d_0):
                print("0",end = "")
            for _ in range(len(bin_lst)):
                print(bin_lst[_],end = "")
        print()