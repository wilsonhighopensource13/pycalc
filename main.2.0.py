#-*- coding: utf-8 -*- 
"""
Just an idea: nested matplotlib 
Use TopLevel to make an interpreter
"""
import math
import matplotlib.pyplot as plt
import sympy
sec_status = False
def replace_english(expression):
    replacement_tables = [["^","**"],["sin(","math.sin("],["cos(","math.cos("],["tan(","math.tan("],
                          ["cot(","math.cot("],["sec(","math.sec("],["csc(","math.csc("],["[[","math.floor("],["]]",")"],
                          ["arccos(","math.acos("],["sqrt(","math.sqrt("],["arccos(","math.acos("],["arcsin(","math.asin("],
                          ["arctan(","math.atan("],["abs(","math.fabs("],["pi","math.pi"]]
    variable = "x"
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for replacements in replacement_tables:
        old = replacements[0]
        new = replacements[1] 
        expression = expression.replace(old,new)
    for i in range(0,len(expression)-1):
        if (expression[i] in digits) and (expression[i+1] == variable):
            a, b =(expression[0:i+1],expression[i+1:])
            expression = ""
            expression = expression.join([a,"*",b])
    return expression

def ln(n):
    return math.log(n)
def log(n,base=10):
    return math.log(n,base)

def nderiv(expression, x, h=0.001, mode="replace"):
    """:finds the numerical derivative at a certain point, n, while h is the accuracy of the derivative calc, the lower the better
:uses f'(n)= (f(x+h) - f(x-h))/(2h)"""
    if mode == "replace":
        expression = replace_english(expression)
    try:
        deriv_expression_a = expression.replace("x", "(x+h)")
        deriv_expression_b = expression.replace("x", "(x-h)")
        solution =(eval(deriv_expression_a)-eval(deriv_expression_b))/(2*h)
    except:
        solution = None
    return solution


def table_deriv_points(expression, lower_bound, upper_bound, delta_x): ##finds all of the values of a function's derivatives
    #(on the increment delta_x) in domain: [lowerbound,upperbound]
    expression = replace_english(expression)
    xs = advanced_range_tool(lower_bound,upper_bound,delta_x)
    ys = []
    for number in xs:
        try:
            storage = round(nderiv(expression, number, .0001,""),4)
        except:
            storage = nderiv(expression, number, .0001, "")
        ys.append(storage)
    return xs, ys

def cderiv(expression, variable):
    return sympy.diff(expression, variable)

def iint(expression, variable):
    return sympy.integrate(expression, variable)
        
def dint(expression, lower_bound, upper_bound):
    summation = 0
    delta_x = math.fabs(upper_bound-lower_bound)/1000.0
    ##use trapezoidal rule to estimate the integral
    x_val_list = advanced_range_tool(lower_bound, upper_bound, delta_x)
    for x in x_val_list:
        try:
            a = eval(expression)
            x = x+delta_x
            b = eval(expression)
            summation +=((a+b)/2)*delta_x
        except:
            continue
    return summation

def val_function(expression, x):
    try:
        return (eval(expression))
    except:
        return None

def table_function_points(expression, lower_bound, upper_bound, delta_x): ##requires more work
    expression = replace_english(expression)
    table_of_values = []
    xs  = []
    ys = []
    x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
    for number in x_val_list:
        try:
            storage = round(val_function(expression,number),4)
        except:
            storage = val_function(expression, number)
        table_of_values.append([number, storage])
    for elements in table_of_values:
        xs.append(elements[0])
        ys.append(elements[1])
    return xs, ys

def gderiv(expression, lower_bound, upper_bound, y_lower_lim, y_upper_lim):
    graph(expression,lower_bound, upper_bound, y_lower_lim, y_upper_lim, "derivative")
    return 0

