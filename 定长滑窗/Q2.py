class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans_sum = 0 
        num_sum = 0
        for i in len(nums):
            num_sum += nums[i]
            
            left = i-k+1
            if(left<0):
                continue    #构造窗口
            else:
                if(left-1>=0):
                    num_sum -= nums[left-1]   #删去out值
            ans_sum = max(ans_sum,num_sum)
        return ans_sum/k

# 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

# 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

# 任何误差小于 10-5 的答案都将被视为正确答案。
# 注意数据的范围