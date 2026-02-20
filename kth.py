class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()              # Sort the array
        return arr[k - 1]       # kth smallest element
