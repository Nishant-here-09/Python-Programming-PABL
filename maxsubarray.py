class Solution:
    def maxSubArraySum(self, arr):
        current_sum = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):
            # Either extend the previous subarray or start new
            current_sum = max(arr[i], current_sum + arr[i])
            
            # Update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
