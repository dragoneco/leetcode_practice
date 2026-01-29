# Last updated: 2026/1/29 16:19:31
'''
用例子走一遍（最重要）

nums = [2, 7, 11, 15], target = 9

i=0, x=2

need = 9 - 2 = 7

seen 里有没有 7？没有

记录：seen[2] = 0
seen = {2: 0}

i=1, x=7

need = 9 - 7 = 2

seen 里有没有 2？有！seen[2] = 0

返回 [0, 1]

结束。
'''

1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        num_map={}
4
5        for key,num in enumerate(nums):
6
7            complement=target-num
8
9            if complement in num_map:
10                 
11                return [num_map[complement],key]
12
13            num_map[num]=key
14
15        return []
16            