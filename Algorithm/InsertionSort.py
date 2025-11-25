arr = [13, 25, 11, 1, 45]

def InsertionSort(array):
    sorted_index = 0
    for first_pointer in range(1,len(array)):
        #unsorted portion
        for second_pointer in range(sorted_index,first_pointer):
            #sorted Portion
            if array[second_pointer] > array[first_pointer]:
                temp = array[second_pointer]
                array[second_pointer] = array[first_pointer]
                array[first_pointer] = temp # overwriting the comparing string 

    print(f"After insertion sort: {array}")

        


if __name__ == "__main__":
    InsertionSort(arr)