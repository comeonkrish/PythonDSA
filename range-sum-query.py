class NumArray:
    def __init__(self, nums):
        """
        Initialize the NumArray object with the list of numbers and 
        compute the prefix sum array.
        """
        if not nums:  # Handle empty array case
            self.arr = []
            self.psum_arr = []
        else:
            self.arr = nums
            self.psum_arr = [0] * (len(self.arr) + 1)  
            
            # Compute prefix sum array
            for i in range(1, len(self.arr) + 1):
                self.psum_arr[i] = self.psum_arr[i - 1] + self.arr[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        """
        Return the sum of the elements of the array between indices left and right (inclusive).
        """
        # Check for valid range (left, right) within bounds
        if not (0 <= left <= right < len(self.arr)):
            raise ValueError("Invalid range. Make sure 0 <= left <= right < len(arr).")
        
        # Return the range sum using the precomputed prefix sum array
        return self.psum_arr[right + 1] - self.psum_arr[left]

# Example usage
obj1 = NumArray([1, 2, 3, 4])
print(obj1.arr)         # [1, 2, 3, 4]
print(obj1.psum_arr)    # [0, 1, 3, 6, 10]

param_1 = obj1.sumRange(2, 3)
print(param_1)          # 7 (3 + 4)

