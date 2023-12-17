#what is numpy?
#the numpy library is popular open-soures python libarary fro numerical python
#pip install numpy
"""
list in numpy is a numpy  arrry homogeneous
"""

#create nd-array-------one dimensional
import numpy as np
arr=np.array([10,20,30,40])
arr           #[10, 20, 30, 40]

#create multi-dimensional arry
arr=np.array([[2,4,6,8,],[1,3,6,9]])
arr
"""
[[2, 4, 6, 8],
[1, 3, 6, 9]]
"""
#convert one dimensionl to multi
arr=np.array([10,20,30,40],ndmin=3)     #ndmin=3
arr         #[[[10, 20, 30, 40]]]

#convert into complex 
arr=np.array([1,2,3,4,5],dtype=complex)
arr        #[1.+0.j, 2.+0.j, 3.+0.j, 4.+0.j, 5.+0.j]

#check dimensions
arr=np.array([[[1,2,3,4],[2,4,6,8],[1,3,6,9]]])
print(arr.ndim)  #3

#find size of each item in array
arr=np.array([1,2,3,4,5])
arr.itemsize  #4

#find type of array
arr=np.array([1,2,3,4,5])
arr.dtype #dtype('int32')

#find shape and size of array
arr=np.array([[[1,2,3,4],[2,4,6,8],[1,3,6,9]]])
arr.shape   #(1, 3, 4)
arr.size    #12

#create array in range
arr=np.arange(10)
arr     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#.............................................................................

#acces value form one dimensional
arr=np.arange(10)
arr[2]  #2

#acces last element one dimensional
arr[-1]  #9

#....................................................................................
#multi-dimensional

arr=np.array([[1,2,3,4,5],[2,3,4,5,6]])
arr
"""
[[1, 2, 3, 4, 5],
 [2, 3, 4, 5, 6]]
"""
arr.shape #(2, 5) -----(dimensional_size,elements_size)

#access 5 from2  
arr[1,3] 

#acess 5 from 1
arr[0,4]

#acces 6 from 2
arr[1,-1]

#acces ele using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
arr[1:8:2] #[3, 5, 7, 9] -----------------start:end:step

arr[-2:3:-1]  #[13, 12, 11, 10,  9,  8,  7,  6]
#...................................................................................

#indixing in numpy

mul_arr=np.array( [  [10,20,30,40],
                     [50,60,70,80],
                     [90,100,110,120],
                     [130,140,150,160]])
#slicling array
#access elements
mul_arr[1,2]  #70

mul_arr[1,:]   #[50, 60, 70, 80]   #on---row
  
mul_arr[:,1]  #[ 20,  60, 100, 140]   #on-----col

mul_arr[1:3,1:3]  #(row_star : row_end   ,  col_start : col_end)
"""
      [[ 60,  70],
       [100, 110]]

"""
mul_arr[1:3,2:4]



#interger array indexing
arr=np.arange(35).reshape(5,7)
arr
"""
      [[ 0,  1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12, 13],
       [14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27],
       [28, 29, 30, 31, 32, 33, 34]]
"""

#booolen array indexing
arr=np.arange(12).reshape(3,4)
arr
"""
      [[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]]
"""
rows=np.array([False,True,True]) #on row
want_array=arr[rows,:]
want_array
"""
      [[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]]  
"""
#..............................................................................

#convert one dimensional array to  list
arr=np.array([1,2,3,4,5])
arr
type(arr) #ndarray
list_1=arr.tolist()  #-----------.tolist()
list_1
type(list_1)   #list

#convert multi dimensional array to  list
arr=np.arange(16).reshape(4,4)
arr
"""
      [[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]]
"""

type(arr) #array
lsit_2=arr.tolist()
lsit_2  #[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

#..............................................................................
#convert lsit to array
list1=[1,2,3,4,5]  #list --------------- .array()
arr=np.array(list1)
arr  #array([1, 2, 3, 4, 5])



list1=[1,2,3,4,5]  #list
arr=np.asarray(list1) #-----------------.asarray()
arr  #array([1, 2, 3, 4, 5])


#......................................................................................
arr=np.array([[1,2,3],
              [4,5,6]])
arr.shape
arr.shape=(3,2)
arr
"""
array([[1, 2],
       [3, 4],
       [5, 6]])
"""



