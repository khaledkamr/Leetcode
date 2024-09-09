class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        Sum = 1
        for i in range(n):
            Sum *= nums[i]
            prefix[i] = Sum

        Sum = 1
        for i in range(n - 1, -1, -1):
            Sum *= nums[i]
            postfix[i] = Sum

        for i in range(n):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == n - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]

        return nums
