class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}
        for i in s:
            if i in s_hashmap:
                s_hashmap[i] += 1
            else:
                s_hashmap[i] = 1
        for j in t:
            if j in t_hashmap:
                t_hashmap[j] += 1
            else:
                t_hashmap[j] = 1
        for k in s_hashmap:
            if k not in t_hashmap or (s_hashmap[k] != t_hashmap[k]):
                return False
        return True