
if __name__=="__main__":
    #n,c=list(map(int,input().split()))
    #array=[]
    #for _ in range(n):
    #    array.append(int(input()))
    n,c=5,3
    array=[1,2,4,8,9]
    array.sort()

    start=1
    end=array[-1]-array[0]

    result=0

    # 최소의 거리를 이진탐색하여 찾기
    while(start<=end):
        mid=(end+start)//2#거리
        print(start,mid,end)
        value=array[0]
        count=1
        for i in range(1,n):
            if array[i]>=value+mid:#만약 최소 거리보다 먼 곳에 있으면
                value=array[i]
                print(value)
                count+=1#공유기 설치
        print("----------")
        if count>=c:#거리를 더 벌릴수 있을 때
            start=mid+1
            result=mid#최적을 일단 저장
        else:#더 거리를 찾는게 불가능=>거리의 범위(end)를 줄인다
            end=mid-1

    print(result)