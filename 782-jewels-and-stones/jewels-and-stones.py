class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        sumo = 0
        for i in stones:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for key, value in hashmap.items():
            if key in jewels:
                sumo += value
        return sumo