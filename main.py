import threading
from threading import Thread
import tkinter
from tkinter import Button, Entry, Label, Toplevel, ttk, Frame, Event, Text
from tkinter import *
import random
import string
import math
from tkinter.constants import BOTH, LEFT, TOP

root = tkinter.Tk()

string.ascii_letters = 'abcdefghijklmnopqrstuvwx yzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))

def consolespam():
    for i in range(10000000000000):
        print(random_char(200))
    print('done')

def threadedcs():
    thrcs = Thread(target=consolespam)
    thrcs2 = Thread(target=consolespam)
    thrcs3 = Thread(target=consolespam)
    thrcs4 = Thread(target=consolespam)
    thrcs5 = Thread(target=consolespam)
    thrcs.start()
    thrcs2.start()
    thrcs3.start()
    thrcs4.start()
    thrcs5.start()

def filespam():
    for x in range(1000000000):
        y = open(f'Spammed-File-{random_char(10)}', 'a')
        y.write('lmaooooooooooo')

def threadedfs():
    thrfs = Thread(target=filespam)
    thrfs2 = Thread(target=filespam)
    thrfs3 = Thread(target=filespam)
    thrfs4 = Thread(target=filespam)
    thrfs5 = Thread(target=filespam)
    thrfs.start()
    thrfs2.start()
    thrfs3.start()
    thrfs4.start()
    thrfs5.start()

def spamwin():
    for i in range(75):
        okay = Toplevel(root)
        okay.title(random_char(20))
        okay.geometry(f'{random.randint(200, 600)}x{random.randint(200, 600)}+{random.randint(1, 1000)}+{random.randint(1, 1000)}')
        okayb = Label(okay, text=f'{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n{random_char(600)}\n', bg='black', fg='red')
        okayb.pack()

def threadedws():
    thrws = Thread(target=spamwin)
    thrws2 = Thread(target=spamwin)
    thrws3 = Thread(target=spamwin)
    thrws4 = Thread(target=spamwin)
    thrws5 = Thread(target=spamwin)
    thrws.start()
    thrws2.start()
    thrws3.start()
    thrws4.start()
    thrws5.start()

def whloop():
    while True:
          print(pow(random.randint(1,1000), random.randint(1,1000)))

def thrwhloop():
    thrwl = Thread(target=whloop)
    thrwl2 = Thread(target=whloop)
    thrwl3 = Thread(target=whloop)
    thrwl4 = Thread(target=whloop)
    thrwl5 = Thread(target=whloop)
    thrwl6 = Thread(target=whloop)
    thrwl7 = Thread(target=whloop)
    thrwl8 = Thread(target=whloop)
    thrwl9 = Thread(target=whloop)
    thrwl10 = Thread(target=whloop)
    thrwl.start()
    thrwl2.start()
    thrwl3.start()
    thrwl4.start()
    thrwl5.start()
    thrwl6.start()
    thrwl7.start()
    thrwl8.start()
    thrwl9.start()
    thrwl10.start()

message = tkinter.Label(root, text='Welcome to school breaker, please enter the password to continue:\n', bg='#23272e', foreground='white')
message.config(font=('Helvetica bold', 15))
message.pack()

linebr = tkinter.Label(root, text='\n', bg='#23272e', foreground='white')

title_bar = Frame(root, bg='#23272e', relief='raised', bd=2)

linebr.pack

root.title('School Breaker')
root.geometry('600x400+50+50')
root.config(bg='#23272e')

password_entry = ttk.Entry(
    root,
    show='\u2022',
    background='#23272e',
    foreground='black'
)
password_entry.pack()

message2 = tkinter.Label(root, text='This password has been set into place to prevent the misuse of this tool.\nWe do not promote harmful activities. We are not responsible of what you do with this tool.\nThis tool is made for educational purposes only.\n', bg='#23272e', fg='white')
message2.pack()

def clickedit():
    password = password_entry.get()
    if password == '1337':
        confirmed = Toplevel(root)
        confirmed.title("School Breaker")
        confirmed.geometry("600x380+650+50")
        confirmed.config(bg='#23272e')
        headerr = Label(confirmed, text='WELCOME TO SCHOOL BREAKER:', bg='#23272e', fg='white')
        headerr.config(font=('Helvetica bold',20))
        csbutton = Button(confirmed, text='Spams Console', bg='#471f47', fg='white', command=consolespam, height=1, width=80)
        fsbutton = Button(confirmed, text='Spams Files on PC', bg='#471f47', fg='white', command=filespam, height=1, width=80)
        wsbutton = Button(confirmed, text='Spams new windows', bg='#471f47', fg='white', command=spamwin, height=1, width=80)
        wlbutton = Button(confirmed, text='Spams intensive maths', bg='#471f47', fg='white', command=whloop, height=1, width=80)
        threadwarn = Label(confirmed, text='!! WARNING !!\nTHESE FUNCTIONS CAUSE EXTREME LAG!!\nThese are the threaded modules:', bg='#23272e', fg='white')
        tcsbutton = Button(confirmed, text='Threaded console spammer', bg='#471f47', fg='white', command=threadedcs, height=1, width=80)
        tfsbutton = Button(confirmed, text='Threaded file spammer', bg='#471f47', fg='white', command=threadedfs, height=1, width=80)
        twsbutton = Button(confirmed, text='Threaded window spammer', bg='#471f47', fg='white', command=threadedws, height=1, width=80)
        twlbutton = Button(confirmed, text='Threaded intensive maths', bg='#471f47', fg='white', command=thrwhloop, height=1, width=80)
        disclaimer = tkinter.Label(confirmed, text='DEAR USER:\nPlease note that we are no responsible for any harm\nor damage done by this tool.\nThis tool is strictly for educational purposes only.', bg='#23272e', fg='white')
        headerr.pack()
        csbutton.pack()
        fsbutton.pack()
        wsbutton.pack()
        wlbutton.pack()
        threadwarn.pack()
        tcsbutton.pack()
        tfsbutton.pack()
        twsbutton.pack()
        twlbutton.pack()
        disclaimer.pack()
    else:
        exit()

enterpass = Button(root, text='Enter', bg='#23272e', fg='white', command=clickedit)
enterpass.pack()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()