class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1x = Counter(s1)
        for i in range(len(s2)):
            x = s2[i: i + len(s1)]
            xx = Counter(x)
            if s1x == xx:
                return True
        return False