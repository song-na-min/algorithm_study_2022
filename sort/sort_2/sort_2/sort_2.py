
if __name__=="__main__":

    n=int(input())#개수

    arr=[]

    for i in range(n):
        arr.append(int(input()))

    arr=sorted(arr,reverse=True)

    for i in range(n):
        print(arr[i],end=" ")