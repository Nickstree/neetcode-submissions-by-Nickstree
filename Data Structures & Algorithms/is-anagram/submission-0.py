class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_dict = {}
        for chr in s:
            check_dict[chr] = check_dict.get(chr, 0) + 1
        for chr in t:
            check_dict[chr] = check_dict.get(chr, 0) - 1
        for v in check_dict.values():
            if v != 0:
                return False
        return True