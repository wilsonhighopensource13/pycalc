#The GUI work is contained here.
from Tkinter import *
i = 0
root = Tk()
    
frame = Frame(root, width=500, height=400)
frame.config(bg="#838996",borderwidth=2)
inputbox = Text(frame)
outputbox = Text(frame)
lbl=Label(frame ,text="Command Line")
outputbox.grid(row=1,column=0)
inputbox.grid(row=2,column=0)
lbl.grid(row=0,column=0)
outputbox.config()
frame.pack()


root.mainloop()

