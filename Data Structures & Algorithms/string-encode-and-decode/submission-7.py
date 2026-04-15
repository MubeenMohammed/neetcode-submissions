class Solution:

    def encode(self, strs: List[str]) -> str:
        # To track the length of each string we put the length of the string and a demlimiter like "#" to differenciate between one string from another
        e_s = ''
        for s in strs:
            len_s = len(s)
            e_s += str(len_s) + '#' + s
        return e_s

    def decode(self, s: str) -> List[str]:
        # To decode the encoded string first get the length of string which is int value until # appears
        # Convert that length of forward characters to string and add it to result array
        # Do this until you hit the end of the encoded string
        res = []
        i = 0
        while i < len(s):
            start = i
            s_len = ''
            while start < len(s) and s[start] != '#':
                s_len += s[start]
                start += 1
            start += 1
            end = start + int(s_len)
            d_s = s[start:end]
            res.append(d_s)
            i = end
        return res