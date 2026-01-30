# Last updated: 2026/1/29 19:12:31
# 注意location 和 range 增加的次数速度不同的
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, i = 0, 1
        while i < len(nums) and nums[p] != 0:
            i += 1
            p += 1
        print(p)
        print(i)
        while i < len(nums):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
            i += 1

        