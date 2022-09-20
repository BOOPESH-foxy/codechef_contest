# Function to calculate Euclidean distance between two points
import math
def compute_distance(x1, y1, x2, y2):
    x= x1 - x2 
    y = y1 - y2
    a=pow(x,2);
    b=pow(y,2);
    return math.sqrt(a+b)

if __name__ == '__main__':
    t = int(input())
    if(t>=1 and t<=25):
        for _ in range(t):
            x1,y1,x2,y2 = map(int,input().split())
            if((x1>=-100 and x1<=100) and (x2>=-100 and x2<=100) and (y2>=-100 and y2<=100) and (y1>=-100 and y1<=100)):
                eucledian_distance = compute_distance(x1, y1, x2, y2)
                print("Distance:","{:.2f}".format(eucledian_distance))
                