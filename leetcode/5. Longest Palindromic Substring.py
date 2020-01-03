"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


class Solution:
    def is_palindrome(self, substring):
        return substring == substring[::-1]

    def longestPalindrome(self, s: str) -> str:
        # $#b#a#b#, $#a#b#b#a#
        result, longest_radius = '', 0
        s = '$' + '#'.join(s) + '#'
        # 以每个字符为假想中心，进行扩展判断是否是回文串
        print(s)
        for i, c in enumerate(s):
            mid, radius = i, 1
            while (mid - radius) >= 0 and (mid + radius) < len(s):
                if self.is_palindrome(s[mid - radius:mid + radius + 1]):
                    radius += 1
                else:
                    break
            if radius > longest_radius:
                longest_radius = radius
                result = s[mid - radius + 1:mid + radius]
        result = ''.join(result.split('#'))
        return result

    def longestPalindrome_new(self, s: str) -> str:


s = Solution()
s.longestPalindrome('abcd')
