
def gold(arr,n,m):
    max_num=0
    for j in range(2,m+1):
        for i in range(1,n+1):
            arr[i][j]=arr[i][j]+max(arr[i-1][j-1],arr[i][j-1],arr[i+1][j-1])
            if j==m and max_num<arr[i][j]:
                max_num=arr[i][j]
    #print(arr)
    #print(arr[n][m])
    return max_num
if __name__=="__main__":

    t=2

    n,m=3,4
    arr=[[0,0,0,0,0],
         [0,1,3,3,2],
         [0,2,1,4,1],
         [0,0,6,4,7],
         [0,0,0,0,0]]

    print(gold(arr,n,m))
    """
    for k in range(t):
        ...입력받고 함수
    """
    n,m=4,4
    arr=[[0,0,0,0,0],
         [0,1,3,1,5],
         [0,2,2,4,1],
         [0,5,0,2,3],
         [0,0,6,1,2],
         [0,0,0,0,0]]
    print(gold(arr,n,m))

