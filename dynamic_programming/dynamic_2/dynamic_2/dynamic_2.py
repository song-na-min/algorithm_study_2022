

if __name__=="__main__":
    # x가 5로 나누어떨어지면 5로 나누고
    #3 => /3
    #2 => /2
    #x => -1
    #=>1이 될 때 까지 최소 연산 수
    #x=int(input())

    # 1. 일단 dynamic인지는 모르겠는데 
    """
    count=0
    while x!=1:
        count+=1
        if x%5==0:
            print("5")
            x=x//5
        elif x%3==0:
            print("3")
            x=x//3
        elif x%2==0:
            x=x//2
            print("2")
        else:
            x=x-1
            print("1")
    print(count)
    """
    #이렇게 푸는 경우 최소의 결과가 나오지 않는다
    

    # top-down
    memo={}
    def top_down(i):
        print(i)
        #base case
        if i==1 or i==2 or i==3 or i==5:
            print("base case",i)
            return 1
        #memo에 없으면
        if i not in memo:
            #일단 -1을 한 것을 저장했다가
            memo[i]=top_down(i-1)+1
            #2로 나누어떨어지는 경우
            if i%2==0:
                m=top_down(i//2)+1
                #2로 나누어떨어진 경우가 더 작으면 교체
                if memo[i]>m:
                    memo[i]=m
            if i%3==0:
                m=top_down(i//3)+1
                if memo[i]>m:
                    memo[i]=m
            if i%5==0:
                m=top_down(i//5)+1
                if memo[i]>m:
                    memo[i]=m
        
        return memo[i]
    
    print(top_down(10))
    print(memo)

    #bottom-up
    d=[0]*30001
    def bottom_up(n):
        for i in range(2,n+1):
            d[i]=d[i-1]+1
            if i%2==0:
                d[i]=min(d[i],d[i//2]+1)
            if i%3==0:
                d[i]=min(d[i],d[i//3]+1)
            if i%5==0:
                d[i]=min(d[i],d[i//5]+1)
        print(d[n])
    bottom_up(6)