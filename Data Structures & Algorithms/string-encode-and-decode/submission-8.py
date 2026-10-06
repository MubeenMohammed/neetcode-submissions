class Solution:

    def encode(self, strs: List[str]) -> str:
        # One naive implementation is to add a unique separator between each of the string in the list
        # But there is always a possibility of that unique separator appearing as one of the strings/part of the string in the list
        # Instead with separator, also store a number which is length of next string so that you know where to divide the encoded
        # string when you decode it
        # Example ["Hello, World"] so encoded string will become 5!*!Hello5!*!World
        # When you decode this first you loop through the encoded string, try to figure out the length of the first string
        # You get that by collecting the characters until you find our unique separator which is !*! then you convert whatever you
        # collected as a int which is 5 here 
        # Then you collect the first 5 characters after our unique separator !*! which is Hello here which is our first string in the
        # list
        # You continue this until you are at the end of the string
        unique_sep = '!*!'
        encoded_str = ''
        for s in strs:
            encoded_str = encoded_str + str(len(s)) + unique_sep + s
        return encoded_str


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        l = ''
        while(i < len(s)):
            if s[i:i+3] == '!*!':
                start = i + 3
                end = start + int(l)
                res.append(s[start: end])
                l = ''
                i = end
            else:
                l = l + s[i]
                i += 1
        return res
