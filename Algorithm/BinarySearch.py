arr = [2, 3, 4, 10, 40]

#Eventujally the found would fall on the mid
def binarySearch(arr,n):
     mid = len(arr)//2

     if arr[mid] == n:
          return True
     elif arr[mid] != n and len(arr)==1:
          return False
     elif arr[mid]>n:
          return binarySearch(arr[:mid],n)
     elif arr[mid]<n:
          return binarySearch(arr[mid:],n)
     
def binarySearchIterative(arr,n):
     #while loop implementation
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2

        if arr[mid] == n:
            return mid
        elif arr[mid]<n:
            left = mid +1
        elif arr[mid]>n:
             right = mid-1
    return -1
        
        
        
        

    
if __name__ == "__main__":
    #  found = binarySearch(arr,5)
    found = binarySearchIterative(arr,5)
    if found == -1:
        print(f"The number is not found")
    else:
         print(f"The number is found in index {found}")



