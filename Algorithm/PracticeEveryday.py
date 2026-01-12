#Insertion sort:
# seperate the sorted part of the list from the unsorted part and every element of the unsorted part is compared to the sorted part of the list:

arr= [10,2,5,11,4,2]

def insertionSort(arr):
    mergeArr = arr
    for i in range(1,len(mergeArr)):
        for j in range(0,i):
            if mergeArr[j]>mergeArr[i]:
                mergeArr[j],mergeArr[i] = mergeArr[i],mergeArr[j]

    print(f"After insertionSort: {mergeArr}")


#Selection Sort
#swap the smallest number of the array with the first element of the unsorted part of the array

def selectionSort(arr):
    #TODO every day:
    sorted = arr
    for i in range(len(sorted)-1):
        min = i
        for j in range(i+1,len(sorted)):
            if sorted[min]<sorted[j]:
                min = j
        sorted[min],sorted[i] = sorted[i],sorted[min]

    print(f"After selection sort is: {sorted}")


#swapping the current index and the next index to the correct order, iterate the entire list for each index in the list
def bubbleSort(arr):
    #Todo everyday
    sorted = arr
    for i in range(len(sorted)):
        for j in range(len(sorted)-i-1):
            if sorted[j+1]<sorted[j]:
                sorted[j+1],sorted[j] = sorted[j],sorted[j+1]
    
    print(f"After bubble sort : {sorted}")



def Recursion(n):
    print("Recursive behaviour")


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])


    return merge(left,right)
    
def merge(left,right):
    leftPointer = 0
    rightPointer = 0
    merged = []

    while len(left)>leftPointer and len(right)>rightPointer:
        if left[leftPointer]>right[rightPointer]:
            merged.append(left[leftPointer])
            leftPointer+=1
        elif right[rightPointer]>left[leftPointer]:
            merged.append(right[rightPointer])
            rightPointer+=1
        
    merged.extend(left[leftPointer:])
    merged.extend(right[rightPointer:])

    return merged



def recurBinarySearch(arr,n):
    #recursive method

    pass

    
def itiBinarySearch(arr,n):
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2

        if arr[mid] == n :
            return mid
        
        elif arr[mid]>n:
            right = mid-1
        
        elif arr[mid]<n:
            left = mid + 1
    
    return -1



    
if __name__ == "__main__":
    insertionSort(arr)
    selectionSort(arr)
    bubbleSort(arr)
    merged = mergeSort(arr)
    print(f"After merged sort: {merged}")

    # searching algorithm
    index = recurBinarySearch(arr,3)
    if not index:
        print(f"The number is not found")
    else:
        print(f"The number is found at index {index}")

    index = itiBinarySearch(merged,10)
    if index== -1:
        print(f"The number is not found")
    else:
        print(f"The number is found at index {index}")

