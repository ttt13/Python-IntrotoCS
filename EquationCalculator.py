# EquationCalculator.py
#
# Discription: This equation calculator can add, subtract, multiply,
#              and divide an equation that follows the following syntax:
#              <operand><space><operator><space><operand>. An operator is
#              any of these following 4 operators: (+, -, *, /)
#
# Peter Tran
#
# February 6th 2017

# Print an introduction
print("Welcome to my Equation Calculator!\n")

# Print the function of this code
print("""My EquationCalculator can
    add: +,
    subtract: -,
    multiply: *,and
    divide: / (result is a float)\n""")

# Print the instructions for user input
print("""The equation you enter must follow this syntax:
<operand><space><operator><space><operand>.
An <operand> is any float you wish.
An <operator> is any of the above 4 operators this Calculator can deal with.
A <space> is an empty space. :)""")

# Input an equation
equation = input("Please, enter an equation: ")

# Turn equation into list using split method
equationSplit = equation.split()

# Print the equation that was entered
print("The equation you entered is '%s'." %(equation))

# If only enter key pressed, display error message.
if len(equationSplit) == 0 :
    print("Have you simply pressed the Enter key? Please, enter an equation next time! :)")

# If the equation contains a word, display error message.
if equation.isalpha() == True :
    print("You have entered the sequence of letters '%s' which is not an equation. Please, try again." %(equation))

# If user enters an equation of length 1, observe the following conditions: 
elif len(equationSplit) == 1 :
    
    # If user enters only an operator, display error message.
    if '*' in equationSplit[0] or '/' in equationSplit[0] or '-' in equationSplit[0] or '+' in equationSplit[0] :
        print("You have entered the equation '%s' which is not a complete equation since it only contains the operator '%s'. Please, try again." %(equation, equation))

    # If user enters only one float, display error message.
    else:
        print("You have entered the equation '%s' which is not a complete equation since it only contains the operand '%s'. Please, try again." %(equation, equation))

# If user enters an equation of length 2, observe the following conditions:
elif len(equationSplit) == 2 :

    # If user enters <float> <operand> or <operand> <operand>, display error message.
    if '*' in equationSplit or '/' in equationSplit or '+' in equationSplit or '-' in equationSplit :
        print("You have entered the equation '%s' which is not a complete equation since it only contains the operand %s and the operator %s. Please, try again." %(equation, equationSplit[0], equationSplit[1]))

    # If user enters <float> <float>, display error message.
    else :
        print("You have entered the equation '%s' which is not a complete equation since it only contains the operand %s and the operand %s. Please, try again." %(equation, equationSplit[0], equationSplit[1]))

# If the equation is of length 3, observe the following condition below:
elif len(equationSplit) == 3 :

    # If equationSplit[0] is an integer
    if '1' in equationSplit[0] or '2' in equationSplit[0] or '3' in equationSplit[0] or '4' in equationSplit[0] or '5' in equationSplit[0] or '6' in equationSplit[0] or '7' in equationSplit[0] or '8' in equationSplit[0] or '9' in equationSplit[0] or '0' in equationSplit[0] :

        # If equationSplit[2] is an integer
        if '1' in equationSplit[2] or '2' in equationSplit[2] or '3' in equationSplit[2] or '4' in equationSplit[2] or '5' in equationSplit[2] or '6' in equationSplit[2] or '7' in equationSplit[2] or '8' in equationSplit[2] or '9' in equationSplit[2] or '0' in equationSplit[2] :

            # Set up operation variables
            operand1 = equationSplit[0]
            operand2 = equationSplit[2]
            operator = equationSplit[1]
            
            # If the equation contains '+', add.
            if '+' in equationSplit :
                result = float(operand1) + float(operand2)
                print("The equation is %g %s %g = %g" %(float(operand1), operator, float(operand2), result))
                
            # If the equation contains '-', subtract.
            if '-' in equationSplit :
                result = float(operand1) - float(operand2)
                print("The equation is %g %s %g = %g" %(float(operand1), operator, float(operand2), result))
                
            # If the equation contains '*', multiply.
            if '*' in equationSplit :
                result = float(operand1) * float(operand2)
                print("The equation is %g %s %g = %g" %(float(operand1), operator, float(operand2), result))
                
            # If the equation contains '/', observe the following conditions.        
            if '/' in equationSplit :
                
                # If user attempts to divide by 0, print that this is not possible.    
                if float(operand2) == 0 :
                    print("The equation has 0 as a demoninator. The equation cannot be evaluated. Please, try again.")

                # Otherwise, divide the equation.
                else :
                    result = float(operand1) / float(operand2)
                    print("The equation is %g %s %g = %g" %(float(operand1), operator, float(operand2), result))
                    
        # Print following message if equationSplit[2] is not a number
        else :
            print("You have entered the sequence '%s' which is not an equation. Please, try again." %(equation))
            
    # Print following message if equationSplit[0] is not a number
    else :
        print("You have entered the sequence '%s' which is not an equation. Please, try again." %(equation))
     
# Indicates the end of the code 
print("\n----!")
