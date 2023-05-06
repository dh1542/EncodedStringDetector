import tkinter as tk

window = tk.Tk()

header = tk.Label(text = "Encoded String Detector & Converter")
header.pack()

entry = tk.Entry()
entry.bind()
entry.pack()

user_input = entry.get()
print(user_input)

window.mainloop()