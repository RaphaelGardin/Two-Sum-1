class Solution:
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, i in enumerate(nums):
            if hash.get(i) is not None:
                return[hash.get(i), idx]
            hash[target -i] = idx