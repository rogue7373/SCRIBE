import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import pyperclip
from zoneinfo import ZoneInfo
from datetime import datetime
import requests

global darkmode_on,tablename,sysid,get,post,ticketid,username,password,newWin
darkmode_on = False
tablename = str("insert_tablename")
sysid = int(1234)
ticketid = int(1234)
username = str("insert_username")
password = str("insert_password")
get = str("/api/now/table/"+tablename+"/"+str(sysid))
post = str("/api/now/table/"+tablename)

# def login_window():
#     newWin = Toplevel(root,background="grey")
#     newWin.title("Enter LAN Credentials")
#     newWin.geometry("300x120")
#     Label(newWin,text="Enter your credentials")
#     newWin.columnconfigure(0, weight=1)
#     newWin.rowconfigure(1,weight=1)
#     # sndbutton.destroy()
#     newWinFrame = Frame(newWin,background="grey")
#     newWinFrame.grid(row=0,column=0)
#     usernameField = Entry(newWinFrame)
#     usernameField.grid(row=0,column=0,pady=20)
#     usernameField.focus_set()
#     pwField = Entry(newWinFrame,insertofftime=1)
#     pwField.grid(row=1,column=0,pady=0)
#     loginbuttonFrame = Frame(newWin,background="grey")
#     loginbuttonFrame.grid(row=2,column=0)
#     loginbutton = Button(loginbuttonFrame,text="SUBMIT",font="Roboto 10 bold", command=submit_note)
#     loginbutton.grid(row=2,column=0,sticky=S,pady=10)
#     usernameField.get()
#     pwField.get()
    
def submit_note():
    request = requests.get("https://idpxnyl3m.pingidentity.com/pingid/rest/4/startauthentication/do",auth=(username,password))
    print(username, password, request.status_code, request.reason)

def insert_text():
    txtbox.delete(1.0,tk.END)
    txtbox.insert(tk.INSERT,pyperclip.paste()+"\n ^ HANDOFF ^")
    insert_timestamp(None)

def insert_timestamp(event):
    pacifictime = datetime.now(ZoneInfo('America/Los_Angeles')).replace(tzinfo=None)
    txtbox.config(selectbackground="grey",font="none 12 bold",wrap=WORD)
    txtbox.insert(tk.INSERT, "\n" + str(pacifictime.isoformat(sep=" ",timespec="seconds")) + " >>>    ")
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
        label.config(bg="white",background="white",foreground="black")
        group.config(bg="white",background="white",foreground="black")
        buttons_frame.config(bg="white",background="white")
        toolbuttons_frame.config(bg="white",background="white",padx=20)
        clrbutton.config(bg="white",background="white",foreground="black")
        pstbutton.config(bg="white",background="white",foreground="black")
        darkmodebutton.config(bg="black",background="black",foreground="white",text="DARK")
        txtbox.config(bg="white",background="white",foreground="black",selectbackground="grey",insertbackground="black",blockcursor=False)
        darkmode_on = False
        # sndbutton.config(bg="white",background="white",foreground="black")
    else:
        root.config(bg="black",background="black")
        label.config(bg="black",background="black",foreground="white")
        group.config(bg="black",background="black",foreground="white")
        buttons_frame.config(bg="black",background="black")
        toolbuttons_frame.config(bg="white",background="black",padx=20)
        clrbutton.config(bg="black",background="black",foreground="white")
        pstbutton.config(bg="black",background="black",foreground="white")
        darkmodebutton.config(bg="white",background="white",foreground="black",text="LIGHT")
        txtbox.config(bg="black",background="black",foreground="white",selectbackground="grey",insertbackground="white",blockcursor=False)
        darkmode_on = True
        # sndbutton.config(bg="black",background="black",foreground="white")

def privacy_filter(event):
    for x in password:
        pass

root = Tk()
root.configure(bg="white")
root.title("SCRIBE")
root.geometry("450x550")
root.columnconfigure(0, weight=1)
root.rowconfigure(1,weight=1)

label = tk.Label(root,text="SCRIBE...",font='Roboto 32 bold italic', foreground="black",bg="white")
label.grid(row=0, column=0, sticky=W+E)

group = LabelFrame(root, text="Version 1.1.0", padx=5, pady=5, bg="white", foreground="grey",font="Roboto 8 italic")
group.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
group.rowconfigure(0, weight=1)
group.columnconfigure(0, weight=1)

buttons_frame = Frame(root,bg="white")
buttons_frame.grid(row=3,column=1,sticky=S)    

toolbuttons_frame = Frame(root,bg="white",background="white",padx=20)
toolbuttons_frame.grid(row=0,column=1)

pstbutton = Button(buttons_frame,text="PASTE",width=7,command=insert_text,font="Roboto 10 bold",foreground="black",bg="white")
pstbutton.grid(column=0,row=0,sticky=W)

clrbutton = Button(buttons_frame,text="COPY",width=7,command=clear_text,font="Roboto 10 bold",foreground="black",bg="white")
clrbutton.grid(column=0,row=1,pady=20,sticky=W)

# sndbutton = Button(toolbuttons_frame,text="LOGIN",width=7,command=login_window,font="Roboto 10 bold",foreground="black",bg="white")
# sndbutton.grid(row=0,column=0,pady=20,sticky=E+N)

darkmodebutton = Button(toolbuttons_frame,width=7,font="Roboto 10 bold",foreground="white",bg="black",command=darkmode_selector,text="DARK")
darkmodebutton.grid(row=1,column=0,sticky=E+N)

txtbox = scrolledtext.ScrolledText(group, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=E+W+N+S)
txtbox.config(font="Roboto 12",blockcursor=False)
txtbox.bind("<Return>",insert_timestamp)

insert_timestamp(None)

root.mainloop()