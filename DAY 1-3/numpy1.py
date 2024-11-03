import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arr3=arr1+arr2
print(arr3)

arr4=arr2-arr1
print(arr4)
print(arr3*arr4)

#2d array
arr_2d=np.array([1,2,3,4,5,6])
print(np.prod(arr_2d))#product of the array
print(np.min(arr_2d))# minimum value of the array
print(np.max(arr_2d))#max value 
print(np.exp(arr_2d))
print(np.log(arr_2d))
print(np.log10(arr_2d))
#slicing
print(arr_2d[0:3])
reshaped_array=arr_2d.reshape(3,2)
print(reshaped_array)
print(np.sum(reshaped_array,axis=0))#row
print(np.sum(reshaped_array,axis=1))#column

flatten_array=arr_2d.flatten()
print(flatten_array)
#sum,mean,standard deviation
print(np.sum(arr_2d))
print(np.mean(arr_2d))
print(np.std(arr_2d))
print(np.sin(arr_2d))

arr5=np.zeros((3,4))
arr6=np.ones((5,6))
arr7=np.full((4,5),86)
print("zeros are\n",arr5)
print(arr6)
print(arr7)

arrang1=np.arange(4,200,4)
print(arrang1)
linespace1=np.linspace(4,5,10)
print(linespace1)

matrix = np.array([[1, 2], [3, 4]])
vector = np.array([1, 0])

# Matrix-vector multiplication
print(np.dot(matrix, vector))  # Output: [1 3]

# Matrix transpose
print(matrix.T)  # Output: [[1 3] [2 4]]

arr = np.array([1, 2, 3, 4])

# Check for elements greater than 2
print(arr > 2)  # Output: [False False  True  True]

random1=np.random.randint(3,400,size=(4,4))
print(random1)

random2=np.random.rand(3,4)
print(random2)