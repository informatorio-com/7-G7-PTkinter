import tkinter as tk

root = tk.Tk()
root.title("Hola desde Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="¡Hola, mundo!")
label.pack(pady=20)

root.mainloop()
