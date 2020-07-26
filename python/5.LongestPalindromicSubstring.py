class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLength = 0
        end = 0
        begin = 0
        for idx in range(len(s) - 1):
            length1 = self.getPalindromicLength(s, idx, idx)
            length2 = self.getPalindromicLength(s, idx, idx + 1)
            if max(length1, length2) > end - begin + 1:
                if length1 > length2:
                    begin, end = idx - (length1 - 1) / 2, idx + (length1 - 1) / 2
                else:
                    begin, end = idx - (length2)/2 + 1, idx + (length2)/ 2
        # print(begin, end)
        return s[int(begin):int(end + 1)]

    def getPalindromicLength(self, string, left, right):
        idx = 0
        length = 0
        if left == right:
            left -= 1
            right += 1

        while left >= 0 and right < len(string) and string[left] == string[right]:
            length = right - left + 1
            left -= 1
            right += 1

        return length
