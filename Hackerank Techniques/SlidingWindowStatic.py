# This program demonstrate the sliding window technique neccessary to the Hackerrank questions 
#.
# In practice technical interviews in the future
# Question: Find out what is the highest sum of 3 consequtive number in the array
# k = 3 (3 consequetive number)

arr = [5,4,10,3,11,1,8,15,2,6]
k = 3
highestSum = pair = sum(arr[:k]) # until K 

for i in range(k,len(arr)):
    pair += arr[i]
    pair-=arr[i-k]
    highestSum = max(pair,highestSum)

print(f"The highest sum of three consequetive number is {highestSum}")

# Steps tracing
# First step = Find out the sum of the first pair of k numbers
# Set that as the higest sum initially 
# Create a loop that starts with number from k up till the length of array (incremented number I)
# add I to the sum of the first pair and remove index I - K from the sum 
#   - This will automatically remove the first index number of the array from the sum every time the window shifts (equivalent of every loop)
# compair the highest Sum to the sum of the pair and choose the highest of those