# Last updated: 2026/1/29 18:29:19
# indention problem
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if len(nums)==0:
4            return 0
5
6
7        numset=set(nums)
8        max_length=0
9        
10        for num in numset:
11            if num-1 not in numset:
12                currentnum=num  #assume 是第一个开始计算了
13                current_length=1
14
15                while (currentnum+1) in numset:  ##新的条件循环
16
17                    currentnum +=1
18                    current_length +=1
19
20            
21                max_length=max(max_length, current_length)
22        
23        return max_length