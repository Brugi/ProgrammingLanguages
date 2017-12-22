#Jamie's coursework template
print('''
#My Name Mark Schmieg, My ms147, My H00238262   
#F28PL Coursework PY1                         
''')
print('Coursework of Mark Schmieg, my ID: ms147, my Regno: H00238262' )
#You may assume variables, procedures, and functions defined in earlier questions 
#in your answers to later questions, though you should add comments in code explaining 
#this if any clarification might help read your code.


################################################################################
#Question 1   <--- Yes, so we know what question you think you're answering 
print()
print()
print('Question 1')

"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j,
depending on the complex numbers notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
tocomplex and fromcomplex that map (x1,y1) to x1+(y1)j and vice versa. You may use the
python methods real and imag without comment.
"""
#  <--- always have the question under your nose 

#####################################
#Question 1a

'''
Adds the first part of x to the first part of y and does the same with the second part.
'''
print('Question 1a')
print('Executing the function cadd, explanation of the code is in comments.')
def cadd(x,y):
	return(x[0]+y[0], x[1]+y[1])

print('Executing cadd((4,2),(3,7)), should return: (7,9).')
print(cadd((4,2),(3,7)))

print('Executing cadd((3,0),(3,4)), should return: (6,4).')
print(cadd((3,0),(3,4)))

print('Executing cadd((0,1),(2,0)), should return: (2,1).')
print(cadd((0,1),(2,0)))

print()
print()
print()
print('Executing the function cmult, explanation of the code is in comments.')
def cmult(x,y):
	return(x[0]*y[0]-x[1]*y[1], x[0]*y[1]+y[0]*x[1])

print('Executing cmult((3,2),(1,7)), should return: (-11, 23).')
print(cmult((3,2),(1,7)))

print('Executing cmult((4,5),(3,6)), should return: (-18,39).')
print(cmult((4,5),(3,6)))

print('Executing cmult((4,9),(7,1)), should return: (19,67).')
print(cmult((4,9),(7,1)))
#####################################
#Question 1b
print()
print()
print('Question 1b')
print('Executing the function tocomplex, explanation of the code is in comments.')
def tocomplex(x,y):
	return(x + y*1j)

print('Executing tocomplex(4,8), should return: (4+8j).')
print(tocomplex(4,8))

print('Executing tocomplex(7,1), should return: (7+1j).')
print(tocomplex(7,1))

print('Executing tocomlpex(4,3), should return: (4+3j).')
print(tocomplex(4,3))

print()
print()
print()
print('Executing the function fromcomplex, explanation of the code is in comments.')
def fromcomplex(x):
	return(int(x.real),int(x.imag))
	
print('Executing fromcomplex(3+2j), should return: (3,2).')
print(fromcomplex(3+2j))

print('Executing fromcomplex(4+9j), should return: (4,9).')
print(fromcomplex(4+9j))

print('Executing fromcomplex(5+3j), should return: (5,3).')
print(fromcomplex(5+3j))
'''
The function cmult takes two complex numbers. Since i^2=-1, the product of the two imaginary parts will turn into 
integers(for example: 5i * 2i = -10). The rest of the operation goes like a normal multiplication. And the integer 
part is added together and the imaginary part is added together.
'''	
print('''
#END ANSWER TO Question 1
################################################################################
''')


################################################################################
#Question 2
print()
print()
print('Question 2')

"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
seqaddi([1,2,3],[~1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (as for ML).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
"""

