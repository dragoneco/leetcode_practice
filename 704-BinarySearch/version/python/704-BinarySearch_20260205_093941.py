# Last updated: 2026/2/5 09:39:41
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left=0 
4        right=len(nums)-1
5
6    
7
8      
9
10        while left<=right:
11            mid=int((left+right)/2)
12
13            if nums[mid]<target:
14
15                left=mid+1
16
17        
18
19            elif nums[mid]>target:
20
21                right=mid-1
22
23            else: 
24                return mid
25
26
27        return -1
28
29
30
31
32
33