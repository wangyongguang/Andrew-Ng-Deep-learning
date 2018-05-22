import numpy as np
def normalizeRows(x):
    """
    implement a function that normalizes each row of the matrix x(to have unit length)
    :param x: --A numpy matrix of shape(n,m)
    :return: The normalized (by row) numpy matrix,you are allowed to modify x.
    """
    x_norm = np.linalg.norm(x,axis=1,keepdims=True) #计算每一行长度，得到一个列向量
    #divide x by its norm
    x = x/x_norm #利用numpy的广播，用矩阵与列向量相除
    print("x_norm=",x_norm)
    return x
x = np.array([[0,3,4],[1,6,4]])
print("normalizeRows(x)=",str(normalizeRows(x)))