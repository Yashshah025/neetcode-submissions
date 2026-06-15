class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            x = target - numbers[i]
            if x in seen:
                return [seen[x] + 1, i + 1]

            seen[num] = i
            