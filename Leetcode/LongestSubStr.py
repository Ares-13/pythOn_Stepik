class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            letter = s[right]

            while letter in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(letter)
            max_len = max(max_len, right - left + 1)
    

        return max_len


s = "abcabcbb"
res = Solution()

print(res.lengthOfLongestSubstring(s))
