class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * (len(nums)+1) 
        suffixes = [1] * (len(nums)+1)

        for i in range(len(nums)-1, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i]
        
        for i in range(len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i]
        
        return [prefixes[i-1] * suffixes[i+1] for i in range(len(nums))]