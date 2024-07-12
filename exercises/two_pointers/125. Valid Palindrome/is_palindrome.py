class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(filter(str.isalnum,s.lower()))
        return False if s != " " and s != s[::-1] else True