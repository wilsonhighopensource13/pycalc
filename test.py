import math
import matplotlib.pyplot as plt

def nderiv(expression, x, h=0.001):
    """:finds the numerical derivative at a certain point, n, while h is the accuracy of the derivative calc, the lower the better
:uses f'(n)= (f(x+h) - f(x-h))/(2h)"""
    try:
        deriv_expression_a = expression.replace("x", "(x+h)")
        deriv_expression_b = expression.replace("x", "(x-h)")
        
        solution =(eval(deriv_expression_a)-eval(deriv_expression_b))/(2*h)
    except:
        solution = None
    return solution

def table_deriv_points(expression, lower_bound, upper_bound, delta_x): ##finds all of the values of a function's derivatives
    print(expression,lower_bound,upper_bound,delta_x)
    #(on the increment delta_x) in domain: [lowerbound,upperbound]
    #expression = replace_english(expression)
    table_of_values = []
    x_val_list = advanced_range_tool(lower_bound,upper_bound,delta_x)
    for number in x_val_list:
        try:
            storage = round(nderiv(expression, number, .0001))
        except:
            storage = nderiv(expression, number, .0001)
        table_of_values.append([number, storage])
    xs = []
    ys = []
    for elements in table_of_values:
        xs.append(elements[0])
        ys.append(elements[1])
    return xs, ys

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
print(nderiv("x**2", 1))
