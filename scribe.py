import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import pyperclip
from zoneinfo import ZoneInfo
from datetime import datetime

global darkmode_on
darkmode_on = False

def insert_timestamp(event):
    pacifictime = datetime.now(ZoneInfo('America/Los_Angeles')).replace(tzinfo=None)
    txtbox.config(selectbackground="grey",insertbackground="black",font="none 12 bold")
    txtbox.insert(tk.INSERT, "\n" + str(pacifictime.isoformat(sep=" ",timespec="seconds")) + " >>> ")
    
    return "break"

def clear_text():
    copytext = txtbox.get(1.0,tk.END)
    pyperclip.copy(copytext)
    txtbox.delete(1.0,tk.END)  
    insert_timestamp(None)
    return "break"

def darkmode_selector():
    global darkmode_on
    if darkmode_on:
        root.config(bg="white",background="white")
        group.config(bg="white",foreground="black",background="white")
        label.config(bg="white",foreground="black",background="white")
        darkmodebutton.config(bg="white",foreground="black",background="white",text="Dark")
        toolbuttons_frame.config(bg="white",background="white",padx=20)
        buttons_frame.config(bg="white",background="white")
        clrbutton.config(bg="white",foreground="black",background="white")
        txtbox.config(bg="white",foreground="black",background="white",selectbackground="grey",insertbackground="black")
        buttons_frame.config(bg="white",background="white")
        darkmode_on = False
    else:
        root.config(bg="black",background="black")
        label.config(bg="black",foreground="white",background="black")
        toolbuttons_frame.config(bg="white",background="black",padx=20)
        group.config(bg="black",foreground="white",background="black")
        darkmodebutton.config(bg="black",foreground="white",background="black",text="Light")
        buttons_frame.config(bg="black",background="black")
        clrbutton.config(bg="black",foreground="white",background="black")
        txtbox.config(bg="black",foreground="white",background="black",selectbackground="grey",insertbackground="white")
        buttons_frame.config(bg="black",background="black")
        darkmode_on = True


root = Tk()
root.configure(bg="white")
root.title("SCRIBE")
root.geometry("640x360")

buttons_frame = Frame(root,bg="white")
buttons_frame.grid(row=3,sticky=S)    

toolbuttons_frame = Frame(root,bg="white",background="white",padx=20)
toolbuttons_frame.grid(row=3,column=2)

group = LabelFrame(root, text="  YYYY-MM-DD HH:mm:SS", padx=5, pady=5, bg="white", foreground="grey")
group.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

group.rowconfigure(0, weight=1)
group.columnconfigure(0, weight=1)

txtbox = scrolledtext.ScrolledText(group, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=E+W+N+S)
txtbox.config(font="none 12")

label = tk.Label(root,text="SCRIBE",font='none 24 bold', foreground="black",bg="white")
label.grid(row=0, column=0, sticky=W+E)

darkmodebutton = Button(toolbuttons_frame,width=7,font="none 10 bold",foreground="black",bg="white",command=darkmode_selector,text="Dark")
darkmodebutton.grid(row=1,column=0,sticky=E+N)

clrbutton = Button(buttons_frame,text="COPY",width=15,command=clear_text,font="none 10 bold",foreground="black",bg="white")
clrbutton.grid(pady=10, padx=25)

txtbox.bind("<Return>",insert_timestamp)

insert_timestamp(None)

root.mainloop()
