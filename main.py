import calculations
import inputValidation
import memory


def main():
    while True:
        print("Log: start")

        validOperators = calculations.validOperators
        
        #firstNumber = int(input("Enter first number: "))
        firstNumber = inputValidation.validateIntInput("Enter first number: ")

        operator = inputValidation.validateInputInList("Enter operator: \n"
                          "1: plus \n"
                          "2: minus \n"
                          "3: nasobeni \n"
                          "4: deleni: \n",
                        validOperators)
        secondNumber = inputValidation.validateIntInput("Enter second number: ")

        result = calculations.calculate(firstNumber, operator, secondNumber)

        print(f"Result = {result}")
        print(f"Entered first number: {firstNumber}, entered operator: {operator}, entered second number: {secondNumber}")

        memoryLog = str(firstNumber) + str(operator) + str(secondNumber) + "=" + str(result)
        memory.writeToMemory(memoryLog)

if __name__ == "__main__":
    main()
