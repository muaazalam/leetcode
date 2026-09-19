class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        head=0
        tail=len(numbers)-1

        while numbers[head]+numbers[tail] != target:
            if numbers[head]+numbers[tail]>target:
                tail-=1
            else:
                head+=1
            
        return [head+1, tail+1]


        