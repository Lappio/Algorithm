from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        num_sum = 0
        for i in range(len(arr)):
            num_sum += arr[i]
            left = i - k + 1
            if(left<0):
                continue
            else:
                if(left-1>=0):
                    num_sum -= arr[left-1]
            if(num_sum/k >=threshold):
                ans += 1
        return ans
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。

# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。