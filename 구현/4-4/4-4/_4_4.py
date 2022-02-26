

if __name__=="__main__":

    n,m=map(int, input().split())

    a,b,d=map(int, input().split())

    mylist=[list(map(int, input().split())) for _ in range(n)]

    #print(mylist)

    count=1

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    mylist[b][a]=-1
    while(True):
        end=1
        for i in range(5):
            #print(a+dx[(i+d)%4],b+dy[(i+d)%4])
            if i==4:
                a=a-dx[(d+i)%4]
                b=b-dy[(d+i)%4]
                print(a,b)
                if mylist[a][b]==-1:
                    end=0
            if(mylist[a+dx[(i+d)%4]][b+dy[(i+d)%4]]==0 and 0<b+dy[(i+d)%4]<n and 0<a+dx[(i+d)%4]<m):
                #print(mylist[a+dx[(i+d)%4]][b+dy[(i+d)%4]])
                print(i)
                
                a=a+dx[(i+d)%4]
                b=b+dy[(i+d)%4]
                mylist[a][b]=-1
                #print(a,b)
                d=(i+d)%4
                count+=1
                end=0
                print(mylist)
                print(d)
                break
            
        if(end==1):
            print(mylist)
            break
    print(count)

             

