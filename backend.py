# backend.py

class CalculatorBackend:
    def __init__(self):
        self.expression = ""

    def press(self, num):
        """Update the expression with the given number or operator."""
        self.expression += str(num)
        return self.expression

    def equalpress(self):
        """Evaluate the current expression and return the result."""
        try:
            result = str(eval(self.expression))  # Unsafe in production!
            self.expression = result  # Update expression to result for further calculations
            return result
        except:
            self.expression = ""  # Reset on error
            return "error"

    def clear(self):
        """Clear the expression."""
        self.expression = ""
        return self.expression
