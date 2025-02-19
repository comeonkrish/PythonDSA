class Solution:
    def isHappy(self, n: int) -> bool:

        def get_sum_of_squares(num):
            sum_squares = 0
            while num > 0:
                digit = num % 10
                sum_squares += digit ** 2
                num //= 10
            return sum_squares

        slow = n
        fast = get_sum_of_squares(n)
        
        while fast != 1 and slow != fast:
            slow = get_sum_of_squares(slow)  
            fast = get_sum_of_squares(get_sum_of_squares(fast))  
        
        return fast == 1

obj = Solution()
ans = obj.isHappy(23)
print(ans)  
