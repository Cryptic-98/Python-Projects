import tkinter as tk

def button_clicked():
    print('Button clicked.')

# Create the main application window
root = tk.Tk()

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_clicked)

# Pack the button into the window
button.pack()

# Run the Tkinter event loop
root.mainloop()
