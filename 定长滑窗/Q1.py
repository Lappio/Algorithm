class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):  # 枚举窗口右端点 i
            # 1. 右端点进入窗口
            if c in "aeiou":
                vowel += 1

            left = i - k + 1  # 窗口左端点
            if left < 0:  # 窗口大小不足 k，尚未形成第一个窗口
                continue

            # 2. 更新答案
            ans = max(ans, vowel)

            # 3. 左端点离开窗口，为下一个循环做准备
            if s[left] in "aeiou":
                vowel -= 1
        return ans
    # 第一道题!
#给你字符串 s 和整数 k 。
# 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
# 英文中的 元音字母 为（a, e, i, o, u）。