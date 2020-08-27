class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        
        def recur(i , j):
            
            if i < 0 or j < 0 or i>R-1 or j>C-1 
            or image[i][j] == newColor or image[i][j] != oldColor:
                return
                
            
            image[i][j] = newColor
                
            
            recur(i+1, j)
            recur(i-1, j)
            recur(i, j+1)
            recur(i, j-1)
                
            
            
        recur(sr, sc)
        
        return image
