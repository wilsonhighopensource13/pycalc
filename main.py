import math

def replace_english(expression):
    expression.replace("^","**")
    return expression

def find_terms(expression):
    #finds the terms in an expression and puts them into a list, to be used to 
    #create a derivative of a function at all points
    operator_list = ["+","-","/","*","^"]
    

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

def table_deriv_points(expression, lower_bound, upper_bound, delta_x): ##finds all of the values of a function's derivative (on the increment delta_x) in domain: [lowerbound,upperbound]
    table_of_values = []
    try: #may fail if either lower_bound, upper_bound, or delta_x are floats
        for numbers in range(lower_bound,upper_bound+1, delta_x):
            try:
                storage= round(nDeriv(expression, numbers, .0001),4)
            except:
                storage = nDeriv(expression, numbers, .0001)
            table_of_values.append([numbers, storage])
    except:#will run an advanced list-making tool
        x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
        for number in x_val_list:
            try:
                storage = round(nDeriv(expression, number, .0001),4)
            except:
                storage = nDeriv(expression, number, .0001)
            table_of_values.append([number, storage])
    return table_of_values

def val_function(expression, x):
    try:
        return eval(expression)
    except:
        return "DNE"

def table_function_points(expression, lower_bound, upper_bound, delta_x): ##requires more work
    expression = replace_english()
    table_of_values = []
    storage_float = 0
    storage_string = ""
    try: #may fail if either lower_bound, upper_bound, or delta_x are floats
        for numbers in range(lower_bound,upper_bound+1, delta_x):
            try: storage = round(val_function(expression, number),4)
            except: storage = val_function(expression, number)
            table_of_values.append([numbers, storage])
    except:#will run an advanced list-making tool
        x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
        for number in x_val_list:
            try: storage = round(val_function(expression, number),4)
            except: storage = val_function(expression, number)
            table_of_values.append([number, storage])
    return table_of_values

def advanced_range_tool(lower_bound,upper_bound,delta_x): ##will assist in figuring a table of values for a function
    i = 0
    table_of_inputs=[]
    while i < math.floor((upper_bound - lower_bound)/delta_x):
        intermediate_x = lower_bound + i*delta_x
        table_of_inputs.append(intermediate_x)
        i = i+1
    return table_of_inputs

print (table_function_points("x^2", -10, 10, .25))
