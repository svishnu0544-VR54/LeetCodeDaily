'''
Brute Force Method

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
'''

#One pass Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()

        for i in range(len(nums)-1, -1, -1):
            if target - nums[i] in hash:
                return [i, hash[target-nums[i]]]
            hash[nums[i]] = i
        
        return []