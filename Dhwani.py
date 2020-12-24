from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer

root = Tk()
root.geometry('300x175')
root.title('Dhwani')
root.resizable(0,0)
root.iconbitmap('assets\ico.ico')
root.configure(background = 'grey30')

mixer.init()

statusBar = Label(root, text = 'Welcome to Dhwani', relief = 'sunken', bg='grey30', fg = 'white')
statusBar.pack(side='top', fill = X)

def load():
    global file
    file = filedialog.askopenfile()

def play():
    global paused
    if paused:
        mixer.music.unpause()
        statusBar['text'] = 'Music Resumed'
        paused = False

    else:
        try:
            mixer.music.load(file)
            mixer.music.play()
            statusBar['text'] = 'Playing'
        except:
            messagebox.showerror('Error', 'Unable to load your file.')

paused = False

def pause():
    global paused
    paused = True
    mixer.music.pause()
    statusBar['text'] = "Music Paused"

def stop():
    mixer.music.stop()
    statusBar['text'] = "Music Stopped"

def set_vol(val):
    vol = int(val) / 100
    mixer.music.set_volume(vol)

def info():
    messagebox.showinfo('About Us', 'Dhwani is coded by Shreyash & Tejas.')

load = Button(root, text = 'Load', bg='purple2', activebackground = 'grey30', width = 10, command = load)
play = Button(root, text = 'Play', bg='purple2', activebackground = 'grey30', width = 5, pady=10, command = play)
pause = Button(root, text = 'Pause', bg='purple2', activebackground = 'grey30', width = 5, command = pause)
stop = Button(root, text = 'Stop', bg='purple2', activebackground = 'grey30', width = 5, command = stop)


load.place(x = 112, y = 33)
pause.place(x = 40, y = 80)
play.place(x = 130, y = 73)
stop.place(x = 220, y = 80)


scale = Scale(root, label = '-      Volume      +', showvalue = 0, highlightcolor = 'purple2', from_=0 , to = 100, bg='grey30', orient = HORIZONTAL, bd = 0, highlightbackground = 'purple2', activebackground = 'grey30',  command = set_vol)  
scale.set(70)
mixer.music.set_volume(0.7)
scale.place(x = 100, y = 133)

infoImage = PhotoImage(file = 'assets\info.png')
infoButton = Button(root, image = infoImage, relief = 'raised', borderwidth = 0, bg = 'grey30', highlightbackground = 'grey30', activebackground = 'grey30', command = info)
infoButton.place(x = 261, y = 137)

root.mainloop()
