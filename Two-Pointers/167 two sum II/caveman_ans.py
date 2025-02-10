class Solution:
    def twoSum(self, numbers, target: int):
        n = len(numbers)

        left = 0
        right = n - 1

        for i in range(n):
            if (numbers[left] + numbers[right] == target):
                return ([left+1, right+1])
            elif (numbers[left] + numbers[right] > target):
                right -= 1
            else:
                left += 1
        
obj = Solution()
answer = obj.twoSum([2,7,11,15], 9)
print(answer)


        