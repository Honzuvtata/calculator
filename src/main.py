import tkinter as tk
from backend import CalculatorBackend

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Instantiate the backend
calc = CalculatorBackend()

# Create a StringVar to hold the display value
equation = tk.StringVar()

# Function to update expression in the entry box when buttons are pressed
def press_button(num):
    expression = calc.press(num)
    equation.set(expression)

# Function to evaluate the expression and update the entry box
def evaluate_expression():
    result = calc.equalpress()
    equation.set(result)

# Function to clear the display
def clear_expression():
    result = calc.clear()
    equation.set(result)

# Create the display text entry box
entry_box = tk.Entry(root, textvariable=equation, font=('arial', 25, 'bold'), bd=10, insertwidth=8, width=20, borderwidth=6)
entry_box.grid(columnspan=4, padx=20, pady=20)

# Create buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=clear_expression)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=lambda t=text: press_button(t))
    
    button.grid(row=row, column=col, sticky="nsew")

# Configure grid to make buttons expand
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
