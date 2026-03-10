# selection sort practice
# selection sort try to find the smallest number from the pointer to the end of the array 

array = [1,3,54,43,2,5]

def selectionSort(arr):
    for i in range(len(arr)):
        min = i # keep the index of the first element of the unsorted part
        flag=0
        for j in range(i,len(array)):
            if arr[j]<arr[min]:
                min = j # replace index of the element smaller than min everytime
                flag=1 
        if flag==1:
            arr[i],arr[min] = arr[min],arr[i]
        
    print(f"After selection sort: {arr}")


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    print(f"After bubble sort: {arr}")


if __name__=="__main__":
    # selectionSort(array)
    bubbleSort(array)