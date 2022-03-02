

if __name__=="__main__":

    n=input("n을 입력하세요")
    #print(n)
    list_n=list(map(int,list(n)))

    a=0
    b=0
    length=len(list_n)
    for i in range(length//2):
        a+=list_n[i]
        b+=list_n[length-1-i]
    #print(a,b)
    if(a==b):
        print("LUCKY")
    else:
        print("READY")



    

