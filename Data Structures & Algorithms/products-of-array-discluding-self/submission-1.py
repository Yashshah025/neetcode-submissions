class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        
        ans = [1] * len(nums)
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]
        for i in range(1, len(nums) - 1, 1):
            ans[i] = prefix[i - 1] * postfix[i+1]
        return ans
