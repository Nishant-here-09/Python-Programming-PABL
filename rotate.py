class Solution:
    def rotate(self, arr):
        n = len(arr)
        
        if n == 0:
            return
        
        last = arr[-1]  
        
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        
        arr[0] = last
