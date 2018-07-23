



# Main

#print("Welcome to my Interior Design Application.\n\n")
#input("Please, enter the path and anme of the data file or 'X' to exit: ")


def createMaze(aMaze, aWidth, aHeight, cellContent):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "cellContent".      
    '''
    aMaze = [ [ (cellContent) for i in range(aWidth) ] 
                                                  for j in range(aHeight) ]   
    # For debug purposes - Print maze as a list of list
    # printMaze(aMaze)
    return aMaze

# Print Maze - for debug purposes
def printMaze(aMaze):
    ''' Print "aMaze" - for debug purposes.
    ''' 
    for row in aMaze:
        print(row)
        
def boundaries(aMaze):

    
aMaze = createMaze("blah", 10, 5, ' ')

printMaze(aMaze)
