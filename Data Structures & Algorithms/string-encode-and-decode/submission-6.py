class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result = result + str(length) + "#" + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        # while(i < len(s)):
        #     start = i
        #     j = ''
        #     while s[start] != '#':
        #         start += 1
        #         j += s[start]
        #     start += 1
        #     end = start + int(j)
        #     temp = s[start: end]
        #     result.append(temp)
        #     i = end
        while i < len(s):
            start = i
            slen = ''
            while start < len(s) and s[start] != '#':
                slen = slen + s[start]
                start = start + 1
            print(slen)
            start += 1
            end = start + int(slen)
            result.append(s[start: end])
            i = end
        return result

