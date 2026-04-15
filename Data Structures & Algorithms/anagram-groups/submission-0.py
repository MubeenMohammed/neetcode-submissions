class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo_dict = defaultdict(list)
        for s in strs:
            frequency_dict = [0] * 26
            for char in s:
                frequency_dict[ord(char) - ord("a")] += 1
            memo_dict[tuple(frequency_dict)].append(s)
        return memo_dict.values()

