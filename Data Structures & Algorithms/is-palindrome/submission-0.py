class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_A = ''.join(filter(str.isalnum, s)).lower()
        for i, ch in enumerate(str_A):
            j = len(str_A) - i - 1
            if ch != str_A[j]:
                return False
        return True