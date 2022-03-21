
if __name__=="__main__":

    n=int(input())

    arr=[]

    #https://leedakyeong.tistory.com/entry/python-%ED%8A%9C%ED%94%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%EB%91%90-%EB%B2%88%EC%A7%B8-%EC%9B%90%EC%86%8C%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-tuple-sorting-in-python
    #파이썬 튜플 리스트로 정렬
    for i in range(n):
        name,score=input().split()
        arr.append((name,int(score)))

    arr=sorted(arr,key=lambda student:student[1])
    for student in arr:
        print(student[0],end=" ")