# Numerical Python aka Numpy

import numpy as np

datap = np.array([1,2,3,4,5])
#print(datap)
dataq = np.zeros((2,3))
#print(dataq)

datas = np.arange(1,20,3)
#print(datas)

# evenly space arrange
datay = np.linspace(1,5,10)
#print(datay)

# Manipulating Arrays



#eLEMENT-wise oPERATIONS

data1 = np.array([1,2,3,4,5])
data2 = np.array([1,2,3,4,5])
data3 = np.array([4, 16, 25])

#print(data1 + data2)
#print(data1 * data2)

#print(np.sqrt(data3))
#print(np.max(data3))
#print(np.min(data3))


#SLICING IN ARRAY
data4 = np.array([1,2,3,4,5])
#print(data4[3:])
#print(data4[:3])
#print(data4[:])

#RESHAPED AN ARRAY
#
# data5 = np.array([6,7,8,9,10,11])
# print(data5.reshape(3,2))


#EXERCISE 1 Generate array for basic mathematical exercises

# arr1 = np.arange(1,6)
# arr2 = np.arange(6, 11)
#
# #print("ADD", arr1 + arr2)
# #print("SUB", arr1 - arr2)
# #print("MUL", arr1 * arr2)
#
# #EXERCISE 2 Generate A 3X3 matric and perform mathematical exercises
#
# arr3 = np.array([[1,2,3,], [4,5,6], [7,8,9]])
# print(arr3)