# 1) Think of a number between 1 and 100( including 1 and 0)
# 2)Ask question if number is less than(<), equal(=), greater than(>)
# 3)incorrect inputs should print out error message and prompt to type again asking user to do so 
# 4) Should spot if information user provides is inconistent/lying Should finish at once if detected
# 5)Play game and use same inteface
# 6)Binary Search
# 7) create a run time function from 1 to 100(1-101) that calculates the run time for every number using the algo
# " pick a number, any number between 1-100! I bet I can guess your number in 7 goes or less "
# " Is your number greater (>), equal (=), or less (<) than", (calculated number), "Please Answer <,=, or >!"
# " I have guessed it! its ", (Calculated Number)
# "I needed, (calculated number) steps!"
  

# Binary search:
# sort the list into assending order 1-100
# create a start and end element
# integer divison to find middle value of both even and odd values
# check if the middle value is equal to the mid value - if equal print a quote and number of steps and end program 
# if middle is not equal to the to the desired value then eliminate all the numbers from the right or left of the list (either 1-50 or 50-100 gets eliminated)
# repeat integer division on new list 
# repeat check on if the middle is equal
# if not eliminate left or right of the list depending on whether it is greater or Lower



def pickanumber():
    print("Guessing Game!")
    print("")
    print("Pick a number, any number between 1-100! I bet I can guess your number in 7 goes or less")
    print("")    
    # Asks the intial Questions

def CalculatedNumber(x,y,z):
    print(" I have guessed it! its ", x) # bring in the guessed value
    print("")
    if x == z // 2 :
        print("I needed" ,y , "step!") # If value is equal to value of 1st step then say 1 step needed 
    else:
        print("I needed" ,y , "steps!") # else say how many steps were needed
    return x, y,z

n = 100 

def game(n):
    my_list = list(range(1,n+1)) # Creates list of 1 to 100
    Constant = len(my_list) # A constant length of list
    pickanumber() # Calls out pick a number function 
    L = 0 # Lowest value in the List
    H = len(my_list) # Highest Value in the List 
    count = 0
    for i in range(1,8): # increment from 1 -7 as that is the highest amount of steps in an ordered list of 100 based on logarithms
        if L >= H:
            print("This number is outside of the range, You are cheating!") 
            break # Stops from looping the print 7 times more
        while L <= H:
            mid = (L + H) // 2
            print("Is your number greater (>), equal (=), or less (<) than",mid)
            answer = input("Please Answer <,=, or >!: "   ) # While the lowest value in the list is less than or equal to the highest keep repeating halving the highest + lowest to get mid list value
            if (answer == "<"):
                H = mid - 1 
                count += 1
                mid = (L + H) // 2 # when answer is equal to "<" increment count, set the highest value to 1 less of the mid and set mid to half of the new H and the L
            elif (answer == ">"):
                L = mid + 1
                count += 1
                mid = (L + H) // 2 # when answer is equal to ">" increment count, set the lowest to 1 higher of the mid and set mid to half of the H and the new L
            elif (answer == "="):
                count += 1
                return CalculatedNumber(mid,count,Constant) # Pass parameters of mid,count and Constant and they represent x,y,z in the CalculatedNumber() function 
            else:
                print("invalid input please try again ")
        
                       

game(n) 

# Improvements would be to use .split() to allow spaces in the string
# raw_input added so that all my inputs are automatically string instead of needing quotaion marks
# Changing n for any number should work and will take a maximum amount of steps as Log2(n) rounded up to the highest integer


