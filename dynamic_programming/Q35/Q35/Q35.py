
if __name__=="__main__":

    dp=[0]*30

    dp[1]=1
    dp[2]=2

    n=10
    count=3
    for i in range(3,1000):

        if i%2==0 and dp[i//2]!=0:
            #print(i,count)
            dp[i]=count
            count+=1
        elif i%3==0 and dp[i//3]!=0:
            #print(i,count)
            dp[i]=count
            count+=1
        elif i%5==0 and dp[i//5]!=0:
            #print(i,count)
            dp[i]=count
            count+=1
        if count==n+1:
            print(i)
            break
    #print(dp)

