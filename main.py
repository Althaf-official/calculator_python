import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except Exception as e:
        output.config(text="Error: " + str(e))

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window)
entry.pack()

# Create the calculate button
button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

# Create the output label
output = tk.Label(window)
output.pack()

# Start the main loop
window.mainloop()
