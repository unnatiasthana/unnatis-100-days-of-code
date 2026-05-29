# 3300. Minimum Element After Replacement With Digit Sum

# Hint
# You are given an integer array nums.

# You replace each element in nums with the sum of its digits.

# Return the minimum element in nums after all replacements.


# Example 1:

# Input: nums = [10,12,13,14]

# Output: 1

# Explanation:

# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in nums :
            s=0
            while i>0:
                r=i%10
                s=s+r
                i=i//10
            arr.append(s)
        return min(arr)
                
        

