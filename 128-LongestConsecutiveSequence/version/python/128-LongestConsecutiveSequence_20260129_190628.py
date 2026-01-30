# Last updated: 2026/1/29 19:06:28
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        location=0
7        for i in range(len(nums)):
8
9            if nums[i] !=0:
10                nums[location],nums[i]=nums[i],nums[location]
11
12                location +=1
13
14
15
16                