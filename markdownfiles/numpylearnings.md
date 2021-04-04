# Numpy Learnings

Numpy is a module for creating N-dimensional arrays in python. They have vectorised implementation in C which is extremely fast for computation.

To import it into code:
`import numpy as np`

To create an array of ordered elements in the range 0 to 9 i.e, 10-1 (Excluding the element) 

```python
a=np.arange(10)		#For an array from 0 to 9
a=np.zeros(10)		#For an array 10 elements of 0's 
a=np.ones(10)		#For an array 10 elements of 1's
```

To view the shape of the created numpy array

```python
a.shape		#or
np.shape(a)
```

**Note: Important** The shape of the numpy array is not a perfect typle. Ex: (9,) is the shape for a above.

To reshape this array:

```python
a=a.reshape(10,1)
```

This will give the shape as (10,1) which is a proper shape dimensions

##### Axis of an array

By default this is what axis define:

​									_	_	_	_	_	this is axis=1 (towards right)

axis=0 is down			|	
(towards bottom)		 |
									|
putting axis=0 in sum collapses the rows and hence we get the sum of columns

putting axis=1 in sum collapses the columns and hence we get the sum of rows

```python
a=np.arange(9).reshape(3,3)
a.sum(axis=0)		#Output: array([ 9, 12, 15])
a.sum(axis=1)		#Output: array([ 3, 12, 21])
```

Transpose:

```python
a.T
b.T 	#To transpose a vector
```

To dot product 2 vectors:

```python
a=np.arange(9).reshape(9,1)
b=np.arange(9).reshape(9,1)
c=np.dot(a,b.T)			#Here b.T is the transpose of b matrix because both are having size as (9,1) so they can't be multiplied but (1,9) and (9,1) can be multiplied 
print(c.shape)
print(c)
```

Max, Min, Mean, Sum, can be calculated

```python
a.max(axis=0)
a.min(axis=1)			#axis can be anything 0 or 1 or None as per the need
a.mean(axis=1)
a.xum()
```

Strides

```python
a=np.arange(9).reshape(3,3)
a.strides		#Output: In Ubuntu -> (24,8) but in Windows output is (12,4)
a.itemsize		#Output: In Ubuntu -> 8 but in Windows output is 4

x = np.zeros((10, 10, 10), dtype=np.float)
x.strides		#Output: (800,80,8)	Strides are interchanged in case of transpose
x.T.stride		#Output: (8,80,800)
```

Broadcasting is implemented as 0 strides

To append items to an numpy array:

```python
b=np.arange(10)
np.append(b,[10,11])		#but this will not change b it will simply append and return the new numpy array so we have to store it elsewhere
c=np.append(b,[10,11,12])		#Ex
```

Creating a normal numpy array:

```python
a=np.array([12,11,13])	#reshaping is necessary for it to be proper or else a and a.T both give same shapes
print(np.shape(a))		#Output: (3,)
print(np.shape(a.T))	#Output: (3,)
a=a.reshape(3,1)
print(np.shape(a))		#Output: (3,1)
print(np.shape(a.T))	#Output: (1,3)
```

Diagonal 
Only works for 1D and 2D arrays

```python
a=np.arange(9).reshape(3,3)
np.diag(a)		#Output: array([0,4,8])
```

Inserting an element:

```python
a = np.array([1, 2, 3])
newArray = np.insert(a, 1, 90)	#Output: Does not insert to original numpy array because it creates a new numpy array and adds to it. So we have to store it in a variable

```

Deleting an element:

```python
a = np.array([1, 2, 3])
b = np.delete(a, 1, axis = 0)	#array([1, 3])
```

Deleting a row:

```python
a = np.array([[1, 2, 3], [4, 5, 6], [10, 20, 30]])

#output of a 
#array([[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]])

b = np.delete(a, 1, axis = 0)
#Output of b
#array([[1, 2, 3],
#      [7, 8, 9]])
```

Size:

```python
a.size		#Returns number of elements in array/ length of array
```

Dimensions:

```python
a.ndim		#Returns the number of dimensions/number of axes

a=np.array([1,2,3])		#Output: array([1, 2, 3])
a.size					#Output: 3
a.shape					#Output: (3,)
a.ndim					#Output: 1

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
b.size				#Output: 9
b.shape				#Output: (3, 3)
b.ndim				#Output: 2

c=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
c.size				#Output: 15
c.shape				#Output: (3, 5)
c.ndim				#Output: 2
```

Where:

```python
a = np.array([1, 2, 3, 4, 5])
print("5 is found at index: ", np.where(a == 5))
```

Function to a numpy array:

```python
addition = lambda x: x + 2
a = np.array([1, 2, 3, 4, 5, 6])
print("Array after addition function: ", addition(a))
```

To create a numpy array from a list

```python
mylist=[1,2,3,4]
b=np.array(mylist)		#array([1, 2, 3, 4])
```

To create a numpy array from a tuple

```python
mytuple=(1,2,3,4)
b=np.array(mylist)		#array([1, 2, 3, 4])
```

To sort:

```python
np.sort(a)
```

To convert numpy array to a list:

```
mylist= a.tolist()
```

To save text as a csv:

```python
np.savetext("myfile.csv",a)
```

Itemsize: This Prints the size of each item in the array

```python
a=np.zeros(4)
a.itemsize		#Output: 8
a.strides		#Output: (8,)
```

Complex Numpy arrays: 

```python
a=np.array([1,2],[3,4],dtype=complex)
#Output:
#array([[1.+0.j, 2.+0.j],
#      [3.+0.j, 4.+0.j]])
```

Numpy linspace: Means numbers equally spaced from and to a number. Shows floating points

```python
a=np.linspace(10,4,9)		#Output:array([10.  ,  9.25,  8.5 ,  7.75,  7.  ,  6.25,  5.5 ,  4.75,  4.  ])
#The above command means 9 numbers from 10 to 4 equally spaced

a=np.linspace(10,4,4)		#Output: array([10.,  8.,  6.,  4.])
#The aboce command means 4 numbers from 10 to 4 equally spaced
```

Linear Algebra:

```python
np.linalg.inv(a)		#To calculate the inverse of a square matrix
np.trace(a)				#To calculate the sum of diagonal elements of a 2D matrix
np.linalg.eig(j)		#To find eigen values of a matrix
np.linalg.solve(a, y)	#To solve a system of equations
```

