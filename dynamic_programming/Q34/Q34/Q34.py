
if __name__=="__main__":

    n=7
    arr=[15,11,4,8,5,2,4]
    dp=[1]*n
    for i in range(n):
        max_count=0
        for j in range(i):
            if arr[i]<arr[j]:
                max_count=max(dp[j],max_count)
        dp[i]+=max_count

    print(dp)
    print(n-max(dp))

