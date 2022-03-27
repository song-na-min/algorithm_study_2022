
def binary_search(arr,start,end):
    mid=(start+end)//2
    if start>end:
        return -1
    #print(mid,arr[mid])
    if arr[mid] == mid:
        #print(mid)
        return mid
    elif arr[mid]>mid:
        #binary_search(arr,arr[mid]+1,end)
        return binary_search(arr,start,mid-1)
    else:
       # binary_search(arr,start,arr[mid]-1)
        return binary_search(arr,mid+1,end)

"""
    위 함수에 주석으로 처리한 부분은 직접 푼 답으로 실제 답이 있는 경우 출력은 가능했지만
    답이 없는 경우 -1이 출력되지 않았다 이유는 return 되는 게 없어서인데
    실제 답이 있는 경우 또한 return되는 값은 없었다
    위와 같이 푼 이유는 양쪽을 확인해야 한다는 생각이었는데 ..
"""
if __name__=="__main__":
    n=5
    arr=[-15,-6,1,3,7]
    #n=7
    #arr=[-15,4,3,8,9,13,15]
    
    result=binary_search(arr,0,n-1)
    print(result)