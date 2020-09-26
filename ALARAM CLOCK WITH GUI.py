#GUI Alaram Using Python by NKC
from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox


root = Tk()
root.title("Alarm GUI Using Python")


def SubmitButton():
    AlarmTime = entry1.get()
    Message1()

    CurrentTime = time.strftime("%H:%M")
    print("Alarm time: {}".format(AlarmTime))

    while AlarmTime != CurrentTime:

        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime == CurrentTime:
        print("Music Playing")
        os.system("Start alarm-music.mp3")
        label2.config(text="Alaram Ringing.....")
        messagebox.showinfo(title='Label', message="{}".format(entry2.get()))


def Message1():
    AlarmTimeLable = entry1.get()
    label2.config(text="Alarm is Scheduled...")

    messagebox.showinfo(title='Alarm clock', message='Alarm will Ring at {}'.format(AlarmTimeLable))


frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height=100, width=100)

label1 = ttk.Label(frame1, text="Enter the Alarm time :")
label1.pack()

entry1 = ttk.Entry(frame1, width=30)
entry1.pack()
entry1.insert(3, "Eg: 3:15 (24 hours) ")

labelAlarmMessage = ttk.Label(frame1, text="Label : ")
labelAlarmMessage.pack()

entry2 = ttk.Entry(frame1, width=30)
entry2.pack()

button1 = ttk.Button(frame1, text="submit", command=SubmitButton)
button1.pack()

label2 = ttk.Label(frame1)
label2.pack()

root.mainloop()