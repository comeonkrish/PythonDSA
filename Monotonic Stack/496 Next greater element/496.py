class Solution:
    def nextGreaterElement(self, nums1, nums2):

        nums1.reverse()

        ans = []

        while nums1:
            a = nums1.pop()
            # print(a)
            flag = False
            for i in range(len(nums2)):
                if a == nums2[i]:
                    # print(f"found: {a}")
                    flag = True

                if flag and nums2[i] > a:
                    # print(f"found greater element {nums2[i]}")
                    ans.append(nums2[i])
                    break

                if flag and i == (len(nums2) - 1):
                    ans.append(-1)
            
            # print(ans)

        return ans

obj = Solution()
answer = obj.nextGreaterElement([4,1,2], [1,3,4,2])
print(answer)
        