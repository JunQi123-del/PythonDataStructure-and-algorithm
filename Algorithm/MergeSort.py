#Practicing merge sort
#Divide and conqure and algoritm 

arr = [43,2,44,4,1,56,0]

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left = mergeSort(arr[mid:])
        right = mergeSort(arr[:mid])

        return merge(left,right)
    
def merge(left,right):
    merged = []
    leftPointer = 0
    rightPointer = 0

    while leftPointer<len(left) and rightPointer<len(right):
        if left[leftPointer]<right[rightPointer]:
            merged.append(left[leftPointer])
            leftPointer+=1
        elif left[leftPointer]>right[rightPointer]:
            merged.append(right[rightPointer])
            rightPointer+=1
        else:
            merged.append(left[leftPointer])
            merged.append(right[rightPointer])
            leftPointer+=1
            rightPointer+=1

    merged.extend(left[leftPointer:])
    merged.extend(right[rightPointer:])

    return merged

if __name__ == "__main__":
    merged = merge_sort(arr)
    print(f"After merged sorting {merged}")