class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        largest = sorted(nums)[-1]
        #return set(range(1, largest+1)) - set(nums)
        return set(range(1, len(nums) + 1)) - set(nums)
