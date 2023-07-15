import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = "Invalid Operator"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid Input")

# Create the main application window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x200")  # Optional window size (width x height)
root.configure(bg="purple")

# Input fields
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=10, pady=5)

operator_var = tk.StringVar()
operator_choices = ["+", "-", "*", "/"]
operator_dropdown = tk.OptionMenu(root, operator_var, *operator_choices)
operator_dropdown.grid(row=0, column=1, padx=10, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=2, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