#####################################
#Question 2a
print()
print()
print('Question 2a')
print('Executing the function seqaddi, explanation of the code is in comments.')
def seqaddi(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		v=[]
		for i in range(len(x)):
			v.append(x[i]+y[i])
		return v

print('Executing seqaddi([1,2,3],[4,5,8]), should return: [5,7,11].')
print(seqaddi([1,2,3],[4,5,8]))

print('Executing seqaddi([4,63,2], []), should return: [4, 63, 2].')
print(seqaddi([4,63,2], []))

print('Executing seqaddi([],[]), should return: [].')
print(seqaddi([],[]))


print()
print()
print()
print('Executing the function seqmulti, explanation of the code is in comments.')
def seqmulti(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		v=[]
		for i in range(len(x)):
			v.append(x[i]*y[i])
		return v
		
print('Executing seqmulti([2,1,5],[7,4,2]), should return: [14, 4, 10].')
print(seqmulti([2,1,5],[7,4,2]))

print('Executing seqmulti([], [2,4,6]), should return: [2,4,6].')
print(seqmulti([], [2,4,6]))

print('Executing seqmulti([],[]), should return: [].')
print(seqmulti([],[]))
#####################################
#Question 2b
print()
print()
print('Question 2b')
print('Executing the function seqaddr, explanation of the code is in comments.')
def seqaddr(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		return [x[0]+y[0]] + seqaddr(x[1:],y[1:])
		
print('Executing seqaddr([1,2,3],[4,5,8]), should return: [5,7,11].')
print(seqaddr([1,2,3],[4,5,8]))

print('Executing seqaddr([4,63,2], []), should return: [4, 63, 2].')
print(seqaddr([4,63,2], []))

print('Executing seqaddr([],[]), should return: [].')
print(seqaddr([],[]))


print()
print()
print()
print('Executing the function seqmultr, explanation of the code is in comments.')
def seqmultr(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		return [x[0]*y[0]] + seqaddr(x[1:],y[1:])

print('Executing seqmultr([2,1,5],[7,4,2]), should return: [14, 4, 10].')
print(seqmultr([2,1,5],[7,4,2]))

print('Executing seqmultr([], [2,4,6]), should return: [2,4,6].')
print(seqmultr([], [2,4,6]))

print('Executing seqmultr([],[]), should return: [].')
print(seqmultr([],[]))



#####################################
#Question 2c
print()
print()
print('Question 2c')
print('Executing the function seqaddc, explanation of the code is in comments.')
def seqaddc(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		return [x[i]+y[i] for i in range(len(x))]
		
print('Executing seqaddc([1,2,3],[4,5,8]), should return: [5,7,11].')
print(seqaddc([1,2,3],[4,5,8]))

print('Executing seqaddc([4,63,2], []), should return: [4, 63, 2].')
print(seqaddc([4,63,2], []))

print('Executing seqaddc([],[]), should return: [].')
print(seqaddc([],[]))


print()
print()
print()
print('Executing the function seqmultc, explanation of the code is in comments.')
def seqmultc(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		return [x[i]*y[i] for i in range(len(x))]
print('Executing seqmultc([2,1,5],[7,4,2]), should return: [14, 4, 10].')
print(seqmultc([2,1,5],[7,4,2]))

print('Executing seqmultc([], [2,4,6]), should return: [2,4,6].')
print(seqmultc([], [2,4,6]))

print('Executing seqmultc([],[]), should return: [].')
print(seqmultc([],[]))		


print('''
END ANSWER TO Question 2
################################################################################
''')



################################################################################
#Question 3

"""
Write functions
ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
matrixshape
This should input an intmatrix and return a pair that is the number of columns, and the
number of elements in any row.
matrixadd
Matrix addition, which is simply pointwise addition.
matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may 
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.
"""
print()
print()
print('Question 3')

'''
This function checks if all the lists within the list(matrix= list of lists) are of equal length. It uses a checker, n, which starts with the value True.
If during the iteration of the matrix one of the lists is not equal to the length of the first list then n gets set to false.
At the end the value of n is returned.
'''
print('Executing the function ismatrix, explanation of the code is in comments.')
def ismatrix(x):
	n=True
	for i in x:
		if len(i)!= len(x[0]):
			n=False
	return n
	

print('Executing ismatrix([[5,4,2],[35,32,8],[3,56,7]]), should return:  true.')
print( ismatrix([[5,4,2],[35,32,8],[3,56,7]]))	

print('Executing ismatrix([]), should return:  true.')
print(ismatrix([]))

print('Executing ismatrix([[1],[3],[8]]), should return: true.')
print(ismatrix([[1],[3], [8]]))	

print()
print()
print()
'''
Returns a pair which is (number of rows,number of columns )
''' 
print('Executing the function matrixshape, explanation of the code is in comments. It prints (number of rows, number of columns)')
def matrixshape(x):
	if len(x)==0:
		return (0,0)
	else:
		return (len(x), len(x[0]))

print('Executing matrixshape([[4,5,4,2],[6,35,32,8],[3,78,56,7]]), should return: (3,4).')
print(matrixshape([[4,5,4,2],[6,35,32,8],[3,78,56,7]]))	

print('Executing matrixshape([]), should return:  (0,0).')
print(matrixshape([]))	

print('Executing matrixshape([[1,2,3],[9,8,7]]), should return: (2,3).')
print(matrixshape([[1,2,3],[9,8,7]]))	

print()
print()
print()
'''
Matrixadd uses list comrehension and seqaddc to add the elements of x and y by pointwise addition together.

'''
print('Executing the function matrixadd, explanation of the code is in comments.')
def seqaddc(x,y):
	return [x[i]+y[i] for i in range(len(x))]

def matrixadd(x,y):
	return [seqaddc(x[i],y[i]) for i in range(len(x))]	
	
	
print('Executing matrixadd([[3,5,5],[5,3,1]],[[7,2,1],[1,2,3]]), should return: [[10, 7, 6], [6, 5, 4]].')
print(matrixadd([[3,5,5],[5,3,1]],[[7,2,1],[1,2,3]]))

print('Executing matrixadd([],[]), should return: [].')
print(matrixadd([],[]))


print('Executing matrixadd([[1,2,4]],[[3,2,6]]), should return: [[4,4,10]].')
print(matrixadd([[1,2,4]],[[3,2,6]]))

print()
print()
print()
'''
Matrixmult uses 3 helper functions to make matrix multiplication, seqmult: multiplies 2 lists together, transpose: transposes a matrix, sumList: returns sum of all elements in a list.
Matrixmult takes 2 matrices then transposes the 2nd one, then does the dotproduct of the matrices. 
'''
print('Executing the function matrixmult, explanation of the code is in comments.')
def seqmultc(x,y):
	if len(x) == 0 and len(y)== 0:
		return []
	elif len(x) == 0:
		return y
	elif len(y) == 0:
		return x
	else:
		return [x[i]*y[i] for i in range(len(x))]
		
		
def transpose(y):
	u=[]
	for i in range(len(y)):
		l=[]
		for t in range(len(y[i])):
			l.append(y[t][i]);
		u.append(l)		
	return u
		
def sumList(x):
	s=0
	for i in x:
		s =s+ i
	return s
	
	
def matrixmult(x,y):
	if x == [[]] and len(y)== [[]]:
		return [[]]
	if x == [[]]:
		return [[]]
	if y == [[]]:
		return [[]]
	v=[]
	y=transpose(y)
	for i in range(len(x)): 
		for t in range(len(y)):
			multpoint=0
			multpoint = sumList(seqmultc(x[i],y[t]))
			v.append(multpoint)
	return 	v

print('Executing matrixmult([[1,2]],[[1,2],[3,4]]), should return: [7,10].')
print(matrixmult([[1,2]],[[1,2],[3,4]]))

print('Executing matrixmult([[]],[[]]), should return: [[]].')
print(matrixmult([[]],[[]]))

print('Executing matrixmult([[]],[[1,2,3]]), should return: [[]].')		
print(matrixmult([[]],[[1,2,3]]))

print('''	
#END ANSWER TO Question 3
################################################################################
''')

###############################################################################
#Question 4
print()
print()
print('Question 4')

"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
-Mutable vs immutable types. Give at least two examples of each, with explanation.
-Integer vs float types.
-Assignment = vs equality == vs identity is.
-The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).
-Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""



print(
'''
- Immtable types cannot be modified once created, they cannot use methods which alter their values. 
Whereas mutable types can have their values changed by different kinds of methods.
For example:
A tuple is an immutable type.
#a tuple a is created and then the method append is used on it and python will signal an error for that
>>>t = (3,6,4,7)
>>>t.append(9)  #The following error will be raised: AttributeError: 'tuple' object has no attribute 'append'

A list is a mutable type, and can be altered while being in a tuple.
#here I create a list, x, with some integers, then I create a tuple, y, which contains the list, x, and the word "Python". 
#Since a list is mutable I can change it's values, so in the 3rd line I append the integer 2 to the list x, which works because 
#the tuple is not being altered but the list within the tuple is.
>>>x= [3,4,8]
>>>y = ("Python", x)
>>>y[1].append(2)
>>>y 
('Python', [3, 4, 8, 2])

Then there are sets and frozensets. Sets are mutable and frozensets arent.
#I create a set and remove an element without any issues
>>> set = {5,8,3,1,6}
>>> set.remove(3)
>>> set
{8, 1, 5, 6}

>>>frozSet = frozenset([6,4,8,7,2])
>>> frozSet.remove(8) #The following error is thrown: AttributeError: 'frozenset' object has no attribute 'remove'

- Integer types are precise and are exact values whereas float types are approximations.
For example:
The integer 1 is an exact values
But if we do:
>>>10/3
3.3333333333333335 #This value is an approximation of the real result because the result should be 3.33333... and it goes for ever because 10 cannot be divided by 3 equally

-The assignment "=" is used to assign a value to something, for example( a=9) then a will be equals to 9
The equality "==" is used to compare two values and will return a boolean, for example 9==9 will return true.
The identity "is" is used to compare the addresses where values are stored, for example:
x=[2,3,5,7]  
y=x # this makes y point to the location of x
y==x # will return true because the values are the same
y is x # returns true because the address is the same
x.remove(7) #
y #this will print [2,3,5] because y was pointing to the same location as x and when x was altered y is altered as well.

- When calling a list on an element of range type, a list will be created containing all the numbers to the number entered in range excluded, and the output of the lists also depends on what is passed into range.
So if something like this is written: list(range(x)) then this will print a list from 0 until x excluded.
If something like this is written: list(range(x,y,z)) then this will create a list from x to z excluded and incrementing/decrementing by z.
For example:
list(range(20)) #this will print a list from 0 to 19.
list(range(4,23,2) # this will print a list from 4 to 22 incrementing by 2 
list(range(40,10,-5))  # this will create a list from 40 to 15 decrementing by 10

-Slices is used to get a list of the part of a range that we want. For example: list(range(x [y:z]), this will return a list between y and z excluded inside of the range x.
For example: 
list(range(70) [30:45]) # this will return a list from 30 to 44
list(range(23) [10:19]) #this will return a list from 10 to 18
#Difference in execution between  list(range(10**10)[10:10]) and list(range(10**10))[10:10]
In list(range(10**10) [10:10]), the range gets sliced before it is computed, which means that only a list of the slice [10:10] is created. 
Wheras with list(range(10**10))[10:10], the ranges gets computed first before getting sliced aferwards, for this example this range does not work and gives the error: "memory error", because it runs out of memory.
''')
print('''
#END ANSWER TO Question 4
################################################################################
''')


###############################################################################
#Question 5

"""
Write a general encoding function encdat that will intput an integer, float, complex number, or
string, and return it as a string.

So
-encdat(-5) should return '-5'
-encdat(5.0) should return '5.0'
-encdat(5+5j) should return '5+5j'
-encdat('5') should return '5'

In formulating your answer, you may find it useful to consider the following code fragment
   type(5) == type('5') 
"""
print()
print
'''
This function turns anything which gets passed into it into string by casting it to string. If the value passed in is a complex number, it first gets casted to string and
then the brackets get removed.
'''

print('Question 5')
print('Executing the function encdat, explanation of the code is in comments.')
def encdat(datum):
	if "(" or ")" in datum:
		datum=str(datum)
		datum = datum.replace(")", "")
		datum = datum.replace("(","")
		return str(datum)
	else:
		return str(datum)

print('Executing encdat(45+7j), should return: 45+7j.')
print(encdat(45+7j))		
print('Prints type of encdat(45+7j), should return: <class "str">')
print(type(encdat(45+7j)))
print('Executing encdat(67), should return: 67.')
print(encdat(67))
print('Prints type of encdat(67), should return: <class "str">')
print(type(encdat(67)))
print('Executing encdat(3.2), should return: 3.2.')
print(encdat(3.2))
print('Prints type of encdat(3.2), should return: <class "str">')
print(type(encdat(3.2)))

print('''
#END ANSWER TO Question 5
################################################################################
''')

###############################################################################
#Question 6


"""
An encoding f of numbers in lists is as follows:
-f(0) = [] (0 maps to the empty list)
-f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""
print()
print()
print('Question 6')
'''
This function takes a number, if it is 0 it will return an empty list. If the number is greater than 0, the function will create a list of 2 elements where the first one is the encoding of the number 
before the one passed in, and the second element is the list of the encoding of the number before the one passed in.

'''
print('Executing the function fenc, explanation of the code is in comments')
def fenc(x):
	if (x==0):
		return []
	else:
		return [fenc(x-1),[fenc(x-1)]]
print('Executing fenc(0), should return: []')
print(fenc(0))

print('Executing fenc(3), should return: [[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]].')
print(fenc(3))

print('Executing fenc(1), should return: [[], [[]]].')
print(fenc(1))
[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]

print()
print()
print()
'''
Uses a tail recursion to go through the list given and returns the number of times .
'''
print('Executing the function fdec, explanation of the code is in comments')
def fdec(x):
	
	if(x == []):
		return 0
	else:
		return 1+ fdec(x[0])

print('Executing fdec([[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]), should return: 3.')
print(fdec([[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]))

print('Executing fdec([]), should return: 0.')
print(fdec([]))

print('Executing fdec([[], [[]]]), should return: 1.')
print(fdec([[], [[]]]))

print('''
#END ANSWER TO Question 6
################################################################################
''')

###############################################################################
#Question 7

"""
Implement an iterator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code...
in an endless cycle. If you cannot manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
"""
print()
print()
print('Question 7')

'''
The cycleoflife funtion contains an array, arr, while the funciton doesn't reach the end of the array , it loops through it using yield, which returns a generator of the list. If the end of the list 
is reached, the variable, i, which is used to cycle through the array is reset to 0, so that the program can never end and go for ever. A genereator is an iterator, when called it returns a value of 
the object it is iterating over, it does not store anything in memory but does the operations in the moment. When next(x) is called it uses the iterator returned through yield,which returns the next 
element of the list.
'''
print('Executing the function cycleoflife, explanation of the code is in comments')
def cycleoflife():
	arr=['eat','sleep','code']
	i=0
	while True:
		yield arr[i]
		i = (i+1) % len(arr)
		
#This could be made to run forever, but in order to have a better overview only a few calls to next(x) are made.		
print('Assigning cycleoflife() to x')		
x = cycleoflife()
print('Printing next(x), should return: eat')
print(next(x))
print('Printing next(x), should return: sleep')
print(next(x))
print('Printing next(x), should return: code')
print(next(x))
print('Printing next(x), should return: eat ')
print(next(x))
print('Printing next(x), should return: sleep')
print(next(x))
print('Printing next(x), should return: code')
print(next(x))
print('Printing next(x), should return: eat')
print(next(x))

print('''
#END ANSWER TO Question 7
################################################################################
''')


#################################################################################
#Question 8
"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function flatten that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

In formulating your answer, you may find it useful to consider the following code fragment
   type(5) == type([]) 
"""
print()
print()
print('Question 8')

	
'''	
This function takes a input called datum. If datum is only an integer it will be appended to the list arr and arr will be returned. Otherwise, it cycles through the list, if the element is an integer, it will be appended
to arr, else the function will go deeper into the element and retrieve all the integers, which get appended to the list arr. At the end arr is returned.
'''
print('Executing the function gendat, explanation of the code is in comments')
def gendat(datum):
	arr = []
	if isinstance(datum,int) == True:
		arr.append(datum)
		
	else:
		for elements in datum:
			if isinstance(elements, int) == True:
				arr.append(elements)
			
			elif isinstance(elements, list) == True:
				for withinElement in elements:
					if isinstance(withinElement, int) == True:
						arr.append(withinElement)
					else:
						arr += gendat(withinElement)
	return arr

print('Executing gendat([436,[],[[[[6464],4664]],2],[45]]), should return: [436, 6464, 4664, 2, 45].')
print(gendat([436,[],[[[[6464],4664]],2],[45]]))

print('Executing gendat(67), should return: [67].')
print(gendat(67))

print('Executing gendat([]), should return: [].')
print(gendat([]))

print('''
#END ANSWER TO Question 8
################################################################################
''')




