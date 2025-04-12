import tkinter as tk

# Function to append characters to the expression
def press(value):
    current = equation.get()
    equation.set(current + str(value))

# Function to evaluate the expression
def equalpress():
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except Exception:
        equation.set("Error")

# Function to clear the display
def clear():
    equation.set("")

# Main application window
window = tk.Tk()
window.title("Smooth Calculator")
window.geometry("340x470")
window.resizable(False, False)
window.configure(bg="#2d2d2d")

# Equation display setup
equation = tk.StringVar()
display = tk.Entry(window, textvariable=equation, font=("Arial", 24), bd=10, relief="sunken", bg="#1e1e1e", fg="white", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=10, ipady=10, sticky="nsew")

# Button styles
btn_font = ("Arial", 18)
btn_bg = "#3c3c3c"
btn_fg = "white"
btn_active_bg = "#505050"

# Button creation helper
def create_button(text, row, col, colspan=1, command=None):
    return tk.Button(
        window, text=text, font=btn_font, bg=btn_bg, fg=btn_fg,
        activebackground=btn_active_bg, padx=20, pady=20, borderwidth=0,
        command=command or (lambda t=text: press(t))
    ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Grid weights
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        create_button(text, row, col, command=equalpress)
    else:
        create_button(text, row, col)

# Clear button spans across all columns at the bottom
tk.Button(
    window, text="C", font=btn_font, bg="#ff5c5c", fg="white", activebackground="#ff7b7b",
    padx=20, pady=20, borderwidth=0, command=clear
).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=10)

# Start the GUI loop
window.mainloop()
