class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(s)
        n = len(s)

        substring = []
        seen_chars = []
        maxlength = []

        start = 0
        i = 0

        while start < n:

            if (n-start) in maxlength:
                break
            elif i < n and s[i] not in seen_chars:
                substring = s[start:(i+1)]
                # print(substring)
                seen_chars.append(s[i])
                maxlength.append(len(substring))

                i += 1
            else:
                start += 1
                i=start
                seen_chars=[]

        return max(maxlength) if maxlength else 0

obj = Solution()
ans = obj.lengthOfLongestSubstring("aabbcddgghrkkk")
print(ans)