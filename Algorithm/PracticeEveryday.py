#Insertion sort:
# seperate the sorted part of the list from the unsorted part and every element of the unsorted part is compared to the sorted part of the list:

arr= [10,2,5,11,4,2]

def insertionSort(arr):
    #TODO everyday
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    print(f"After insertion sort: {arr}")

#Selection Sort
#swap the smallest number of the array with the first element of the unsorted part of the array

def selectionSort(arr):
    #TODO every day:
    for i in range(len(arr)-1):
        min = i
        for j in range(i,len(arr)):
            if arr[min]>arr[j]:
                min = j

        arr[min],arr[i] = arr[i],arr[min]

    print(f"After Selection sort: {arr}")


#swapping the current index and the next index to the correct order, iterate the entire list for each index in the list
def bubbleSort(arr):
    #Todo everyday

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]

    print(f"after Bubble sort: {arr}")

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

    while leftPointer<len(left) and rightPointer<len(right):
        if left[leftPointer] < right[rightPointer]:
            merged.append(left[leftPointer])
            leftPointer+=1
        elif left[leftPointer] > right[rightPointer]:
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
    # insertionSort(arr)
    #selectionSort(arr)
    bubbleSort(arr)
    merged = mergeSort(arr)
    print(f"After merged sort: {merged}")

