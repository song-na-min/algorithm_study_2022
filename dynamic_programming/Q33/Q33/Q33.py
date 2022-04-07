
if __name__=="__main__":

    n=7

    day=[3,5,1,1,2,4,2]
    cost=[10,20,10,20,15,40,200]

    dp=[0]*(n+1)
    max_value=0

    for i in range(n-1,-1,-1):
        time=day[i]+i
        if time<=n:
            dp[i]=max(cost[i]+dp[time],max_value)
            max_value=dp[i]
        else:
            dp[i]=max_value
    print(dp)
    print(max_value)

    """
    total=[[0],[0],[0],[0],[0],[0],[0],[0],[0]]

    for i in range(1,n+1):
        if i+day[i]>n:#범위를 넘어가는 경우
            cost[i]=0
            continue
        cost[i]=max(total[0])+cost[i]
        total[i+day[i]].append(cost[i])
        print("====")
        print(i)
        print(cost)
        print(total)
        print(max(total[i]))
    """