def graph(expression,lower_bound, upper_bound, y_lower_lim,y_upper_lim,graph_type="function"):
    delta_x = abs(lower_bound - upper_bound)/1000.0
    original_expression = expression
    x_values = []
    y_values = []
    if graph_type == "derivative":
        x_values, y_values = table_deriv_points(expression,lower_bound,upper_bound,delta_x)
    elif graph_type == "function":
        x_values, y_values = table_function_points(expression,lower_bound,upper_bound,delta_x)
    ax = plt.subplot2grid((1,1),(0,0))
    p1 = plt.plot(x_values, y_values)
    ax.set_ylim(y_lower_lim,y_upper_lim)
    ax.set_xlim(lower_bound,upper_bound)
    plt.vlines(0, -1000,1000)
    plt.hlines(0, -1000,1000)
    if graph_type == "derivative":
        function = "(d/dx)%s"%original_expression
    elif graph_type == "function":
        function = "f(x)=%s"%original_expression
    plt.legend(p1,[function])
    plt.show()
    return 0
    
        
def advanced_range_tool(lower_bound,upper_bound,delta_x): ##will assist in figuring a table of values for a function
    i = 0
    table_of_inputs=[]                                    
    while i < math.floor((upper_bound - lower_bound)/delta_x):
        try:
            intermediate_x = round((lower_bound + i*delta_x), 4)
        except:
            intermediate_x = lower_bound + i*delta_x
        table_of_inputs.append(intermediate_x)
        i = i+1
    return table_of_inputs

#you might want this to directly output via a textbox or something
def latex_out(s):
    text = sympy.latex( expr, mode='inline' )
    return text
#The GUI work is contained here.
# -*- coding: UTF-8-*-
try:
    from tkinter import *
except:
    from Tkinter import *
import webbrowser, os

helper = """\n
<required parameter>, [unrequired parameter]
nderiv(\"<expression>\",<point>,[accuracy])
dint(\"<expression>\",<left-bound>,<right-bound>)\t uses the trapezoidal approximation
gderiv(\"<expression>\",<left-bound>,<right-bound>,<screen_max_y>,<screen_min_y>)
graph(\"<expression>\",<left-bound>,<right-bound>,<screen_max_y>,<screen_min_y>)
>>>
"""

i = 0
def sec_back():
    global sec_status
    sec_status = False
    second_button.config(bg="#10186d",fg="#FFFFFF")
    
def plus_handler():
    clibox.insert(INSERT, "+")
    
def minus_handler():
    clibox.insert(INSERT, "-")
    
def multiply_handler():
    clibox.insert(INSERT, "*")
    
def divide_handler():
    clibox.insert(INSERT, "/")
    
def equals_handler():
    clibox.insert(INSERT, "=")
    
def handle_log():
    if sec_status == False:
        clibox.insert(INSERT, "ln(")
    else:
        clibox.insert(INSERT, "log(")
        sec_back()
        
def handle_exponential():
    if sec_status == False:
        clibox.insert(INSERT, "e^(")
    if sec_status == True:
        clibox.insert(INSERT, "10^(")
        sec_back()
        
def handle_power():
    if sec_status == False:
        clibox.insert(INSERT, "^")
    if sec_status == True:
        clibox.insert(INSERT, "sqrt(")
        sec_back()

def handle_help():
    clibox.insert(INSERT, helper)
    """
    if sec_status == False:
        clibox.insert(INSERT, helper)
    elif sec_status == True:
        directory = os.path.dirname(os.path.abspath(__file__)) 
        filename = os.path.join(directory, 'documentation.html')
        webbrowser.open(url=filename)
        sec_back()
    """
    
def second_handler():
    if sec_status == True:
        global sec_status
        sec_status = False
        second_button.config(bg="#10186d",fg="#FFFFFF")
    elif sec_status == False:
        global sec_status
        sec_status = True
        second_button.config(bg="#fef200",fg="#000000")
def integral_handler():
    clibox.insert(INSERT, "dint(")
    
def graph_handler():
    clibox.insert(INSERT, "graph(")
    
def deriv_handler():
    clibox.insert(INSERT, "gderiv(")
    
def init_formula():
    editor = Toplevel()
    editor.title("Formula Editor")
    def open_formula():
        fformula_name = filesavebox(msg=None, title=None, default='', filetypes=None)
        fformula = open(fformula_name, "rt")
        i = 0
        variables = {}
        for line in fformula:
            if i == 0:
                formula = line
            else:
                variables[line[0]] = line[line.find('=')+1:]
            i += 1
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
    
def handle_nderiv():
    if sec_status == False:
        clibox.insert(INSERT, "nderiv(")
    elif sec_status == True:
        init_formula()
        sec_back()

