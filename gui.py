import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

TITLE = "Quantum CV"
HEIGHT = 700
WIDTH = 700

root = tk.Tk()
root.resizable(False, False)
root.title(TITLE)

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

title = tk.Label(canvas, text = TITLE, font = ('Century', 20), anchor = 'center')
title.place(relx = .15, rely = .02, relwidth = .7, relheight = .05)

frame_1 = tk.Frame(root)
frame_1.place(relwidth=0.8, relheight=0.35, relx=0.5, rely=0.1, anchor='n')

label_1 = tk.Label(frame_1, text = "Choose Image")
label_1.place(relheight=0.1, relx=0.02)

root.mainloop()