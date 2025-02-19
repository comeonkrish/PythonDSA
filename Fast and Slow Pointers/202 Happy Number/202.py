class Solution:
    def isHappy(self, n: int) -> bool:

        def get_sum_of_squares(num):
            sum_squares = 0
            while num > 0:
                digit = num % 10
                sum_squares += digit ** 2
                num //= 10
            return sum_squares
        
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

