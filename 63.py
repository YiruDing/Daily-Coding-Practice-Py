# This problem was asked by Microsoft.

# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.


# https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.geeksforgeeks.org%2Fsearch-a-word-in-a-2d-grid-of-characters%2F%3Ffbclid%3DIwAR2fpfRq-wV2jQy5mouu0f_PIv8qFBLxWFJtAhvWQPHmAfMcJapYS4uM9kM&h=AT2P-eMBzhJNfZcABpq35Erv7r1HmUgAIp9tlcEsvG4y3Vdtwcm92hXAG3ZhsikmfWD-0zA4FrCJyL4eA_M8tjHfx0n0HrSGF4A4ZtXAkJrK3C3kVOthxQY1XMUtyVy0sEQV_2hibnU
class GFG:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1,0],[1,0],[1,1],[1,-1],[-1,-1],[-1,1],[0,1],[0,-1]]
    
    def search2D(self,grid,row,col,word):
        if grid[row][col] != word[0]:
            return False
        for x,y in self.dir:
            rd,cd = row + x,col + y
            flag = True

            for k in range(1,len(word)):
                if (0 <= rd < self.R and 
                    0 <= cd < self.C and
                    word[k] == grid[rd][cd]):
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
            if flag:
                return True
        return False
    
    def patternSearch(self,grid,word):
        self.R = len(grid)
        self.C = len(grid[0])

        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid,row,col,word):
                    print("Pattern found at "+
                    str(row) + ', ' + str(col))

if __name__ == '__main__':
    grid = ["GREEKSFORGREEKS",
            "GREEKSQUIZGREEK",
            "IDEQAPRACTICE"]
        gfg =GFG()
        gfg.patternSearch(grid,'GEEKS')
        print('')
        gfg.patternSearch(grid,'EEE') 

