class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        for i in range(0, len(A)):

            A[i].reverse()

            for j in range(0, len(A[i])):

                if A[i][j] == 0:
                    A[i][j] = 1

                else:
                    A[i][j] = 0

        return A