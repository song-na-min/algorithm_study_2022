from itertools import permutations
import math
if __name__=="__main__":

    n,m=map(int,input().split())

    arr=[list(map(int,input().split())) for _ in range(n)]

    home=[]
    chicken=[]

    for i in range(n):
        for j in range(n):
            value=(i,j)
            if arr[i][j]==1:
                home.append(value)
            if arr[i][j]==2:
                chicken.append(value)
    print(home)
    print(chicken)
    result=100
    for chicken_list in list(permutations(chicken,m)):
        sum=0
        for h in home:
            min_dist=100
            for c in chicken_list:
                dist=abs(h[0]-c[0])+abs(h[1]-c[1])
                min_dist=min(min_dist,dist)
            sum+=min_dist
        result=min(result,sum)
    print(result)