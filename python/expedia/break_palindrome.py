

class Solution:

    def breakPalindrome(self, str):
        n = len(str)
        for i in range(n//2):
            if str[i] != 'a':
                return str[:i] + 'a' + str[i + 1:]
        return "IMPOSSIBLE"

if __name__ == '__main__':
    solu = Solution()
    print(solu.breakPalindrome("bab"))
    print(solu.breakPalindrome("acca"))
    print(solu.breakPalindrome("bbbb"))
    print(solu.breakPalindrome("aaaa"))