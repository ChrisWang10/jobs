"""
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

0     6       12
1   5 7    11 13
2 4   8 10
3     9

interval-2i,2i

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or len(s) <= numRows:
            return s
        interval = 2 * numRows - 2
        # 首行
        result = ''
        for i in range(0, len(s), interval):
            result += s[i]

        # 中间行
        for i in range(1, numRows - 1):
            result += s[i]
            j = i
            turn = 1
            while j < len(s):
                gap = interval - 2 * i if turn % 2 == 1 else 2 * i
                if j+gap >= len(s):
                    break
                result += s[j+gap]
                j += gap
                turn += 1

        # 尾行
        for i in range(numRows-1, len(s), interval):
            result += s[i]

        return result




so = Solution()
print(so.convert('PAYPALISHIRING', 4))
