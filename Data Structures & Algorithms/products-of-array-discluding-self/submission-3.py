class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    prod *= nums[j]
            res[i] = prod

        return res        