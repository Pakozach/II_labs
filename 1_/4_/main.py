import math as m
import statistics as stat
import random
import matplotlib.pyplot as plt

#1
# m = [round(random.random(), 2) for i in range(10)]
# print(m)
# print(stat.mean(m))
# print(stat.median(m))
#
# # h (height) and w (weight) data
# h = [range(len(m))]
# w = m
#
# # plot a scatter plot
# plt.scatter(h, w)
# plt.savefig('plot.png')
# # plt.show()

def func_y1(x):
    y = m.sqrt(1 + m.e**m.sqrt(x) + m.cos(x**2)) / abs(1 - m.sin(x)**3) + m.log(abs(2*x))
    return y


l = [round(func_y1(i), 3) for i in range(1, 11)]
print(l)
sl = l[:len(l)//2:]
print(sl)
# h (height) and w (weight) data
h = [i for i in range(1, len(sl)+1)]
w = sl

# plot a scatter plot
plt.scatter(h, w)
plt.savefig('plot1.png')

plt.cla()
# h (height) and w (weight) data
h = [i for i in range(1, len(l)+1)]
w = l


# plot a scatter plot
plt.plot(h, w)
plt.savefig('plot2.png')