import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Create a global variable for the expression string
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    global expression
    try:
        # Use eval to calculate the expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the display
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar() to update the entry text field
equation = tk.StringVar()

# Create the display text entry box
entry_box = tk.Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
entry_box.grid(columnspan=4, padx = 20, pady = 20)

# Create buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=equalpress)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=clear)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20, 'bold'), command=lambda t=text: press(t))
    
    button.grid(row=row, column=col, sticky="nsew")

# Configure grid to make buttons expand
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
