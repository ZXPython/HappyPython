Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L=[]
>>> for x in range(20)
SyntaxError: invalid syntax
>>> for x in range(20):
	x=x+1
	s=x*x*x
	L.append(s)

	
>>> print("L=",L)
L= [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]
>>> for x in L:
	print(x)

	
1
8
27
64
125
216
343
512
729
1000
1331
1728
2197
2744
3375
4096
4913
5832
6859
8000
>>> 
