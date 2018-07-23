# InteriorDesignApp1171.py
#
# Description : Reads a file containing coordinates to:
#               Width and Height of a room,
#               Pieces of furnature (C = chair, T = table, t = small table, S = sofa, E = entertainment system)
#               The coordinates of each piece of furniture.
#               Then, displays a grid, with the furniture in their coordinates.
#
# Peter Tran
#
# 1 April 2017

# Build function that creates a list of lists.
def createGrid(aGrid, width, height, cells) :
    ''' Create and return "aGrid" of "Width" by "Height".
        Each cell of the grid is a string set to "cell".      
    '''
    aGrid = [ [ (cells) for i in range(width) ] 
                                                  for j in range(height) ]   
    return aGrid

# Build function that places elements into the lists of lists.
def placeInGrid(aGrid) :
    ''' Modifies aGrid by placing furnature (C, T, t, S, E) into cells, at given coordinates. 
        Parameters: aGrid
        return : aGrid (Modified)
    '''
    for line in textFile :
        line = line.split()
        for row in range(int(line[1]), int(line[2])+1 ) :
            for column in range(int(line[3]), int(line[4])+1) :
                aGrid[row][column] = line[0]
    return aGrid

# Build function that creates a border of numbers corresponding to the width of the grid.
def topNumbers(width) :
    ''' Creates a top border of numbers for the grid.
        Parameters: The width of the grid.
        Return: none.
    '''
    firstLine = offset
    for number in range(width) :
        if len(str(number)) == 1 :
            firstLine += " " + str(number) + " "
        else :
            firstLine += str(number) + " "   
    print(firstLine)   
    return

# Build function that creates horizontal border corresponding to width of grid.
def dashBoundaries(width) :
    ''' Creates a boundary of dashes for the horizontal axis of the grid.
        Parameters: Width of the grid.
        Return: none
    '''
    secondLine = offset
    for number in range(width) :
        secondLine += " " + "-" + " "
    print(secondLine)
    return

# Build function takes the list of lists and its elements, and displays it without brackets.
def displayGrid(aGrid) :
    ''' Displays the grid. First adds the number of the row, followed by a vertical border.
        Parameters: aGrid.
        Return: none.
    '''
    for aRow in range(len(aGrid)) :
        if len(str(aRow)) == 1 :
            print(str(aRow) + " " + "| " + "  ".join(aGrid[aRow]) + " " + "|")
        else :
            print(str(aRow) + "| " + "  ".join(aGrid[aRow]) + " " + "|")
    return

### Main part of the program - Top level of execution. ###

# Introduction.
print("Welcome to my Interior Design Application. \n")

# Set X as condition for while statement.
X = False

# While the user does not wish to exit the program by entering 'X' :
while not X :
    # Ask for a file to open.
    textFile = input("\nPlease, enter the path and name of the data file or 'X' to exit: ")

    # If user enters 'X', set condition to true, closing the program.
    if textFile.upper() == 'X' :
        X = True

    # Otherwise :
    else :
        
        # For spacing in the grid.
        offset = "   "

        # Open the file to read mode.
        textFile = open(textFile, "r")

        # Obtain the width and height contained in the first line of the file.
        widthHeight = textFile.readline().split()

        # Width is the first element of the first line.
        width = int(widthHeight[0])

        # Height is the second element of the first line.
        height = int(widthHeight[1])

        # Create the grid with the specified width and height, each cell containing nothing.
        aGrid = createGrid("aGrid", width, height, " ")

        # Begin placing furniture into the grid by filling the specified cells, using the coordinates given from the file.
        placeInGrid(aGrid)

        # Print numbers to line the top of the grid.
        topNumbers(width)

        # Horizontal border directly below the numbers.
        dashBoundaries(width)
        
        # Display the grid, including numbers lining the right side of the grid, and vertical borders on either side of the grid.
        displayGrid(aGrid)

        # Horizontal border at the bottom of the application.
        dashBoundaries(width)

# When the user wishes to close the program.        
print("\nExiting the Interior Design Application.")
    
    
