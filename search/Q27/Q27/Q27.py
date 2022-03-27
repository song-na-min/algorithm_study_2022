
def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    global count
    if arr[mid]==target:
        count+=1
        binary_search(arr,target,mid+1,end)
        binary_search(arr,target,start,mid-1)
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
if __name__=="__main__":

    count=0

    n,x=7,2
    arr=[1,1,2,2,2,2,3]
    #n,x=7,4
    
    binary_search(arr,x,0,n-1)
    if count==0:
        print("-1")
    else:
        print(count)