class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        nums = []
        seen = dict(sorted(seen.items(), key=lambda x:x[1], reverse=True))

        return list(seen.keys())[:k]

