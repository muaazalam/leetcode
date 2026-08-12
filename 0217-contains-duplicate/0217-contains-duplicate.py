class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        for n in nums:
            if n in a:
                return True
            a[n]=1
        return False