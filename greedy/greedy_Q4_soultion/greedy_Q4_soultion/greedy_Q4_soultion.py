

if __name__=="__main__":

    n=int(input())

    data=list(map(int,input().split()))
    data.sort()

    target=1
    for x in data:
        print("target=")
        print(target)
        print("x=")
        print(x)
        if target<x:
            break
        target+=x

    print(target)