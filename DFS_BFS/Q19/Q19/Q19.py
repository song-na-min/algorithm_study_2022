
from itertools import permutations

if __name__=="__main__":
    n=6
    arr=[1,2,3,4,5,6]
    cal=[2,1,1,1]
    calcul=[]
    min,max=9999,0
    
    cal_String=["+","-","*","//"]
    # 0:+ , 1:- , 2:*, 3:// => 총 n-1개

    # 연산자를 개수별로 리스트(string)형태로
    for i in range(4):
        for j in range(cal[i]):
            calcul.append(cal_String[i])
    #print(calcul)

    # 연산자 순열
    calpermutation=list(permutations(calcul,n-1))

    stack_arr=list()

    for cal_list in calpermutation:
        ##초기화
        result=0
        #스택에 거꾸로 넣기 (stack을 사용하기 때문에)
        for i in reversed(range(n)):
            stack_arr.append(arr[i])
        #print("-----------------------")
        #print(cal_list)

        #모든 순열을 확인
        for i in cal_list:
            #숫자를 stack에서 하나씩 빼서
            a=stack_arr.pop()
            b=stack_arr.pop()
            #단 나누기연산은 첫 수를 절댓값으로 하도록
            if i=="//":
                a=abs(a)
            #연산 https://www.delftstack.com/ko/howto/python/python-list-replace-element/
            result=eval(str(a)+i+str(b))
            #print(result)
            #print("{}{}{}={}".format(a,i,b,result))

            #계산한 값을 stack에 push
            stack_arr.append(result)
        #최소, 최대 검사
        if result<min:
            min=result
        if result>max:
            max=result

        #print(result)
        #print(min,max)
    print(min,max)

