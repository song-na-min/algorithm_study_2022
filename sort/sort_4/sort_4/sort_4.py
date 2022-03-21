
if __name__=="__main__":

    n,k=map(int,input().split())

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a=sorted(a)
    b=sorted(b,reverse=True)
    #print(a)
    #print(b)
    for i in range(k):
        if a[i]>=b[i]:
            break
        a[i],b[i]=b[i],a[i]
        #print(a[i],b[i])

    print(sum(a))