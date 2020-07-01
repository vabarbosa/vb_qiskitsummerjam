import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import image_merger as imgmgr
from PIL import Image, ImageTk

TITLE = "Quantum Art"
HEIGHT = 900
WIDTH = 700
BROWSE_BUTTON_TEXT_1 = "Browse for image 1"
BROWSE_BUTTON_TEXT_2 = "Browse for image 2"
RUN_BUTTON_TEXT = "Run"
IMAGE_ENTRY_TEXT_1 = "Type in image 1's directory or use the browse button above"
IMAGE_ENTRY_TEXT_2 = "Type in image 2's directory or use the browse button above"


def image_file_selector(entry):
    filename = filedialog.askopenfilename(initialdir="/D", title="Select image file",
                                          filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
    set_entrybox_text(filename, entry)
    return


def set_entrybox_text(filename, entry):
    entry.delete(0, tk.END)
    entry.insert(0, filename)
    return


def clear_search1(event):
    if (image_entry_1.get() == IMAGE_ENTRY_TEXT_1):
        image_entry_1.delete(0, "end")
        return None


def clear_search2(event):
    if (image_entry_2.get() == IMAGE_ENTRY_TEXT_2):
        image_entry_2.delete(0, "end")
        return None


def run_merger():
    print("Running...")
    image_dir_1 = image_entry_1.get()
    image_dir_2 = image_entry_2.get()
    imgmgr.run_quantum(image_dir_1, image_dir_2)

    # Now display the image.
    print("Done. Displaying results.")
    result_label = tk.Label(frame_1, text="Result", font=('Helvetica', 14))
    result_label.place(relheight=.1, relx=.5, rely=.3, anchor='n')

    # result_load = Image.open("result.jpeg")
    # result = ImageTk.PhotoImage(result_load)
    # output = tk.Label(image=result)
    # output.image = result
    # output.place(relheight=.5, relx=.5, rely=.3, anchor='n')

    # img1 = ImageTk.PhotoImage(Image.open("result.jpeg").resize((100, 100), Image.ANTIALIAS))
    panel = tk.Label(frame_1, image=img)
    # panel.pack(side="bottom", fill="both", expand="yes")
    panel.place(relheight=.5, relx=.5, rely=.4, anchor='n')
    return


root = tk.Tk()
root.resizable(False, False)
root.title(TITLE)

# Placeholder
img = ImageTk.PhotoImage(Image.open("result.jpeg").resize((300, 300), Image.NEAREST))

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="gray")
canvas.pack()

title = tk.Label(canvas, text=TITLE, font=('Helvetica', 18), anchor='center')
title.place(relx=.25, rely=.0125, relwidth=.5, relheight=.075)

frame_1 = tk.Frame(root)
frame_1.place(relwidth=0.85, relheight=0.85, relx=0.5, rely=0.1, anchor='n')

label_1 = tk.Label(frame_1, text="Choose Image", font=('Helvetica', 14))
label_1.place(relheight=0.1, relx=0.02, rely=0, anchor="nw")

image_entry_1 = tk.Entry(frame_1)
image_entry_1.insert(0, IMAGE_ENTRY_TEXT_1)
image_entry_1.place(relwidth=.9, relheight=.1, relx=.05, rely=.2, anchor='sw')
image_entry_1.bind("<Button-1>", clear_search1)
image_entry_2 = tk.Entry(frame_1)
image_entry_2.insert(0, IMAGE_ENTRY_TEXT_2)
image_entry_2.place(relwidth=.9, relheight=.1, relx=.05, rely=.2, anchor='nw')
image_entry_2.bind("<Button-1>", clear_search2)

browse_button_1 = tk.Button(frame_1, text=BROWSE_BUTTON_TEXT_1, command=lambda: image_file_selector(image_entry_1))
browse_button_1.place(relx=.69, rely=.05, relwidth=.25, relheight=.075, anchor='e')
browse_button_2 = tk.Button(frame_1, text=BROWSE_BUTTON_TEXT_2, command=lambda: image_file_selector(image_entry_2))
browse_button_2.place(relx=.69, rely=.05, relwidth=.25, relheight=.075, anchor='w')

run_button = tk.Button(frame_1, text=RUN_BUTTON_TEXT, command=lambda: run_merger())
run_button.place(relx=.5, rely=.2, relwidth=.25, relheight=.05, anchor='center')

root.mainloop()
