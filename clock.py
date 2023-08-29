import tkinter
from time import strftime

tk = tkinter.Tk()
title = tk.title("Clock")
tk.resizable(1080,200)

def time():
    string = strftime("%H:%M:%S %p")
    clocktime.config(text=string)
    clocktime.after(1000, time)

clocktime = tkinter.Label(
    tk, font=("calibri", 40,"bold"),background="black",foreground="gray"
)

clocktime.pack(anchor = "center")
time()
tk.mainloop()