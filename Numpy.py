import numpy as np


# list into array.


'''
mylist = [2,4,6,8,10]

arr1 = np.array( mylist )
print(arr1)
'''

'''
mytuple = (2,4,6,8,10)

arr1 = np.array( mytuple )
print( type(arr1))
'''

# type promotion :

'''
arr1 = np.array( [10, 20, 30, 40, 50,2.3] )
print( arr1 )
'''

# 0-D 1-D 2-D
# ndim

'''
arr1 = np.aarray(7)
print( arr1.ndim )
'''

'''
arr1 = np.array( [5,10,15,20] )
print( arr1.ndim)
'''

'''
1 2 3
4 5 6
7 8 9
'''

'''
mylist = [ [1,2,3] , [4,5,6] , [7,8,9] ]
arr = np.array( mylist )
print(arr)

print(arr.ndim)
'''
'''
arr1 = np.array( [5,10,15,20] )
print( arr1[0])
print( arr1[-1])
print(arr[1:3])
'''

'''
arr1 = np.array( [5,10,15,20] )
arr1[0] = 90
print(arr1)
'''

#shape | size | datatype

'''
mylist = [ [1,2,3] , [4,5,6] , [7,8,9] ]
arr = np.array ( mylist )


print( arr.shape )
print( arr.size )
print( arr.dtype )
'''


# 64 bits :
# 1 byte = 8 bits
# 8 byte = 64 bits

# indexing in 2-D Array :


'''

0    1    2

10 20 30    0 th row
40 50 60
70 80 90

[0,2]
[2,0]
'''

'''
mylist = [ [10,20,30] , [40,50,60] , [70,80,90] ]

arr1 = np.array( mylist )

#print( arr[0,2] )
#print(arr1[2,0] )
'''

'''
mylist = [ [10,20,30] , [40,50,60] , [70,80,90] ]

arr1 = np.array( mylist )

print( arr1[0,] )
print ( arr[1,])
print ( arr[:,0])
'''

'''
arr1 = np.array ( [2,4,6,8,10] )

print(arr1 * 3)

print(arr1 + 3)

print(arr1 - 3)
'''


'''
mylist = [2,4,6]

print( mylist * 3)
'''

'''
arr1 = np.array ( [10,20,30,40] )
arr2 = np.array ( [5,10,15,20] )

print( arr1 + arr2 )
'''

#transpose :

'''
mylist = [ [10,20,30] , [40,50,60] , [70,80,90] ]

arr1 = np .array( mylist )

print( arr1.T)
'''

# copy and view :

#copy :

'''
arr = np.array( [10,20,30,40] )

x = arr.copy()

print("x = ", x)
print("arr = ",arr)

arr[0] = 90

print("x = ", x)
print("arr = ",arr)
'''


'''

arr = np.array( [10,20,30,40] )
x = arr.view()

print("x = ", x)
print("arr = ",arr)

arr[0] = 90

print("x = ", x)
print("arr = ",arr)
'''


'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print( arr.shape )
'''


'''
arr = np.array( [1, 2, 3] , [4, 5, 6] , [7, 8, 9])

for x  in arr:
    print(x)

# [1 2 3 4 5 6 7 8 9]

# [1 2 3]
# [4 5 6] 
# [7 8 9]
'''












