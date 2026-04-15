class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create two hashmaps and compare them at the end
        if len(s) != len(t):
            return False
        
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for i in s:
            s_hash[i] += 1
        for i in t:
            t_hash[i] += 1
        
        for i in s_hash:
            if s_hash[i] != t_hash[i]:
                return False
        return True
        
            

