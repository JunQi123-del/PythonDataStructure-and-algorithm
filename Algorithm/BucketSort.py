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
