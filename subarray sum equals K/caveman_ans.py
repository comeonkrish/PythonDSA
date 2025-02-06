class Solution:
    def subarraySum(self, nums, k: int) -> int:
    
        print("Original Array:", nums)

        prefix_sums_dict = {}
        prefix_sums = [0] * len(nums)

        prefix_sums_dict[0] = [nums[0]]
        prefix_sums[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sums[i] = nums[i] + prefix_sums[i-1]
            sum_till_i = prefix_sums[i]
            prefix_sums_dict[i] = [sum_till_i]
            j = i - 1
            temp = sum_till_i
            while j>=0:
                temp -= nums[j]
                prefix_sums_dict[i].append(temp)
                j-=1
   
        print(prefix_sums_dict) 

        # Iterate through the prefix_sums_dict
        for key, prefix_values in prefix_sums_dict.items():
            # Check if the target k exists in the list
            if k in prefix_values:
                # Find the index where k is found
                index_of_k = prefix_values.index(k)
                start_index = key  # Calculate the start index from the original array
                print(f"Subarray from index {start_index} to {key}: {nums[start_index:key+1]}")



#Example inputs
obj = Solution()
obj.subarraySum([1,1,1,2,3], 3)