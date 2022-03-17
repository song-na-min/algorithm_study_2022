
def div(arr):
    left,right=0,0
    for index,value in enumerate(arr):
        if value=="(":
            left+=1
        elif value==")":
            right+=1
        if left==right:
            return index
    return True
def is_ok(arr):
    count=0
    for i in arr:
        if i=='(':
            count+=1
        else:
            if count==0:
                return False
            count-=1
    return True
    """
    left,right=0,0
    for index,value in enumerate(arr):
        if value=="(":
            left+=1
        elif value==")":
            right+=1
        if left<right:
            return False
    return True 
    """
    
def to_ok(arr,answer):
    div_index=div(arr)
    u=arr[:div_index+1]
    v=arr[div_index+1:]
    print(u,v)
    if is_ok(u):
        answer=u+to_ok(v,answer)
    else:
        length=len(u)
        answer="("
        answer+=to_ok(v)
        answer+=")"
        for i in range(len(u)):
            if u[i]=="(":
                u[i]=")"
            else:
                u[i]="("
        answer+="".join(u)
    if len(v)!=0:
        to_ok(v,answer)
    return answer
def solution(p):
    answer = ''
    if p=='':
        return answer
    div_index=div(p)
    u=p[:div_index+1]
    v=p[div_index+1:]
    print(u,v)
    if is_ok(u):
        answer=u+solution(v)
    else:
        answer="("
        answer+=solution(v)
        answer+=")"
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=="(":
                u[i]=")"
            else:
                u[i]="("
        answer+="".join(u)
    #if len(v)!=0:
     #   solution(v)
    return answer