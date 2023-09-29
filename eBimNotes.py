import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import pyperclip
from zoneinfo import ZoneInfo
from datetime import datetime

def insert_timestamp(event):
    pacifictime = datetime.now(ZoneInfo('America/Los_Angeles')).replace(tzinfo=None)
    txtbox.insert(tk.INSERT, "\n" + str(pacifictime.isoformat(sep=" ",timespec="seconds")) + " >>> ")
    return "break"

def clear_text():
    copytext = txtbox.get(1.0,tk.END)
    pyperclip.copy(copytext)
    txtbox.delete(1.0,tk.END)  
    insert_timestamp(None)
    return "break"

master_window = Tk()

buttons_frame = Frame(master_window)
buttons_frame.grid(row=5, column=0, sticky=W+E)

group = LabelFrame(master_window, text="ISO Format: YYYY-MM-DD HH:mm:SS", padx=5, pady=5)
group.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

master_window.columnconfigure(0, weight=1)
master_window.rowconfigure(1, weight=1)

group.rowconfigure(0, weight=1)
group.columnconfigure(0, weight=1)

txtbox = scrolledtext.ScrolledText(group, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=E+W+N+S)

label = tk.Label(master_window,text="SCRIBE",font='none 24 bold')
label.grid(row=0, column=0, sticky=W+E)

clrbutton = Button(buttons_frame,text="COPY & CLEAR",width=20,command=clear_text,font="none 15 bold")
clrbutton.grid(row=5, column=0, sticky=E+W+N+S)

txtbox.bind("<Return>",insert_timestamp)

insert_timestamp(None)

mainloop()
