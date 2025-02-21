class Solution:
    def dailyTemperatures(self, temperatures):

        n = len(temperatures)
        answer = [0] * n
        stack = []
    
        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                
                index = stack.pop()
                answer[index] = i - index

            stack.append(i)
    
        return answer


obj = Solution()
ans = obj.dailyTemperatures([73,74,75,71,69,72,76,73])
print(ans)        