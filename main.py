import math
from types import *

def replace_english(expression):
    replacement_tables = [["^","**"],["sin(","math.sin("],["cos(","math.cos("],["tan(","math.tan("],
                          ["cot(","math.cot("],["sec(","math.sec("],["csc(","math.csc("],["[[","math.floor("],
                          ["]]",")"]]
    for replacements in replacement_tables:
        old = replacements[0]
        new = replacements[1]
        expression = expression.replace(old,new)
    return expression

def find_terms(expression):
    infix_operation_indices = ["+","-","*","/"] ##items which will separate terms
    prefix_operation_indices = ["math.sin(","math.cos(","(","math.tan(","math.cot(","math.sec(","math.csc(","log("]
    postfix_operation_indices = [")"]
    infix_location = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == infix_operation_indices:
            infix_location.append(char)

def nDeriv(expression, x, h):
    """:finds the numerical derivative at a certain point, n, while h is the accuracy of the derivative calc, the lower the better
:uses f'(n)= (f(x+h) - f(x-h))/(2h)"""
    try:
        deriv_expression_a = expression.replace("x", "(x+h)")
        deriv_expression_b = expression.replace("x", "(x-h)")
        solution =((eval(deriv_expression_a))-(eval(deriv_expression_b)))/(2*h)
    except:
        solution = "DNE"
    return solution

def table_function_points(expression, lower_bound, upper_bound, delta_x): ##requires more work
    expression = replace_english(expression)
    print (expression)
    table_of_values = []
    try: #may fail if either lower_bound, upper_bound, or delta_x are floats
        for numbers in range(lower_bound,upper_bound+1, delta_x):
            try:
                storage = round(nDeriv(expression, number),4)
            except:
                storage = nDeriv(expression, number)
            table_of_values.append([numbers, storage])
    except:#will run an advanced list-making tool
        x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
        for number in x_val_list:
            try:
                storage = round(nDeriv(expression,number),4)
            except:
                storage = nDeriv(expression, number)
            table_of_values.append([number, storage])
    return table_of_values

def val_function(expression, x):
    try:
        return (eval(expression))
    except:
        return "DNE"

def table_function_points(expression, lower_bound, upper_bound, delta_x): ##requires more work
    expression = replace_english(expression)
    print (expression)
    table_of_values = []
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
    return table_of_values

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

print(table_function_points("[[x]]",0,10,.1))
