
if __name__=="__main__":

    n=input("s를 입력하세요\n")

    list_n=list(n)

    print(list_n)
    sum=0

    remove_list=[]
    for i in list_n:
        #print(i)
        if ord(i)<64:
            #print(i)
            num=int(i)
            sum=sum+num
            remove_list.append(i)

    list_n=[i for i in list_n if i not in remove_list]
    list_n.sort()
    list_n.append(str(sum))
    print(''.join(list_n))