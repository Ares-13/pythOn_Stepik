class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l, max_r = 0, 0  # находим границы макс.палиндрома

        def max_pal_around_cen(l,r):
            nonlocal max_l, max_r
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l) > (max_r - max_l):
                    max_l, max_r = l, r  
                l -= 1
                r += 1

        for i in range(len(s)):        # проходимся по строке (индексы)
            max_pal_around_cen(i, i)   # для нечётной длины
            max_pal_around_cen(i, i+1) # для чётной длины

        return s[max_l:max_r+1]

s = input()
obj = Solution()
print(obj.longestPalindrome(s))
