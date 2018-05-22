import numpy as np
def softmax(x):
    """
    Calculates the softmax for each row of the input x.
    your code should work for a row vector and also for matrices of shape(n,m)
    :param x: A numpy matrix of shape(n,m)
    :return: A numpy matrix equal to the softmax of x,of shape(n,m)
    """
    #apply exp() element-wise(逐个元素) to x. use np.exp().
    x_exp = np.exp(x)
    # axis=1表示按行处理，求多个行向量的范数，keepdims是否保持矩阵的二维特性
    x_sum = np.sum(x_exp,axis=1,keepdims=True)
    s = x_exp/x_sum
    print("x_sum=",x_sum)
    return s
x = np.array([[0,3,4],[1,6,4]])
print("softmax=",str(softmax(x)))
