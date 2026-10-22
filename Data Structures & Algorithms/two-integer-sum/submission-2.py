class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[comp], i]

