class Solution:
    def search(self, nums, target):
        print(nums)

        left = 0
        right = len(nums) - 1

        while left<=right:

            mid = (left + right)//2

            if nums[mid] == target:
                return mid 
            
            # if left half is sorted
            if nums[left] <= nums[mid]:
                # if target lies in left half
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # if right half sorted
            else: 
                # if target lies in right half
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1            

obj = Solution()
ans = obj.search([4,5,6,7,0,1,2],0)
print(ans)
        