# implementing selection sort algorithm in Python

arr = [64, 25, 11, 22, 45]

def selection_sort(array):
    length = len(array)

    for first_pointer in range(length-1):
    # current index to enter (First pointer)
        min = first_pointer #Assuming the first index is the min
        for second_pointer in range(first_pointer+1,length): 
            if array[second_pointer]<array[min]:
                min = second_pointer # constantly updating the smallest pointer
        
        array[first_pointer], array[min] = array[min],array[first_pointer] # swapping 

    print(f"After sorting {array}")
            
if __name__ == "__main__":
    selection_sort(arr)
