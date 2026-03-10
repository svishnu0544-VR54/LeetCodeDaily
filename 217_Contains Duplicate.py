'''
Brute Force approach:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            j=i+1
            for j in range(i+1, length):
                if nums[i] == nums[j]:
                    return True
        return False
'''
'''
Sorting Approach:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = nums.copy()
        numbers.sort()
        for i in range(1, len(numbers)-1):
            if numbers[i-1] == numbers[i]:
                return True
        return False
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for number in nums:
            if number in visited:
                return True
            visited.add(number)
        return False