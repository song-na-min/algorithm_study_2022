
if __name__=="__main__":

    a="sunday"
    b="saturday"


    dp=array = [[0 for col in range(len(a)+1)] for row in range(len(b)+1)]

    for i in range(len(a)+1):
        dp[0][i]=i

    for j in range(len(b)+1):
        dp[j][0]=j
    #print(dp)
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                dp[j][i]=dp[j-1][i-1]
            else:
                dp[j][i]=min(dp[j-1][i-1],dp[j][i-1],dp[j-1][i])+1
    #print(dp)
    print(dp[len(b)][len(a)])