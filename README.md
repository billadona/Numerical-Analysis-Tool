# Numerical-Analysis-ToolINSTALLATION:
	Make sure you have python 2.7 in your system:
	To check python version in Mac, Windows or Linux, run this command: python --version
	
	If you don't have Python 2.7 download it here:
	https://www.python.org/downloads/

	Make sure you have Tkinter library in your system:
	To install Tkinter in Mac, Windows or Linux, run this command in terminal: 
	sudo pip install Tkinter or sudo apt-get install Tkinter
	NOTE: Make sure that you have the python2.7 path in you PATH environment variable
	NOTE: Also to be able to use pip, you need Python2.7\Scripts in your PATH envirionment variable as well.

	Make sure you have sympy library in your system:
	To install sympy in Mac, Windows or Linux, run this command in terminal: 
	sudo pip install Tkinter or sudo apt-get install Tkinter
	NOTE: Make sure that you have the python2.7 path in you PATH environment variable
	NOTE: Also to be able to use pip, you need Python2.7\Scripts in your PATH envirionment variable as well.	
	
HOW TO USE:
	Navigate to the folder in Terminal and run this code: python DifferenceMethod.py
	NOTE: The program will close if invalid inputs are given and if required inputs are not given.
	
	NOTE: Syntax for python is different than MATLAB or regular expressions (x^2+2)
	      In sympy, x^2 is represented as x**2.
	      In sympy, x^2 + 1 -> x**2+1
	      In sympy, 1/x -> 1/x
	      In sympy, 2x -> 2*x
   	      In sympy, 2x^2 -> 2*x**2
	      THERE IS NO SPACES IN BETWEEN OPERATORS 

	TO PERFORM DIFFERENCE METHOD/EXTRAPOLATION:
	TO PERFORM TWO-POINT FORWARD:
	Input is needed for Function field, initial h, and x field.
	This will allow you to compute for a single approximation.
	
	To create a table of approximation and approximation errors,
	input is needed for Function field, initial h, ending h and x field.

	Example inputs:
	Function : 1/x
	Initial h : 0.1
	Ending h : 
	x : 2

	Function : 1/x
	Initial h : 0.1
	Ending h : 5
	x : 2

	TO PERFORM CENTERED DIFFERENCE:
	Input is needed for Function field, initial h, and x field.
	This will allow you to compute for a single approximation.
	
	To create a table of approximation and approximation errors,
	input is needed for Function field, initial h, ending h and x field.

	Example inputs:
	Function : 1/x
	Initial h : 0.1
	Ending h : 
	x : 2

	Function : 1 / x
	Initial h : 0.1
	Ending h : 5
	x : 2


	TO USE AUTOMATIC DIFFERENTIATION:
	Input is needed for both Function and x field.
	Example inputs:
	Function : 2*x+2*x
	x : 2

	Function : 2*x**3
	x : 4
	
	Function : 8*x
	x : 6
