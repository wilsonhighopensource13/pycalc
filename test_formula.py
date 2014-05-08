from Tkinter import *
fformula_name = "C:\\Users\\2015fulricb\\Desktop\\Formulas\\physics.fio"
def init_formula():
    editor = Tk()
    editor.title("Formula Editor")
    def open_formula():
        fformula = open(fformula_name, "rt")
        i = 0
        formulas = {}
        for line in fformula:
            if "=" in line:
                formula = line
                formulas[formula] = []
            else:
                delim = line.find(":")
                var = line[0:delim]
                description = line[delim:]
                formulas[formula].append([var,description])
        return
    def exec_formula():
        return
    def save_formula():
        return
    open_button = Button(editor, text="Open", command=open_formula)
    new_button = Button(editor, text="Exec", command=exec_formula)
    save_button = Button(editor, text="Save", command=save_formula)
    #grid these
    open_button.grid(row=0,column=0)
    new_button.grid(row=0, column=1)
    save_button.grid(row=0, column=2)
init_formula()