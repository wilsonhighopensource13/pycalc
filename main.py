import math
import matplotlib.pyplot as plt
def replace_english(expression):
    replacement_tables = [["^","**"],["sin(","math.sin("],["cos(","math.cos("],["tan(","math.tan("],
                          ["cot(","math.cot("],["sec(","math.sec("],["csc(","math.csc("],["[[","math.floor("],["]]",")"],
                          ["arccos(","math.acos("],["sqrt(","math.sqrt("]]
    variable = "x"
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for replacements in replacement_tables:
        old = replacements[0]
        new = replacements[1]
        expression = expression.replace(old,new)
    for i in range(0,len(expression)-1):
        if (expression[i] in digits or expression[i] == variable) and (expression[i+1] in digits or expression[i+1] == variable):
	   expression.join([expression[0:i], "*", expression[i:]])
    return expression

def find_terms(expression):
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
        if solution >= 100000000:
            solution = None
    except:
        solution = None
    return solution

def table_deriv_points(expression, lower_bound, upper_bound, delta_x): ##finds all of the values of a function's derivatives
    #(on the increment delta_x) in domain: [lowerbound,upperbound]
    expression = replace_english(expression)
    table_of_values = []
    try: #may fail if either lower_bound, upper_bound, or delta_x are floats
        for numbers in range(lower_bound,upper_bound+1, delta_x):
            try:
                storage= round(nDeriv(expression, numbers, .0000001,4))
            except:
                storage = nDeriv(expression, numbers, .0001)
            table_of_values.append([numbers, storage])
    except:#will run an advanced list-making tool
        x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
        for number in x_val_list:
            try:
                storage = round(nDeriv(expression, number, .0000001,4))
            except:
                storage = nDeriv(expression, number, .0001)
            if expression.find("math.floor") or expression.find("floor") and storage > 0:
                storage = None
            table_of_values.append([number, storage])
    xs = []
    ys = []
    for elements in table_of_values:
        xs.append(elements[0])
        ys.append(elements[1])
    return xs, ys
        

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
    for elements in table_of_values:
        xs.append(elements[0])
        ys.append(elements[1])
    return xs, ys

  
def graph(expression,graph_type,lower_bound, upper_bound, delta_x,y_lower_lim,y_upper_lim):
    x_values = []
    y_values = []
    if graph_type == "deriv":
        x_values, y_values = table_deriv_points(expression,lower_bound,upper_bound,delta_x)
    elif graph_type == "function":
        x_values, y_values = table_function_points(expression,lower_bound,upper_bound,delta_x)
    ax = plt.subplot2grid((1,1),(0,0))
    p1 = plt.plot(x_values, y_values)
    ax.set_ylim(y_lower_lim,y_upper_lim)
    ax.set_xlim(lower_bound,upper_bound)
    plt.vlines(0, -1000,1000)
    plt.hlines(0, -1000,1000)
    if graph_type == "deriv":
        function = "(d/dx)%s"%expression
    elif graph_type == "function":
        function = "f(x)=%s"%expression
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
    
graph("10x","function",-10,10,.01,-10,10)