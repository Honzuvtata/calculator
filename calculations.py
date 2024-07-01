validOperators = ("+", "-", "*", "/")

def calculate(firstNumber, operator, secondNumber): 
    if operator == "+":
        return firstNumber + secondNumber
    elif operator == "-":
        return firstNumber - secondNumber
    elif operator == "*":
        return firstNumber * secondNumber
    elif operator == "/":
        return firstNumber / secondNumber
    else:
        print("Invalid input operator")
        return False