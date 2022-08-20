from cgitb import text
from contextlib import nullcontext
from email import message_from_binary_file
from tkinter.filedialog import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import turtle

#Window Settings
win = tk.Tk()
win.geometry('400x600')
win.title("Fluent Notepad")
win.config(bg = "white")
top = Frame(win)
top.pack(padx = 10, pady = 5, anchor = 'nw')

#Saving, Opening, Clearing, Exiting
def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('Text files', '.txt')])
    if new_file is None:
        return
    text = str(Text.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('Text files', '*.txt')])
    if file is not None:
        content = file.read()
    Text.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)

def exitApp():
    win.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "You have unsaved changes. Do you want to quit?"):
        win.destroy() 

win.protocol("WM_DELETE_WINDOW", on_closing)

#Buttons
b1 = Button(win, text="Save", bg = "white", command = saveFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(win, text="Open", bg = "white", command = openFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(win, text="Clear", bg = "white", command = clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(win, text="Exit", bg = "white", command = exitApp)
b4.pack(in_ = top, side=LEFT)
entry = Text(win, wrap = WORD, bg = "white", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)
win.mainloop()




