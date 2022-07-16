from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        tmp = 0
        width = 0
        hight = 0

        for i in height:

            for j in range(len(height),height.index(i),-1):

                width = j-height.index(i)-1
                hight = min([i,height[j-1]])
                tmp = width*hight

                if tmp>max_area :
                    max_area=tmp
                else:
                    next

        return max_area

        
if __name__ == '__main__':
    
    sol = Solution()
    
    sol.maxArea(height=[1,2,3,4])
    sol.maxArea(height=[1,8,6,2,5,4,8,3,7])
    sol.maxArea(height=[1,1])
    sol.maxArea(height=[2,1])