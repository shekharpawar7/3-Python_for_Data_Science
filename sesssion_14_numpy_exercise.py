import numpy as np
#write a program for check version oof numpy and show
print(np.__version__)
                  #1.24.3
                  
#........................................................................
#write a numpy progra to test whether non of the element are zero
import numpy as np
x=np.array([1,2,3,4,5,0]) #false
print(x)
x.all() #.all() check if any zero

x=np.array([1,2,3,4,5])  #True
print(x)
x.all() #.all() check if any zero

#......................................................................

#write a program for chack arRAY are zero or not
import numpy as np
x=np.array([1,2,3,4,5])
x.any()  #true

x=np.array([0,0,0,0,0])
x.any()  #false

#..........................................................................
#write program for check given array element wise for finitenesss
#not infintiy or not nummber
import numpy as np
a=np.array([1,2,np.inf,np.nan])
a
np.isfinite(a)  #[ True,  True, False, False]

#.........................................................................
#write a numpy program for test element wise for NaN of a given array
import numpy as np
a=np.array([1,2,np.inf,np.nan])
np.isnan(a)  #[False, False, False,  True]

#.........................................................................
#write aprogram for create an elemnet wise compparison
        #(grather,grther_equal,less,less_equal)

x=np.array([2,3])
y=np.array([4,5])

np.greater(x,y)#--------------------------.greather()
#array([False, False])

np.greater_equal(x,y)#-------------------.greather_equal()
#array([False, False])

np.less(x,y)#----------------------------.less()
#array([ True,  True])

np.less_equal(x,y)#----------------------.less_equal()
#array([ True,  True])

#..........................................................................
#write nimpy program to create a 3*3 idenitiy matrix
import numpy as np
array_2D=np.identity(3)#-----------------------------.identiy()
array_2D
"""
      [[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]]
"""

#..........................................................................
#write a numpy program to generete a random number between 1 and 100
import numpy as np
arr=np.random.normal(0,1,1)  #start:end:how_many -------.random()
arr
arr=np.random.rand(1,7)
arr

#..........................................................................
#write a numpy program to create 3*4 array and iterrate over it.
import numpy as np
a=np.arange(12).reshape(3,4)
a
for i in np.nditer(a):#---------------------------------.nditer()
    print(i,end=" ")  #0 1 2 3 4 5 6 7 8 9 10 11 
    
#..............................................................................
#write a numpy program to create a vector of length 5 with value evenly
#distubuted between 10 to 50
import numpy as np
a=np.linspace(10,50,5)   #start,end,how_many----------.linespace()
a #[10., 20., 30., 40., 50.]

#..............................................................................44
#write a program for 3*3 matrix for range in 2 to 10
a=np.arange(2,11).reshape(3,3)#---------------------.arange()
a
"""
      [[ 2,  3,  4],
       [ 5,  6,  7],
       [ 8,  9, 10]])
   """
#............................................................................
#write a program for reverse an array
import numpy as np
a=np.array([1,2,3,4,5,6])
a[::-1]  #[6, 5, 4, 3, 2, 1]

#........................................................................
#write a numpy program to compute the multiplication of array
a=[[1,2],[3,4]]
b=[[6,7],[8,9]]
result=np.dot(a,b)#---------------------------.dot()
result
"""
[[22, 25],
[50, 57]]
"""
#......................................................................
#write a numpy program to compute the corros product of matrix
a=[[1,2],[3,4]]
b=[[6,7],[8,9]]

result=np.cross(a, b) #------------------------------.cross()
result   #array([-5, -5])

#.......................................................................
#write a program for compute a determination of asquare array
import numpy as np
a=np.array([[1,2],[4,5]])
det=np.linalg.det(a)#---------------------------------.det()
det #-2.9999999

#.......................................................................
#write a numpy program for eigenvalue and right eigenvetor of given
#square array
import numpy as np
m= np.mat("3 -2; 1 0")#-----------------------.mat()
print(m)
"""
[[ 3 -2]
 [ 1  0]]
"""
w,v =np.linalg.eig(m)#-----------------------------.eig()

print("eigenvalue",w)
print("eigenvetor",v)

#.............................................................................
#write a progra of inverse of given matrix
import numpy as np
m=np.array([[1,2],[3,4]])
result=np.linalg.inv(m)#--------------------------------.inv()
result
"""
[[-2. ,  1. ],
[ 1.5, -0.5]]
"""

#.......................................................................







