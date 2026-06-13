class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        max_freq = max(seen.values())
        bucket  = [[] for i in range(max_freq + 1)]

        for num, freq in seen.items():
            bucket[freq].append(num)

        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


