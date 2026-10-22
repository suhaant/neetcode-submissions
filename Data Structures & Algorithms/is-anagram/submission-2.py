class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        
        for k in t:
            if k in hashmap and hashmap[k] > 0:
                hashmap[k] -= 1
            else:
                return False
        return True
