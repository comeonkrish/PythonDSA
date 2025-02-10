class Solution:
    def twoSum(self, numbers, target: int):
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left+=1
            else:
                right-=1

obj = Solution()
answer = obj.twoSum([2, 7, 11, 15], 9)
print(answer)
