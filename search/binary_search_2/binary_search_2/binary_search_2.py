import sys

def binary_search(arr,target,start,end):
    
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return "Yes"
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return "No"
if __name__=="__main__":
    #n=int(input())
    #input_data=list(map(int,sys.stdin.readline().rstrip().split()))
    #m=int(input())
    #customer=list(map(int,sys.stdin.readline().rstrip().split()))
    n=5
    input_data=[8,3,7,9,2]
    m=3
    customer=[5,7,9]
    input_data.sort()
    print(input_data)
    for target in customer:
        print(target)
        print(binary_search(input_data,target,0,n-1)+" ")
