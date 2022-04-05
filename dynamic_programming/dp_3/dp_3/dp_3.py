
if __name__=="__main__":
    n=4
    arr=[1,3,1,5]

    d=[0]*100

    d[0]=arr[0]
    d[1]=arr[1]

    for i in range(n):
        d[i]=max(d[i-1],d[i-2]+arr[i])
    print(d[n-1])
