class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        count=0

        for num in nums:
            a=target -num
            
            if a in dict1:
                return [dict1[a], count]
            dict1[num]=count
            count+=1
        return False
    
                     
        