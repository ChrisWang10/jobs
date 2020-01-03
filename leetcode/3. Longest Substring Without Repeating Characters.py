"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""


class Solution:
    """
    遍历字符串，
    """

    def new(self, s: str) -> int:
        result = 0
        D = dict()
        maxResult = 0
        for i in range(0, len(s)):
            if s[i] in D:
                maxResult = max(D[s[i]], maxResult)
            result = max(result, i - maxResult + 1)
            D[s[i]] = i + 1

        return result

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        record = {}
        max_length = 1
        cur_length = 1
        while len(s) > end >= start:
            if start == end:
                record[s[start]] = start
                end += 1
            elif s[end] not in record:
                record[s[end]] = end
                end += 1
                cur_length += 1
                if cur_length > max_length:
                    max_length = cur_length
                # end指向的位置的值之前访问过
            else:
                start = record[s[end]] + 1
                end = start
                record = {}
                cur_length = 1
        return max_length

    def review(self, s: str) -> int:
        result, cur_max = 0, 0
        record = dict()
        for i, c in enumerate(s):
            if c in record:
                cur_max = max(cur_max, record[c])
            result = max(result, i - cur_max + 1)
            record[c] = i + 1
        return result


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
