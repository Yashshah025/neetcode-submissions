class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        cnt = 0
        l = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            cnt = max(cnt, len(seen))
        return cnt