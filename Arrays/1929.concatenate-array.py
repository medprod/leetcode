class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(0,n):
            ans.append(nums[i])

        ans = ans + ans
        return ans