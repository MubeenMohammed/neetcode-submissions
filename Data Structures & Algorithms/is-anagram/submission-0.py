class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_memory = {}
        t_memory = {}
        for char in s:
            if char in s_memory:
                s_memory[char] += 1
            else:
                s_memory[char] = 1
        for char in t:
            if char in t_memory:
                t_memory[char] += 1
            else:
                t_memory[char] = 1
        for key in s_memory:
            if key not in t_memory:
                return False
            elif s_memory[key] != t_memory[key]:
                return False
        return True