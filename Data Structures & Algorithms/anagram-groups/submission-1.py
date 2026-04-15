class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use hashmap. 
        # For Keys use the list of frequency of each character (array of 26 values)
        # For values, use the words that match that key frequency
        # Since anagrams have the same frequency, this works out perfectly
        
        # Calculate the frequncy list of each string

        
        freq_dict =  {}
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            freq_str = str(freq)
            if freq_str in freq_dict:
                freq_dict[freq_str].append(s)
            else:
                freq_dict[freq_str] = [s]
        return list(freq_dict.values())