class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=len(matrix)-1
        for i in range(c):
            if matrix[i][-1]==target:
                return True
            elif matrix[i][-1]>target:
                l=0
                r=len(matrix[0])-1
                while l<r:
                    mid=(l+r)//2
                    if matrix[i][mid]>target:
                        r=mid
                    elif matrix[i][mid]<target:
                        l=mid
                    else:
                        return True
            else:
                return False
        # return False