class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            if (numbers[left] + numbers[right]) == target:
                return [left+1, right+1]
            elif (numbers[left] + numbers[right]) < target:
                temp = left
                while (numbers[temp] + numbers[right]) < target and temp+1 < right:
                    temp += 1
                if numbers[temp] + numbers[right] != target:
                    right -= 1
                    while numbers[right] == numbers[right+1]:
                        right -= 1
                    continue
                left = temp
            else:
                temp = right
                while (numbers[left] + numbers[temp]) > target and temp-1 > left:
                    temp -= 1
                if numbers[left] + numbers[temp] != target:
                    left += 1
                    while numbers[left] == numbers[left-1]:
                        left += 1
                    continue
                right = temp
                        