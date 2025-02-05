class Solution:

    def findMaxLength(self,nums) -> int:
        self.barr = nums
        print(self.barr)

        tbarr = [1] * len(nums)

        print(tbarr)
        for i in range(len(nums)):
            if self.barr[i] == 0:
                tbarr[i] = -1
        print(tbarr)

        psum_tbarr = [0] * (len(tbarr)+1)

        for i in range(1, (len(tbarr)+1)):
            psum_tbarr[i] = psum_tbarr[i-1] + tbarr[i-1]

        print(psum_tbarr)

        for i in range(1,len(psum_tbarr)):
            if psum_tbarr[i] == 0:
                count = i

        ans = [0] * count

        for i in range(count):
            ans[i] = self.barr[i]

        print(ans)

obj = Solution()
obj.findMaxLength([0,1,1,1,0,0,1,0,1])



