class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            mem[sorted_s].append(s)
        return list(mem.values())
 