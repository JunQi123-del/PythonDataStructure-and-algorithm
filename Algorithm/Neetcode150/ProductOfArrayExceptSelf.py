from typing import List
#Neetcode medium 
# find the product of all the number in the array except self

# The solution is to find the prefix of all the left multiplication of the I index 

nums = [2,4,5,7,12,23]

def getProductsExceptSelf(nums:List[int]) -> List[int]:

    result = [1]*len(nums)

    prefix = 1
    postfix = 1

    # find the prefix product except self
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    #find the post fix from right to left except self 
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix*=nums[i]
    
    print(f"{result}")


if __name__ == "__main__":
    getProductsExceptSelf(nums)