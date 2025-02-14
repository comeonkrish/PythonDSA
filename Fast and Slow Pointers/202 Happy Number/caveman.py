class Solution:
    def isHappy(self, n: int) -> bool:

        def get_sum_of_squares(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        seen = set()  
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_sum_of_squares(n)
        
        return True

obj = Solution()
ans = obj.isHappy(19)
print(ans)

