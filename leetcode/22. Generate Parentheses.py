"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def dfs(self, need_open, need_close, res, path, n):
        if need_close == 0 and need_open == 0:
            res.append(path)
            return
        if n >= need_open > 0:
            self.dfs(need_open - 1, need_close + 1, res, path + '(', n)
        if n >= need_close > 0:
            self.dfs(need_open, need_close - 1, res, path + ')', n)

    def generateParenthesis(self, n: int):
        res = []
        self.dfs(n, 0, res, '', n)
        print(res)


so = Solution()
so.generateParenthesis(3)