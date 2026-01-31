# Last updated: 2026/1/30 19:02:25
'''
你这段代码是在做 “把所有非 0 的元素按原顺序挪到数组前面”（典型的 Move Zeroes 思路）。关键点就是：

location 表示 下一个“非 0 应该放的位置”（也就是“非 0 区”的末尾）

遍历 i 的时候：

如果 nums[i] != 0：就把它换到 location 上，然后 location += 1

如果 nums[i] == 0：什么也不做，继续往后扫

你问的：nums[i] == 0 时会怎样？

答案：不会进入 if，所以不会交换，location 也不会变。

也就是说：

这个 0 先“留在原地”，等后面遇到非 0 的时候，那个非 0 会被交换到前面来，0 可能被换到后面去。
'''

1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        location=0
7
8        for  i in range(len(nums)):
9
10            if nums[i] !=0:
11
12                nums[location],nums[i]=nums[i],nums[location]
13
14                location +=1