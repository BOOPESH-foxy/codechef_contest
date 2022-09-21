# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):
    AP_series = []
    for _ in range(n):
        ap_v = a1 + (_)*d
        AP_series.append(ap_v)
        ap_v = 0
    return AP_series

def square_ap(AP_series):
    return AP_series ** 2

# Main function
if __name__ == '__main__':
    
    t = int(input())
    if(t<=25 and t>=1):
        for _ in range(t):
            a1 , d , n = map(int,input().split())
            if((a1<=20 and a1>=1)and (d>=1 and d<=20)and (n>=1 and n<=200)):
                AP_series = generate_AP(a1, d, n)
            for _ in range(n):
                print(AP_series[_],end = " ")
            print()
        
        
        # Using lambda and map functions, find squares of terms in AP series and print it
            sqr_AP_series = list(map(lambda x:x ** 2,AP_series))
            for _ in range(n):
                print(sqr_AP_series[_],end = " ")   
            print()
        
        
        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
            sum_sqr_AP_series = reduce(lambda a,b:a+b,sqr_AP_series)
            print(sum_sqr_AP_series)