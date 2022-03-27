
def binary_search(arr,m,start,end):
    
    while start<=end:
        
        mid=(start+end)//2
        print(start,mid,end)
        length=0
        for i in arr:
            if i-mid>0:
                length+=i-mid
        if length==m:
            return mid
        elif length>m:
            start=mid+1
        else:
            end=mid-1

if __name__=="__main__":
    n,m=4,6
    input_data=[19,15,10,17]

    input_data.sort()

    #이걸 binary search로?

    print(binary_search(input_data,m,0,input_data[-1]))
