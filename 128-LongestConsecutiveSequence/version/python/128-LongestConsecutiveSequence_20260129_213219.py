# Last updated: 2026/1/29 21:32:19
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right=0,len(height)-1
4        max_water=0
5
6        while left<right:
7
8            water=min(height[left],height[right])*(right-left)  ##这里已经开始每次循环了
9            max_water=max(water,max_water)
10
11
12            if height[left]<height[right]:
13                left+=1
14
15            elif height[left]>height[right]:
16                right-=1
17
18            else:
19                left +=1 
20                right -=1
21
22        return max_water
23
24            
25