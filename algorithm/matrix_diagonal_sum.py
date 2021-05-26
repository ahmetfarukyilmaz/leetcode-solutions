
#https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        if len(mat)%2==1:
            sum-=mat[len(mat)//2][len(mat)//2]
        for i in range(len(mat)):
            sum+=mat[i][len(mat)-i-1]+mat[i][i]
        return sum