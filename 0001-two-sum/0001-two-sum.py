class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        i=0
        for num in nums:
            temp=target-num
            if temp in a:
                return [a[temp],i]
            else:
                a[num]=i
            i+=1
    
                     
        