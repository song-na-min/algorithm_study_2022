
if __name__=="__main__":
    n=3
    m=4

    #arr=[2,3]
    arr=[3,5,7]
    d=[-1]*10000

    for i in arr:
        d[i]=1
    for j in range(arr[0],m+1):
        if d[j]!=-1:
            continue
        d[j]=1000#최소로 비교하기 위해 큰 값을 일단 넣고 
        for i in arr:
            if d[j-i]!=-1:
                d[j]=min(d[j],d[j-i]+1)
        if d[j]==1000:#만약 앞에서 update가 되지 않은 경우
            d[j]=-1#불가능하다
    print(d[m])