#The GUI work is contained here.
from Tkinter import *
i = 0
root = Tk()
    
frame = Frame(root, width=500, height=400)
frame.config(bg="#")
clibox = Text(frame)
lbl=Label(frame ,text="Command Line")
clibox.grid(row=1,column=0)
lbl.grid(row=0,column=0)
clibox.config(bg="#000000", fg="#FFFFFF")
frame.pack()

root.mainloop()