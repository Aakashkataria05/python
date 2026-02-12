import numpy as np
numpy_array = np.array([1,2,3,4,5])
# print(numpy_array)

# ones_array = np.ones((2,3))
# print(ones_array)

# filled_array = np.full((2,4),9)
# print(filled_array.shape)
# print(filled_array.size)
# print(filled_array.astype(str))

# new_arr = np.insert(numpy_array, 3, 100)
# print(new_arr)

# arr1 = np.array([5,6,7])
arr2 = np.array([5,4,3])

result = arr1 + arr2
print(result)

sis = np.full((3,4),4)
print(sis)
print(np.arange(0,100,2))
print(np.linspace(0,1000,5))

myarr = np.array([[1,2,3,4],[5,6,7,8],[9,1,23,3]])
print(myarr)
print(myarr.reshape(4,3))

myarr2 = np.array([1.2, 1.6, 2.9, 3.5])
print(myarr2.astype(int))

print(myarr[myarr % 2 == 0])

myarr3 = np.array([1,2,3,4,5,6,7,8,9])
print(myarr3.reshape(3,3))
print(myarr3[myarr3>3])
