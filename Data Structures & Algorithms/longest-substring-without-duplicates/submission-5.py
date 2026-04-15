class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        charSet = set()
        res = 0
        count = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[count])
                count += 1
            charSet.add(s[i])
            res = max(res, i - count + 1)
        return res