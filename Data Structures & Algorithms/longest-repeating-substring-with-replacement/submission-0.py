class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Okay I have solution that might work which is using sliding window with two pointers
        # First find the longest substring which has same continous character like 'AAA'. We only need the length of this substring
        # Then you replace the characters infront and behind of this substring until k depletes.
        # Use this formula to calculate the final output
        # len(longest_continous_str) + min((len(s) - len(longest_continous_str)), k)
        # Here you take the minimum so that you are not crossing the len of the original string and adding new characters to it instead of just replacing it

        # So lets code this solution


        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res