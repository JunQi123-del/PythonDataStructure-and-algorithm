#Bucket sort is used on question that counts on frequency 
# Like Top K frequent
# 

Data = [3,2,4,3,3,2,1,1,4,4,4]

k = 2

def getKFrequentNumber():
    frequencyMap = {}

    for i in Data:
        frequencyMap[i] = frequencyMap.get(i,0)+1

    #Bucket sort:
    #create a list of list that is one size bigger than the original List

    freqList = [[] for _ in range(len(Data)+1)]
    # store the frequency as index and key as value
    for key,val in frequencyMap.items():
        freqList[val].append(key)

    result = []

    for i in range(len(freqList)-1,0,-1): # param in range = start, stop , step (Stop before 0 and deduct 1 every loop)
        for num in freqList[i]:
            result.append(num) # automatically skips list that is empyu 
            if len(result)==k:
                return result

if __name__ == "__main__":
    result = getKFrequentNumber()
    print(f"{result}")

#Step 1 
#Use map to map all the number in the list to their frequency in the list, this allows us to know the frequency of each occurence of the number
#But we do not know which number is the highest frequency against each other and we do not know which are the higgest number in the list

#step 2
# Use list to find out the higgest frequency to the number in the list (Using index as freqency)
# create empty lists in side a list where which = to length of actual list + 1 (You plus one to discount the 0 so you know exactly the length in human language)
# The index of the list inside = frequency, the val of the list = to the number in the dataset

#step 3 
#step take the val from the back of the list until length of the new list = to K 
