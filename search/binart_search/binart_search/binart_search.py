import sys
#재귀
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

#반복문
def binary_search2(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
if __name__=="__main__":
    
    arr=[2,7,1,8,10,9,18,5,6]
    
    target=10
    arr.sort()
    print(arr)
    result=binary_search2(arr,target,0,len(arr)-1)
    if result==None:
        print("none")
    else:
        print(result)
        print(arr[result])


    #빠른 입력
    input_data=sys.stdin.readline().rstrip()
    #rstrip()은 공백문자 제거

    print(input_data)
