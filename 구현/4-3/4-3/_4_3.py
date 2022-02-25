

if __name__=="__main__":
    
    start=input()

    col=int(ord(start[0]))-int(ord('a'))+1
    row=int(start[1])

    print(start)

    step=[(-1,-2),(1,-2),(1,2),(-1,2),(-2,-1),(2,-1),(2,1),(-2,1)]
    count=0
    for x,y in step:
        if (0<col+x<9) and (0<row+y<9):
            count=count+1

    print(count)