def handle_numpad(button):
    clibox.insert(INSERT,str(button))
    
def four_function_handler(button):
    clibox.insert(INSERT,str(button))
    
def interpret_input():
    s = clibox.get(1.0, END)
    last_cmd = s.rfind(">>>")
    com = s[last_cmd+3:]
    out = ""
    cmd = replace_english(com)
    if cmd.find("graph") >= 0:
        clibox.insert(END,"\n>>>")
        eval(cmd)
        return 0
    elif cmd.find("gderiv") >= 0:
        clibox.insert(END,"\n>>>")
        eval(cmd)
        return 0
    try:
        out = str(eval("".join(["(",cmd,")*1.0"])))
        clibox.insert(END, "\n%s"%out)
    except:
        try:
            clibox.insert(eval(cmd))
        except:
            eval(com)
    finally:
        clibox.insert(END, "\n>>>")
    return 0
def handle_graphs(button):
    clibox.insert(INSERT,str(button))
    
def handle_arrows(direction):
    index = str(clibox.index("insert"))
    placemark = index.find(".")
    line = int(index[0:placemark])
    column = int(index[placemark+1:])
    if direction == "up":
        clibox.mark_set("insert", "%d.%d" % (line - 1, column))
    if direction == "down":
        clibox.mark_set("insert", "%d.%d" % (line + 1, column))
    if direction == "left":
        clibox.mark_set("insert", "%d.%d" % (line, column -1))
    if direction == "right":
        clibox.mark_set("insert", "%d.%d" % (line, column + 1))
    return 0
    
def handle_clear():
    clibox.delete("1.0",END)
    clibox.insert(END,">>>")
    return 0
    
def handle_back():
    clibox.delete("%s-1c" % INSERT, INSERT)
    
def handle_vars():
    clibox.insert(INSERT,"x")
    """
    if sec_status == False:
        clibox.insert(INSERT,"x")
    elif sec_status == True:
        clibox.insert(INSERT,"let")
        sec_back()
    """
    
def handle_trig(s):
    s += "("
    if sec_status == False:
        clibox.insert(INSERT, s)
    elif sec_status == True:
        s = "arc" + s
        clibox.insert(INSERT, s)
        sec_back()

    
