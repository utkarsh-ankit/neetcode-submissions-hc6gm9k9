class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=len(matrix)
        for i in range(c):
            if matrix[i][0]==target:
                return True
            elif matrix[i][0]< target and matrix[i+1][0]>target:
                l=0
                r=len(matrix[0])-1
                while l<r:
                    mid=(l+r)//2
                    if matrix[i][mid]<target:
                        l=mid
                    elif matrix[i][mid]>target:
                        r=mid
                    else:
                        return True
            else:
                return False
        # return False




        