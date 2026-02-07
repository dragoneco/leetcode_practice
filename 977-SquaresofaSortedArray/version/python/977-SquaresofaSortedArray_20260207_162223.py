# Last updated: 2026/2/7 16:22:23
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3         return sorted(x**2 for x in nums)