root = Tk()
root.wm_title("pyCalc")
frame = Frame(root)
frame.config(bg="#000000")
clibox = Text(frame)
clibox.grid(row=0,column=0, rowspan=5, columnspan=5)
clibox.config(bg="#c9c9b6", fg="#000000")
clibox.insert(END, ">>>")
clibox.mark_set("sentinel", INSERT)
clibox.mark_gravity("sentinel", LEFT)
dintegral = Button(frame, text="Definite Integral",command=integral_handler)
dintegral.grid(row=5,column=0, sticky=N+E+S+W, columnspan = 1)
dintegral.config(bg="#fef200",fg="#000000", state=NORMAL)
graph_button = Button(frame, text="Graph",command=lambda:handle_graphs("graph("))
graph_button.grid(row=5,column=1, sticky=N+E+S+W, columnspan = 1)
graph_button.config(bg="#fef200",fg="#000000")
deriv_button = Button(frame, text="Graph Derivative",command=lambda:handle_graphs("gderiv("))
deriv_button.grid(row=5, column=2, sticky=N+E+S+W, columnspan=1)
deriv_button.config(bg="#fef200",fg="#000000")
cderiv_button = Button(frame, text="Differentiate", command=lambda:handle_graphs("cderiv("))
cderiv_button.grid(row=5, column=3, sticky=N+E+S+W, columnspan=1)
cderiv_button.config(bg="#fef200",fg="#000000")
indef_button = Button(frame, text="Integrate", command=lambda:handle_graphs("iint("))
indef_button.grid(row=5, column=4, sticky=N+E+S+W, columnspan=1)
indef_button.config(bg="#fef200",fg="#000000")
about_text = Message(frame, text="Graphing Calculator\nPowered by Python 3.3",width=300)
about_text.grid(row=6, column=0, columnspan=5, sticky=N+E+S+W)
about_text.config(anchor=W, bg="#000000",fg="#FFFFFF")
second_button = Button(frame, text="2nd", command=second_handler)
second_button.grid(row=0, column=5, sticky=N+E+S+W)
second_button.config(bg="#10186d", fg="#FFFFFF")
sin_button = Button(frame, text="arcsin\nSIN",command=lambda:handle_trig("sin"))
sin_button.grid(row=0,column=6, sticky=N+E+S+W)
sin_button.config(bg="#10186d", fg="#FFFFFF")
cos_button = Button(frame, text="arccos\nCOS",command=lambda:handle_trig("cos"))
cos_button.grid(row=0, column=7, sticky=N+E+S+W)
cos_button.config(bg="#10186d", fg="#FFFFFF")
tan_button = Button(frame, text="arctan\nTAN",command=lambda:handle_trig("tan"))
tan_button.grid(row=0, column=8, sticky=N+E+S+W)
tan_button.config(bg="#10186d", fg="#FFFFFF")
seven = Button(frame, text=" 7 ", command=lambda:handle_numpad(7))
eight = Button(frame, text=" 8 ",command=lambda:handle_numpad(8))
nine = Button(frame, text=" 9 ",command=lambda:handle_numpad(9))
seven.grid(row=0, column=9, sticky=N+E+S+W)
eight.grid(row=0, column=10, sticky=N+E+S+W)
nine.grid(row=0, column=11, sticky=N+E+S+W)
seven.config(bg="#0a4a92", fg="#FFFFFF")
eight.config(bg="#0a4a92", fg="#FFFFFF")
nine.config(bg="#0a4a92", fg="#FFFFFF")
up_arrow = Button(frame, text="↑", command=lambda:handle_arrows("up"))
left_arrow = Button(frame, text="←", command=lambda:handle_arrows("left"))
right_arrow = Button(frame, text="→",command=lambda:handle_arrows("right"))
down_arrow = Button(frame, text="↓",command=lambda:handle_arrows("down"))
up_arrow.grid(row=1, column=6 , columnspan=2)
left_arrow.grid(row=2, column=5, columnspan=2)
right_arrow.grid(row=2, column=7, columnspan=2)
down_arrow.grid(row=3, column=6, columnspan=2)
up_arrow.config(bg="#524741", fg="#FFFFFF",padx=10,pady=10)
down_arrow.config(bg="#524741", fg="#FFFFFF",padx=10,pady=10)
left_arrow.config(bg="#524741", fg="#FFFFFF",padx=10,pady=10)
right_arrow.config(bg="#524741", fg="#FFFFFF", padx=10,pady=10)
four = Button(frame, text=" 4 ",command=lambda:handle_numpad(4))
five = Button(frame, text=" 5 ",command=lambda:handle_numpad(5))
six = Button(frame, text=" 6 ",command=lambda:handle_numpad(6))
four.grid(row=1, column=9, sticky=N+E+S+W)
five.grid(row=1, column=10, sticky=N+E+S+W)
six.grid(row=1, column=11, sticky=N+E+S+W)
four.config(bg="#0a4a92", fg="#FFFFFF")
five.config(bg="#0a4a92", fg="#FFFFFF")
six.config(bg="#0a4a92", fg="#FFFFFF")
one = Button(frame, text=" 1 ", padx=10,command=lambda:handle_numpad(1))
two = Button(frame, text=" 2 ", padx=10,command=lambda:handle_numpad(2))
three = Button(frame, text=" 3 ", padx=10,command=lambda:handle_numpad(3))
one.grid(row=2, column=9, sticky=N+E+S+W)
two.grid(row=2, column=10, sticky=N+E+S+W)
three.grid(row=2, column=11, sticky=N+E+S+W)
three.config(bg="#0a4a92", fg="#FFFFFF")
two.config(bg="#0a4a92", fg="#FFFFFF")
one.config(bg="#0a4a92", fg="#FFFFFF")
point = Button(frame, text=" . ",command= lambda:handle_numpad("."))
zero = Button(frame, text=" 0 ",command=lambda:handle_numpad(0))
negative = Button(frame, text=" (-) ",command=lambda:handle_numpad("-"))
point.grid(row=3, column=9, sticky=N+E+S+W)
zero.grid(row=3, column=10, sticky=N+E+S+W)
negative.grid(row=3, column=11, sticky=N+E+S+W)
point.config(bg="#0a4a92", fg="#FFFFFF")
zero.config(bg="#0a4a92", fg="#FFFFFF")
negative.config(bg="#0a4a92", fg="#FFFFFF")
                
