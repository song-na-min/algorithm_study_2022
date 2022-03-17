
#https://latte-is-horse.tistory.com/197
#https://freedeveloper.tistory.com/377

# 가장 일반적인 퀵 정렬
def quick_sort(array, start, end):
    if start >= end: return # 원소가 1개인 경우
    pivot = start # 피벗은 첫 요소
    left, right = start + 1, end
    print("pivot={}".format(array[pivot]))
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        print("left,right={},{}".format(left,right))
        if left > right: # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
            print("swap pivot right {} and {}".format(array[right],array[pivot]))
        else: # 엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
            print("swap right,left {} and {}".format(array[left],array[right]))
    print(array[start:right],array[right],array[right+1:end+1])
    print("----------")
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    return array

# 파이썬의 장점을 살린 퀵 정렬
def quick_sort_python(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array
    
    pivot, tail = array[0], array[1:]
    
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    
    return quick_sort_python(leftSide) + [pivot] + quick_sort_python(rightSide)

if __name__=="__main__":
    arr=[50,47,5,13,36,34,31,24,11,17]

    sorted_arr=quick_sort(arr,0,len(arr)-1)

    print("sorted")
    print(sorted_arr)

    python_arr=quick_sort_python(arr)
    print("sorted")
    print(python_arr)