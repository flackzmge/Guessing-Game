# 8 queens puzzle
# recursion for backtracking
# 8 queens on a chess board
# in a way that no queen can catch each other
# 8 X 8 matrix
# grid[y][x] -- y is vertical, x is horizontal


# Create a Solve() function 
# Prints first solution of the puzzle and waits for input"enter"
# once user presses "enter", the next solution is printed and so on
# Use recursion solve(n) - finds place for nth queen
# Calls itself recursively for n + 1 unless all queens have been placed
# Explores all possibilites using backtracking

# Create a Possible() function

# Create a print_grid() function


#Mark Scheme
#Find all solutions for the puzzle
# Easy to modify so works for different board sizes
# code should be as simple as possible and you should use comments to explain how it works
#You should use recursion to implement backtracking

import sys



ChessBrd = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

gridl = len(ChessBrd)



def possible(ChessBrd,y,x):
    #global ChessBrd # bring the global variable Chess Board
    
    gridl = len(ChessBrd)  # length of ChessBoard
    for i in range(gridl) :
        if ChessBrd[y][i]== 1 or ChessBrd[i][x]== 1:
            return False 
        # Check through all rows for a Queen if so Returns False
         #Checks through all columns for a Queen if so then Returns False
    for a in range(gridl) : # Checks all rows
        for b in range(gridl): # Checks all columns
            if ChessBrd[a][b]== 1: # if there is a Queen 
                if (a + b == y +x ) or ((a - b == y - x ))  : # checks for diagonal 
                    return False
    return True



def solve(ChessBrd,n,y):
    if n==0:
        print_grid(ChessBrd) # changes 1 and 0s in ChessBrds to Qs and Dots
        print("")
        print("") # added on spacing 
        return True
    for col in range(0,gridl): 
        if (possible(ChessBrd,y,col))==True and (ChessBrd[y][col]!=1): 
            ChessBrd[y][col] = 1 # if possibles rules are met and there is no existing 1, place a 1
            
            solve(ChessBrd,n-1,y+1) # Recursiom 
               
                
            ChessBrd[y][col] = 0 # Backtracking
            
                 
    return False 
         

                    
def print_grid(ChessBrd):
    for i in range(gridl): # for every row in the Chessbrd
        for j in range(gridl): # and for every column
            print(('.', 'Q')[ChessBrd[i][j]], end=" ") # if 0 print "." and if 1 then print "1"
        print()  
    enter = input("More? ")
    if enter != "":  
        print("Queens Game Over!")
        sys.exit() # User is allowed to enter a value when the More question appears, proceeds if enter is pressed, stops if anything else is said
        
    
        

def main():
    for i in range(0, gridl): 
        #ChessBrd
        solve(ChessBrd, gridl, i) # Solve function does the solution
        ChessBrd[i][0:] # Creates a new solution
        if ChessBrd[i] >= ChessBrd[i][0:]: # if all solutions are done then output message and end program with a break
            print("No more solutions!")
            break
        


main()