#intitalize function pad row 1
help_button = Button(frame, text="HELP", command=handle_help)
function2 = Button(frame, text="(", command=lambda:handle_graphs("("))
function3 = Button(frame, text=")", command=lambda:handle_graphs(")"))
function4 = Button(frame, text="nDeriv(", command=handle_nderiv)
#row 2
logORln_button = Button(frame, text="log\nLN", command=handle_log)
exponential_button=Button(frame,text="10^x\ne^x", command=handle_exponential)
power_button=Button(frame,text="sqrt\nX^Y", command=handle_power)
function5 = Button(frame, text="CLEAR", command=handle_clear)
#row 3
function6 = Button(frame, text="DEL", command=handle_back)
program_button = Button(frame, text="PRGM", state=DISABLED)
x_var_button = Button(frame, text="X", command=handle_vars)
mode_button = Button(frame, text="MODE", state = DISABLED)
#grid function pad elements
help_button.grid(row=4, column=5, sticky=N+E+S+W)
function2.grid(row=4, column=6, sticky=N+E+S+W)
function3.grid(row=4, column=7, sticky=N+E+S+W)
function4.grid(row=4, column=8, sticky=N+E+S+W)
logORln_button.grid(row=5, column=5, sticky=N+E+S+W)
exponential_button.grid(row=5, column=6, sticky=N+E+S+W)
power_button.grid(row=5, column=7, sticky=N+E+S+W)
function5.grid(row=5, column=8, sticky=N+E+S+W)
function6.grid(row=6, column=8, sticky=N+E+S+W)
program_button.grid(row=6, column=6, sticky=N+E+S+W)
x_var_button.grid(row=6, column=7, sticky=N+E+S+W)
mode_button.grid(row=6, column=5, sticky=N+E+S+W)
#configure function pad elements
help_button.config(bg="#006fae", fg="#FFFFFF")
function2.config(bg="#006fae", fg="#FFFFFF")
function3.config(bg="#006fae", fg="#FFFFFF")
function4.config(bg="#006fae", fg="#FFFFFF")
function5.config(bg="#524741", fg="#FFFFFF")
function6.config(bg="#524741", fg="#FFFFFF")
logORln_button.config(bg="#006fae", fg="#FFFFFF")
exponential_button.config(bg="#006fae", fg="#FFFFFF")
program_button.config(bg="#006fae", fg="#FFFFFF")
x_var_button.config(bg="#006fae", fg="#FFFFFF")
mode_button.config(bg="#006fae", fg="#FFFFFF")
power_button.config(bg="#006fae", fg="#FFFFFF")

#initialize four-function elements
minus_button = Button(frame, text="-", command=minus_handler)
plus_button = Button(frame, text="+", command=plus_handler)
division_button = Button(frame, text="/", command=divide_handler)
multiplication_button = Button(frame, text="*", command=multiply_handler)
enter_button = Button(frame, text="ENTER\n↵", command=interpret_input)
equals_button = Button(frame,text="",state=DISABLED)

#grid four-function elements
enter_button.grid(row=4,column=9,columnspan=3,sticky=N+E+S+W)
plus_button.grid(row=5,column=9,sticky=N+E+S+W)
minus_button.grid(row=6,column=9,sticky=N+E+S+W)
equals_button.grid(row=5,column=11,sticky=N+E+S+W,rowspan=2)
multiplication_button.grid(row=5,column=10,sticky=N+E+S+W)
division_button.grid(row=6,column=10,sticky=N+E+S+W)

#configure four-function elements
enter_button.config(bg="#524741", fg="#FFFFFF")
plus_button.config(bg="#524741", fg="#FFFFFF")
minus_button.config(bg="#524741", fg="#FFFFFF")
equals_button.config(bg="#524741", fg="#FFFFFF")
multiplication_button.config(bg="#524741", fg="#FFFFFF")
division_button.config(bg="#524741", fg="#FFFFFF")

frame.pack()

root.mainloop()