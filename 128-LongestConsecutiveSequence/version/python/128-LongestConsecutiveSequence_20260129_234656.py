# Last updated: 2026/1/29 23:46:56
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        result=[]
5        n=len(nums)
6
7        for i in range(n-2):
8
9            if nums[i]>0:
10                break
11            if i>0 and nums[i]==nums[i-1]:
12                continue 
13            
14            left=i+1
15            right=n-1
16
17            while left <right:
18
19                current_sum=nums[i]+nums[left]+nums[right]
20
21                if current_sum==0:
22
23                    result.append([nums[i],nums[left],nums[right]])
24
25                    while left <right and nums[left]==nums[left+1]:
26                        left +=1
27
28                    while left <right and nums[right]==nums[right-1]:
29                        right -=1
30
31                    right-=1
32                    left+=1
33                elif current_sum<0:
34                    left+=1
35                else:
36                    right-=1
37
38
39        return result
40
41        