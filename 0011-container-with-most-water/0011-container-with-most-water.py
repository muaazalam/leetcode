class Solution:
    def maxArea(self, height: list[int]) -> int:
        head=0
        tail=len(height)-1
        maxarea=0

        while head<tail:
            currentarea=min(height[head],height[tail])*(tail-head)
            if maxarea<(currentarea):
                maxarea=currentarea
            
            if height[tail]>height[head]:
                head+=1
            else:
                tail-=1
        return maxarea
