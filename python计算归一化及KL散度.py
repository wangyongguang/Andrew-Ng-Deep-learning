import numpy as np
import scipy.stats

x = [np.random.randint(1,11) for i in range(10)]
print(x)
print(np.sum(x))
px = x/np.sum(x) #归一化
print(px)
print("-------------------------------------------------------------------------")

y = [np.random.randint(1,11) for i in range(10)]
print(y)
print(np.sum(y))
py = y/np.sum(y) #归一化
print(py)
print("-------------------------------------------------------------------------")
##scipy计算函数可以处理非归一化情况，因此两个分布如x和y或px和py散度计算可以使用
# scipy.stats.entropy(x,y)或#scipy.stats.entropy(px,py)均可
KL = scipy.stats.entropy(x,y) #这里x,y没有归一化
print(KL)
print("-------------------------------------------------------------------------")

#自己编程实现
kl = 0.0
for i in range(10):
    kl +=px[i] * np.log(px[i]/py[i])
print(kl)
print("-------------------------------------------------------------------------")