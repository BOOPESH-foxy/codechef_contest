def dec_to_binary(n):
    print('{:08b}'.format(n))
    # if n>1:
    #     dec_to_binary(n//2)
    # print(n%2,end ="")
    # print(bin(format(n,'08b')))


t = int(input())
if(t>=1 and t<=25):
    for _ in range(t):
        dec_data = int(input())
        if(dec_data>=1 and dec_data<=255):
            dec_to_binary(dec_data)
            print()