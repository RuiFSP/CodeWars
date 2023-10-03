""" 
Quite often our programs will need to accept inputs from a user, 
whether through terminal commands, API requests, or form submissions. 
In these cases inputs are processed as a str data type. Lets practice 
type conversion by building a simple_calculator function.

Specs
Our function should take a single list of strings as an argument, containing our first opperand, 
followed by an operator and then the 2nd operand. eg:
simple_calculator(['1', '+', '1' ]) #=> 2

The function should return 'Please enter valid format: [Operand, Operator, Operand]' for arguments that dont match the required format
The funtion should work with the following simple operators +, -, *, /, %, and should return'Please enter a valid operator [ +, -, /, *, % ]' if any other operators are passed
Assume that the operands are always numeric (floats or integers); no need to validate their data type 
"""




# Implement your simple_calculator function below
def simple_calculator(args):
    # Check if the input list has exactly 3 elements
    if len(args) != 3:
        return 'Please enter valid format: [Operand, Operator, Operand]'

    # Unpack the input list
    num1, op, num2 = args

    # Check if the operator is valid
    if op not in ['+', '-', '*', '/', '%']:
        return 'Please enter a valid operator [ +, -, /, *, % ]'

    # Convert the operands to float and perform the calculation
    num1 = float(num1)
    num2 = float(num2)

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return 'Division by zero is not allowed.'
        return num1 / num2
    elif op == '%':
        return num1 % num2
        

# Do not modify the code below:
if __name__ == "__main__":  
    assert simple_calculator(['5', '+', '5']) == 10
    assert simple_calculator(['10.5', '-', '5']) == 5.5
    assert simple_calculator(['8', '*', '8']) == 64
    assert simple_calculator(['1', '/', '4']) == 0.25
    assert simple_calculator(['9', '%', '2']) == 1
    assert simple_calculator(['1', '4']) == 'Please enter valid format: [Operand, Operator, Operand]'
    assert simple_calculator(['1', '4', '5', '+']) == 'Please enter valid format: [Operand, Operator, Operand]'
    assert simple_calculator(['1', '&', '5']) == 'Please enter a valid operator [ +, -, /, *, % ]'
    print("All tests passed")