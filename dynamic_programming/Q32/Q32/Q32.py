
if __name__=="__main__":

    n=5
    arr=[[0,0,0,0,0,0],
         [0,7,0,0,0,0],
         [0,3,8,0,0,0],
         [0,8,1,0,0,0],
         [0,2,7,4,4,0],
         [0,4,5,2,6,5]]
    d=[0,0,0,0,0]*n
    #print(arr)
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j]=max(arr[i-1][j-1],arr[i-1][j])+arr[i][j]
            #print(arr[i-1][j-1],arr[i][j-1])
    #print(arr)
    print(max(arr[n]))