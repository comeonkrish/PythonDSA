class Solution:

    def findMaxLength(self, nums) -> int:
        num_array = nums
        print("Original Array:", num_array)

        # Generate modified array where 0 is replaced with -1
        modified_array = [1 if num == 1 else -1 for num in num_array]
        print("Modified Array:", modified_array)

        # Calculate prefix sum array
        prefix_sum = [0] * (len(modified_array) + 1)

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + modified_array[i - 1]

        print("Prefix Sum Array:", prefix_sum)

        # Find the index where the prefix sum first equals 0
        max_length_index = 0
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] == 0:
                max_length_index = i

        # Generate subarray of maximum length
        subarray = [num_array[i] for i in range(max_length_index)]

        print(f"Subarray of Maximum Length with equal 0s and 1s:", subarray)

# Example usage
obj = Solution()
obj.findMaxLength([0, 1, 1, 1, 0, 0, 1, 0, 1])
