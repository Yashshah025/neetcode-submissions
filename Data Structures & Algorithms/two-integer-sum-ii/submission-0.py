class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set(numbers)

        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in seen:
                return [i + 1, numbers.index(x) + 1]
            