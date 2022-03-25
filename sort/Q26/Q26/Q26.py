from queue import PriorityQueue
if __name__=="__main__":

    n=3
    arr=[10,20,40]

    que=PriorityQueue()

    min=0

    for i in arr:
        que.put(i)

    while que.qsize()!=1:
        #작은 묶음 2개를 가져와서
        a=que.get()
        b=que.get()
        #비교 횟수를 더하고
        min+=a+b
        #다시 큐에 넣기
        que.put(a+b)
    print(min)
    