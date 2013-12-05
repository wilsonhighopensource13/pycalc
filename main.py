<<<<<<< HEAD
import math
import matplotlib.pyplot as plt
=======
import math, matplotlib.pyplot as plt
from types import *
>>>>>>> 874d088d72b993ee876f28c5b36e97d692ad10ea

def replace_english(expression):
    replacement_tables = [["^","**"],["sin(","math.sin("],["cos(","math.cos("],["tan(","math.tan("],
                          ["cot(","math.cot("],["sec(","math.sec("],["csc(","math.csc("],["[[","math.floor("],["]]",")"]]
    for replacements in replacement_tables:
        old = replacements[0]
        new = replacements[1]
        expression = expression.replace(old,new)
    return expression

def find_terms(expression):
<<<<<<< HEAD
    log_signs_locations = {}
    infix_operation_indices = ["+","-","*","**","/"]
    #prefix_operation_indices = ["math.sin(","math.cos(","(","math.tan(","math.cot(","math.sec(","math.csc(","log("]
    #postfix_operation_indices = [")"]
    i = 0
    indicator = 0
    while i < len(expression):
        for indices in infix_operation_indices:
            if expression[i] == indices:
                indicator += 1
                log_signs_locations[indices] = [log_signs_locations[indices]].append(i)
            
    return log_signs_locations
            #if char == infix_operation_indices[0] 
    
=======
    infix_operation_indices = ["+","-","*","/"] ##items which will separate terms
    prefix_operation_indices = ["math.sin(","math.cos(","(","math.tan(","math.cot(","math.sec(","math.csc(","log("]
    postfix_operation_indices = [")"]
    infix_location = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == infix_operation_indices:
            infix_location.append(char)
>>>>>>> f07f23a329b8309b3179e2883b3b3e3f003e4421

def nDeriv(expression, x, h):
    """:finds the numerical derivative at a certain point, n, while h is the accuracy of the derivative calc, the lower the better
:uses f'(n)= (f(x+h) - f(x-h))/(2h)"""
    try:
        deriv_expression_a = expression.replace("x", "(x+h)")
        deriv_expression_b = expression.replace("x", "(x-h)")
        solution =((eval(deriv_expression_a))-(eval(deriv_expression_b)))/(2*h)
    except:
        solution = 0
    return solution

def table_deriv_points(expression, lower_bound, upper_bound, delta_x): ##finds all of the values of a function's derivatives
    #(on the increment delta_x) in domain: [lowerbound,upperbound]
    table_of_values = []
    try: #may fail if either lower_bound, upper_bound, or delta_x are floats
        for numbers in range(lower_bound,upper_bound+1, delta_x):
            try:
                storage= round(nDeriv(expression, numbers, .0001,4))
            except:
                storage = nDeriv(expression, numbers, .0001)
            table_of_values.append([numbers, storage])
    except:#will run an advanced list-making tool
        x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
        for number in x_val_list:
            try:
                storage = round(nDeriv(expression, number, .0001,4))
            except:
                storage = nDeriv(expression, number, .0001)
            table_of_values.append([number, storage])
    return table_of_values

def val_function(expression, x):
    try:
        return (eval(expression))
    except:
        return None

def table_function_points(expression, lower_bound, upper_bound, delta_x): ##requires more work
    expression = replace_english(expression)
    print (expression)
    table_of_values = []
    xs  = []
    ys = []
    try: #may fail if either lower_bound, upper_bound, or delta_x are floats
        for numbers in range(lower_bound,upper_bound+1, delta_x):
            try:
                storage = round(val_function(expression, number),4)
            except:
                storage = val_function(expression, number)
            table_of_values.append([numbers, storage])
    except:#will run an advanced list-making tool
        x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
        for number in x_val_list:
            try:
                storage = round(val_function(expression,number),4)
            except:
                storage = val_function(expression, number)
            table_of_values.append([number, storage])
<<<<<<< HEAD
    for elements in table_of_values:
        xs.append(elements[0])
        ys.append(elements[1])
    return xs, ys

def graph(expression, lower_bound, upper_bound, delta_x):
    x_values, y_values = table_function_points(expression, lower_bound, upper_bound, delta_x)
    for y in y_values:
        if y == "DNE":
            y = None
    plt.plot(x_values,y_values)
    plt.show()

=======
    return table_of_values
    
def graph(expression,Type,lower_bound, upper_bound, delta_x):
    x_values = []
    y_values = []
    if Type == "deriv":
        table_of_values = table_deriv_points(expression,lower_bound, upper_bound,delta_x)
        for elements in table_of_values:
            x_values.append(elements[0])
            y_values.append(elements[1])
        plt.plot(x_values, y_values)
        plt.show()
    elif Type == "function":
        table_of_values = table_function_points(expression,lower_bound,upper_bound,delta_x)
        for elements in table_of_values:
            x_values.append(elements[0])
            y_values.append(elements[1])
        plt.plot(x_values, y_values)
        plt.show()
        
>>>>>>> 874d088d72b993ee876f28c5b36e97d692ad10ea
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
<<<<<<< HEAD
=======

<<<<<<< HEAD
print(table_deriv_points("",lower,upper,))
=======
graph("x**2","deriv",-10,10,.1)
graph("x**2","function",-10,10,.1)
>>>>>>> 874d088d72b993ee876f28c5b36e97d692ad10ea
>>>>>>> f07f23a329b8309b3179e2883b3b3e3f003e4421
