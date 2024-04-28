class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashTable = {}
        total = 0

        for num in nums:
            if num in hashTable:
                total += hashTable[num]
            
            hashTable[num] = hashTable.get(num, 0)+1
        
        return total

        #traditional approach:
        # total = 0

        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             total += 1
        # return total