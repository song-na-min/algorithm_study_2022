
if __name__=="__main__":
    #n=4
    #arr=[5,1,7,9]
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()

    sum=0
    for i in arr:
        sum+=i-arr[0]
    print(sum)
    min=sum
    min_location=0
    print(arr)
    first=arr[0]
    last=arr[-1]
    left=1
    right=n-1
    #print(left,right)
    for k in range(first+1,last+1):
        if k in arr:
            sum=sum+left-right
            left+=1
            right-=1
            #print(k,left,right)
            
        else:
            sum=sum+left-right
        #print(k,sum)
        if min>sum:
            min=sum
            min_location=k

    #print(min)
    print(min_location)
