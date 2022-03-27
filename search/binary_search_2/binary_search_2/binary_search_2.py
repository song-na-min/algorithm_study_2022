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

    #집합 자료형
    #문제가 어떠한 수가 한번이라도 등장했는지 검사하면 되기 때문에 집합 사용 가능
    #리스트의 in연산자를 쓰지 않는 이유:속도가 O(n), set은 O(1)
    #https://kyleyj.tistory.com/56
    n=int(input())
    array=set(map(int,input().split()))
    m=int(input())
    x=list(map(int,input().split()))

    for i in x:
        if i in array:
            print("yes",end=" ")
        else:
            print("No",end=" ")




'''
    #계수정렬
    n=int(input())
    array=[0]*1000001
    #각 부품 번호의 인덱스에 값을 1로
    for i in input().split():
        array[int(i)]=1
    m=int(input())
    x=list(map(int,input().split()))
    #해당 인덱스가 있는지 확인,출력
    for i in x:
        if array[i]==1:
            print("YES",end=" ")
        else:
            print("No",end=" ")
'''

"""
#binary search
    #n=int(input())
    #input_data=list(map(int,sys.stdin.readline().rstrip().split()))
    #m=int(input())
    #customer=list(map(int,sys.stdin.readline().rstrip().split()))
    #n=5
    #input_data=[8,3,7,9,2]
    #m=3
    #customer=[5,7,9]
    input_data.sort()
    print(input_data)
    for target in customer:
        print(target)
        print(binary_search(input_data,target,0,n-1)+" ")
"""
