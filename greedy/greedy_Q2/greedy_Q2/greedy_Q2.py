
import sys
#2. 곱하기 혹은 더하기

if __name__=="__main__":
    # 문자열 배열 원소의 곱
    # https://shoark7.github.io/programming/algorithm/3ways-to-get-multiplication-in-a-list-in-python
    # 리스트 요소를 변경
    # https://www.delftstack.com/ko/howto/python/python-list-replace-element/
    s=input("S을 입력하세요:\n")

    str_list=list(s)

    # 0인 것들을 1로 변경
    for index,value in enumerate(str_list):
        if value == '0':
            str_list[index]=1
    #print(str_list)

    # 문자열 배열 그대로 곱하기
    result= eval('*'.join([str(n) for n in str_list]))

    print(result)
