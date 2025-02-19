class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_map = {} # using a dict is better as the searching of elements happens in O(1)
        max_length = 0
        start = 0  # Start of the sliding window

        # i indicates the end of the window
        for i in range(n):
            # condition to check if the char i is pointing to has been seen before
            # and if it is inside the current window 
            if s[i] in char_map and char_map[s[i]] >= start:
                start = char_map[s[i]] + 1  # Move the start pointer to the right of last occurrence 
                                            # this reduces unnecessary comparisons  

            char_map[s[i]] = i  # Update the last seen index of the character
            max_length = max(max_length, i - start + 1)  # Update the max length

        return max_length

# Test the optimized solution
obj = Solution()
ans = obj.lengthOfLongestSubstring("pwwkew")
print(ans)
