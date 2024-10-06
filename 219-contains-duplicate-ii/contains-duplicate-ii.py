class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, j in enumerate(nums):
            if j not in hashmap:
                hashmap[j] = i
            else:
                if abs(i - hashmap[j]) <= k:
                    return True
                hashmap[j] = i
        return False