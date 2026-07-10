class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        res = []
        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char) - ord('a')] +=1
            key = tuple(key)
            if key in store:
                store[key].append(word)
            else:
                store[key] = [word]
        for group in store.values():
            res.append(group)
        return res