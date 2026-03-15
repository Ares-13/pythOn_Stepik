class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    output.extend([i, j])

        return output

nums = list(map(int, input().split()))
target = int(input())

res = Solution()
print(res.twoSum(nums, target))