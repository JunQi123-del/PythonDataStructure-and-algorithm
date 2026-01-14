# This program belows solves the problem of finding the longest or shortest subcomponenet of a string or array
# This is to practice for technical interview for hacker rank questions 
# Problem Finding the smallest subarray with a sum greater than or equal to a target value.

target = 20

arr = [5,10,4,3,12,10,1]

current = 0
left = 0
smallest = float("inf") #Infinity
 
for right in range(len(arr)):
    current+=arr[right]

    while current>=target:
        smallest = min(smallest,right-left+1)
        current-=arr[left]
        left+=1

print(f"The smallest sub array that is equal or greater than target is {smallest}")


#Steps Tracing:
#First set the target you want to be bigger or equal to
# Second: Set the smallest variable to infinity - reason is because it needs to be overridden by the next number and you cannot put 0 or 
# a random number because you are unsure how long the window is going to be extended until it is greater.
#Third once hit, check the window size if its smaller than the recorded smallest window size then minus the left pointer index of the window from the sum
# Then increment left pointer by 1 everytime