class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            lenght = 1
            if num - 1 not in seen:
                start = num
                
                while (num + lenght) in seen:
                    lenght += 1
            longest = max(lenght, longest)
        return longest