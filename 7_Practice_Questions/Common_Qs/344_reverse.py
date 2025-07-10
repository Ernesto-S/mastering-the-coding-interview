# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

class Solution:
    def initial(s):
        reversed = []
        for i in range(len(s)-1,-1,-1):
            reversed.append(s[i])
        return reversed
    
    def twoPointers(s):
        start = 0
        end = len(s)-1
        while start<end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -=1
        return s
    

        

s = ["h","e","l","l","o"]
print(Solution.twoPointers(s))
