class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        for word in strs:
            freq_key = [0]*26
            for ch in word:
                freq_key[ord(ch) - ord('a')] += 1
            freq_dict[tuple(freq_key)].append(word)
        return list(freq_dict.values())