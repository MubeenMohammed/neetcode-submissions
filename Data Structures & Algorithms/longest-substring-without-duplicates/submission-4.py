class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Lets first try the brute force way
        if len(s) == 0:
            return 0 
        temp = ''
        res = 1
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+ 1, len(s)):
                print(temp)
                if s[j] not in temp:
                    temp += s[j]
                    res = max(res, len(temp))
                else:
                    break
        return res