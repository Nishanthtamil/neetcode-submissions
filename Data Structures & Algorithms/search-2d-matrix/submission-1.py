class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,columns=len(matrix),len(matrix[0])
        low,high=0,rows*columns-1
        while low<=high:
            middle=low+(high-low)//2
            row,col=middle//columns,middle%columns
            if matrix[row][col]>target:
                high=middle-1
            elif matrix[row][col]<target:
                low=middle+1
            else:
                return True
        return False