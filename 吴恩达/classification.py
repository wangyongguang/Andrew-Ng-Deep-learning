import numpy as np
import matplotlib.pyplot as plt
w = np.array([[1/2],[1/2]]) #
x = np.array([[1,2,3],[4,5,6]])
print("x=",x)
b = np.array([1/2,1/2,1/2])
print("w=",w)
print("b=",b)
z = np.dot(w.T,x)+b
print("z=",z)
A = 1/(1+1/np.exp(z))
print("A=",A)
Y = [1,0,1]
#单次迭代梯度下降算法流程
dz = A-Y
dw = 1/3*np.dot(x,dz.T)
db = 1/3*np.sum(dz)
print("dw=",dw)
print("db=",db)
alpha = 0.01
w = w-alpha*dw
b = b-alpha*db
print("w=",w)
print("b=",b)
z = np.dot(w.T,x)+b
print("z=",z)


#以下是sigmoid函数图形
x1 = np.arange(-5,5,0.1)
y1 = 1/(1+1/np.exp(x1))
plt.plot(x1,y1)
plt.title('matplotlib')
plt.xlabel("x1")
plt.ylabel("sigmoid(x1)")
plt.show()