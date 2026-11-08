class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        prev = -1

        for i in range(len(nums)-2):
            if prev > -1 and nums[prev] == nums[i]:
                continue
            
            j, k = i+1, len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
            prev = i

        return res

