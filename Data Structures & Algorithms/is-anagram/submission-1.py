class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_mem = {}
        t_mem = {}
        for char in s:
            if char in s_mem:
                s_mem[char] += 1
            else:
                s_mem[char] = 1
        for char in t:
            if char in t_mem:
                t_mem[char] += 1
            else:
                t_mem[char] = 1
        print(s_mem, t_mem)
        for char in s_mem:
            if char not in t_mem:
                return False
            if s_mem[char] != t_mem[char]:
                return False
        return True