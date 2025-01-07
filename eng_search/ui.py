import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create main window
root = tk.Tk()
root.title("Simple Dictionary")

# Create widgets
label = tk.Label(root, text="Search the meaning of a word: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", command=on_button_click)
button.pack()

# run the event loop
root.mainloop()
