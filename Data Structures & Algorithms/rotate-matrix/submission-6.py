class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #my appraoch, first traspose then flip from left to right(mirror iamge)
        n=len(matrix)

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for k in range(n):
            matrix[k].reverse() 

