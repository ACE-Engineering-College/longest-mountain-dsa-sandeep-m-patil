class Solution:
    def longestMountain(self, arr):
        n = len(arr)
        if n < 3:
            return 0  # A mountain must have at least 3 elements

        longest = 0
        
        for i in range(1, n - 1):
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1

                # Move left pointer downwards
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Move right pointer downwards
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Calculate mountain length
                mountain_length = right - left + 1
                longest = max(longest, mountain_length)

        return longest
