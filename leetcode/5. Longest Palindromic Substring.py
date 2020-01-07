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
        # Take each character as the imaginary center, and expand to determine whether it is a palindrome.
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
        """
        The above method does not use the palindrome information already known
        for example: a s d b d s k
        at this moment we know that b is the center of 's d b d s',
        then don't need to calculate d after b because we already know the radius of d before b according to symmetric
        characteristic of  Palindrome
        """

        def longestPalindrome(self, s: str) -> str:
            if len(s) <= 1:
                return s
            s = '$' + '#'.join(s) + '#'
            maxRight = 0
            maxCenter = 0
            radius = [0] * len(s)
            result = ''
            for i in range(len(s)):
                if len(s) - i <= maxRight - maxCenter:
                    break
                radius[i] = 1 if i >= maxRight else min(radius[2 * maxCenter - i], maxRight - i)

                while i - radius[i] >= 0 and i + radius[i] < len(s) and s[i - radius[i]] == s[i + radius[i]]:
                    radius[i] += 1

                if radius[i] > maxRight - maxCenter:
                    maxRight = radius[i] + i
                    maxCenter = i
                    result = s[i - radius[i] + 1:i + radius[i]]
            return result.replace('#', '')


s = Solution()
s.longestPalindrome('abcd')
