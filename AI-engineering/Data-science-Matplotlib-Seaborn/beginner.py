import matplotlib.pyplot as plt


# x = [1,2,3,4,5]
# y = [10,25,35,45,50]
# plt.plot(x,y)
#
# plt.show()

#LINE PLOT
plt.plot([1,2,3,4], [5,6,7,8], label = 'Line-Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()