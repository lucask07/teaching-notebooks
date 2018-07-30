import numpy as np
from sympy import *


def check_lambdify_out(data, *args):
    """
    If lambdify returns a constant vector field the shape will be () 
    [i.e. a single scalar]. This function expands the shape of the output
    to match the shape of input vectors passed by *args [i.e. x,y,z]
    """
    if not np.shape(data):
        return data*np.ones([len(x) for x in args])
    elif np.shape(data) != tuple([len(x) for x in args]):
        print('Error: Data is not a constant and not the same shape as input')
        return data
    elif  np.shape(data) == tuple([len(x) for x in args]):
        return data
    else: 
        print("No idea! We shouldn't get here")

def evaluate_field_components(A, field, X, Y, Z):
    c_eval = {}     
    vars = symbols('A.x A.y A.z')  # this is to fix a lambdify "bug" 
    for c in field.components:
        print(c)
        l_func = lambdify(vars, field.components[c].subs(dict(zip([A.x, A.y, A.z], vars))), modules='numpy')
        c_eval[c] = l_func(X,Y,Z)
    return (c_eval[A.i], c_eval[A.j], c_eval[A.k])