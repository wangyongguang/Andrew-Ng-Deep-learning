import numpy as np
"""
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.

    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
def sigmoid_derivative(x):
    s = 1/(1+1/np.exp(x))
    ds = s*(1-s)
    return ds

x = np.array([1,2,3])
print("sigmoid_derivative(x)="+str(sigmoid_derivative(x)))
