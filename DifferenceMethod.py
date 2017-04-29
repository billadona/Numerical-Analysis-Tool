from sympy import *
from Tkinter import *
from mpmath import *
import ttk
import sys


MAX_SIZE = 50
lst_x = [0] * MAX_SIZE
lst_y = [0] * MAX_SIZE
lengt = 0



def closePop(pop):
	pop.destroy()

def checkInt(strg):
	try:
		int(strg)
		return True
	except ValueError:
		return False

def differenceM():
	Sfunc = StringVar()				#Holds the given function by the user
	Sh_start = StringVar()			#String var for starting h
	Sh_end = StringVar()			#String var for ending h
	Sx = StringVar()				#String var for x

	#Create new pop up window
	top = Toplevel()
	top.title("Difference Method")
	diffMFrame = ttk.Frame(top, padding="15 20 15 20")
	diffMFrame.grid(column=0, row=0)
	diffMFrame.columnconfigure(0, weight=1)
	diffMFrame.rowconfigure(0, weight=1)

	#create label
	Label(diffMFrame, text="Function").grid(row=0, column=0, pady=(0,10))
	Label(diffMFrame, text="Initial h (step)").grid(row=1, column=0, pady=(0, 10))
	Label(diffMFrame, text="Ending h (step)").grid(row=2, column=0, pady=(0, 10))
	Label(diffMFrame, text="x").grid(row=3, column=0, pady=(0,10))

	#Input field for function
	Entry(diffMFrame, textvariable=Sfunc).grid(row=0, column=1, pady=(0, 10))
	Entry(diffMFrame, textvariable=Sh_start).grid(row=1, column=1, pady=(0, 10))
	Entry(diffMFrame, textvariable=Sh_end).grid(row=2, column=1, pady=(0, 10))
	Entry(diffMFrame, textvariable=Sx).grid(row=3, column=1, pady=(0, 10))

	buttn_two_frwrd = ttk.Button(diffMFrame, text="Two-Point Forward", command = lambda: twoPointDiff(Sfunc.get(), Sh_start, Sh_end, Sx)).grid(row=4, column=0, pady=(0, 10))
	ttk.Button(diffMFrame, text="Centered Difference Forward", command = lambda: centralDiff(Sfunc.get(), Sh_start, Sh_end, Sx)).grid(row=5, column=0, pady=(0, 10))

def twoPointDiff(sf, numh, numh_end, numx):
	#no h input from user
	if len(sf) == 0:
		print 'input neededed in function entry field'
		sys.exit()

	#no initial h input from user
	if len(numh.get()) == 0:
		print 'input neededed for initial h'
		sys.exit()

	#Check if the input value is an Int
	if checkInt(numh.get()):
		numH = int(numh.get())
	else:
		numH = float(numh.get())

	#No x input from the user
	if len(numx.get()) == 0:
		print 'input neededed for x'

	#Check if the input value is an int
	if checkInt(numx.get()):
		numX = int(numx.get())
	else:
		numX = float(numx.get())

	x, y = symbols("x y")

	#sympify converts the string to a sympy expr
	try:
		#create a sympy expression if input is valid
		expr = sympify(sf)	
	except ValueError:
		#exit program if input function is not valid
		print 'Inputted function is not valid'
		sys.exit()

	#no h input from user
	if len(numh_end.get()) == 0:
		num = numX + numH 										#f(x + h)
		n = expr.evalf(5, subs={x: num})
		n = n - ( expr.evalf(5, subs={x: numX}) )				#f(x + h) - f(x)		
		fx = n / numH 											#f(x + h) - f(x) / 2
		aproximation_str = "The approximation: " + str(fx)
		#Value of f'(x)
		#store the derivative of f(x)
		dervFx = expr.diff(x)
		#compute f'(x)
		dervFx_num = expr.evalf(5, subs={x: numX})
		#store the derivative of f'(x)
		snd_dervFx = dervFx.diff(x)
		apprx_error = fx - dervFx.evalf(5, subs={x: numX})
		aprx = "aprroximation error (f'(x) - f''(x)) : " + str(apprx_error)
		c = num / 2
		predicted_err = (numH * (snd_dervFx.evalf(5, subs={x: c}))) / 2
		pred_err = "predicted error (hf''(c)/2) = " + str(predicted_err)

		pop = Toplevel()
		pop.title("Difference Method")
		diffMFrame = ttk.Frame(pop, padding="15 20 15 20")
		diffMFrame.grid(column=0, row=0)
		diffMFrame.columnconfigure(0, weight=1)
		diffMFrame.rowconfigure(0, weight=1)

		Label(diffMFrame, text=aproximation_str).grid(row=0, column=0, pady=(0,10))
		Label(diffMFrame, text=aprx).grid(row=1, column=0, pady=(0, 10))
		Label(diffMFrame, text=pred_err).grid(row=2, column=0, pady=(0,10))

	else:
		#check if int
		if checkInt(numh_end.get()):
			numH_end = int(numh_end.get())
		else:
			numH_end = float(numH_end)

		#check if initial h and ending h is the same
		if numH_end == numH:
			print 'ERROR: starting h and ending h is the same'
			sys.exit()

		elif numH < numH_end:
			pop = Toplevel()
			pop.title("Difference Method")
			diffMFrame = ttk.Frame(pop, padding="15 20 15 20")
			diffMFrame.grid(column=0, row=0)
			diffMFrame.columnconfigure(0, weight=1)
			diffMFrame.rowconfigure(0, weight=1)

			lb1 = Listbox(diffMFrame)		#holds the approximation value
			lb2 = Listbox(diffMFrame)		#holds the approximation error
			lb3 = Listbox(diffMFrame)		#holds the predicted approximation error

			inc = 0							#used as an incrementer for Listbox
			h_itr = numH 					#initializes h_itr to the starting h so while loop will start with h init

			while h_itr != numH_end:
				if h_itr > numH_end:
					break
				
				
				number = numX + h_itr												#x + h
				new_num = expr.evalf(5, subs={x: number})							#f(x + h)									
				new_num = new_num - (expr.evalf(5, subs={x: numX}))					#f(x + h) - f(x)
				func_x = new_num / h_itr											#f(x + h) - f(x) / h

				derv_fx = expr.diff(x)												#f'(x)
				snd_derv_fx = derv_fx.diff(x)										#f''(x)
				approx_err = func_x -( derv_fx.evalf(5, subs={x: numX}) )			#f'(x) (using the formula) - f'(x) (using derivative)

				c2 = number / 2
				predic_err = (h_itr * (snd_derv_fx.evalf(5, subs={x: c2}))) / 2

				lb1.insert(inc, func_x)
				lb2.insert(inc, approx_err)
				lb3.insert(inc, predic_err)

				h_itr += numH

			num2 = numX + numH_end
			new_num2 = expr.evalf(5, subs={x: num2})
			new_num2 = new_num2 - (expr.evalf(5, subs={x: numX}))
			func_x2 = new_num2 / numH_end

			derv_fx2 = expr.diff(x)
			snd_derv_fx2 = derv_fx2.diff(x)
			approx_err2 = func_x2 -( derv_fx2.evalf(5, subs={x: numX}) )
			c_2 = number / 2
			predic_err2 = (numH_end * (snd_derv_fx2.evalf(5, subs={x: c_2}))) / 2

			lb1.insert(inc, func_x2)
			lb2.insert(inc, approx_err2)
			lb3.insert(inc, predic_err2)

			Label(diffMFrame, text="Approximation Values:").grid(row=0, column=0, pady=(0,10))
			Label(diffMFrame, text="Approximation Error:").grid(row=0, column=1, pady=(0,10))
			Label(diffMFrame, text="Predicted Approximation Error:").grid(row=0, column=2, pady=(0,10))

			lb1.grid(row=1, column=0)
			lb2.grid(row=1, column=1)
			lb3.grid(row=1,column=2)

		else:
			#numh > numh_end
			print 'ERROR: Initial h is bigger than ending h'
			sys.exit()



def centralDiff(sf, numh, numh_end, numx):
	#no h input from user
	if len(sf) == 0:
		print 'input neededed in function entry field'
		sys.exit()

	#no h input from user
	if len(numh.get()) == 0:
		print 'input neededed for h'
		sys.exit()

	#Check if the input value is an Int
	if checkInt(numh.get()):
		numH = int(numh.get())
	else:
		numH = float(numh.get())


	#No x input from the user
	if len(numx.get()) == 0:
		print 'input neededed for x'

	#Check if the input value is an int
	if checkInt(numx.get()):
		numX = int(numx.get())
	else:
		numX = float(numx.get())

	x, y = symbols("x y")

	#sympify converts the string to a sympy expr
	try:
		#create a sympy expression if input is valid
		expr = sympify(sf)	
	except ValueError:
		#exit program if input function is not valid
		print 'Inputted function is not valid'
		sys.exit()



	#no h input from user
	if len(numh_end.get()) == 0:

		#f(x + h)
		num = numX + numH
		n = expr.evalf(5, subs={x: num})
		#f(x + h) - f(x - h)
		n = n - ( expr.evalf(5, subs={x: (numX - numH)}) )
		#f(x + h) - f(x - h) / 2h		
		fx = n / (2*numH)
		aproximation_str = "The approximation: " + str(fx)
		#Value of f'(x)
		#store the derivative of f(x)
		dervFx = expr.diff(x)
		#compute f'(x)
		dervFx_num = expr.evalf(5, subs={x: numX})
		#store the derivative of f'(x)
		snd_dervFx = dervFx.diff(x)
		apprx_error = fx - dervFx.evalf(5, subs={x: numX})
		aprx = "aprroximation error (f'(x) - f''(x)) : " + str(apprx_error)
		c = num / 2
		predicted_err = (numH * (snd_dervFx.evalf(5, subs={x: c}))) / 2
		pred_err = "predicted error (hf''(c)/2) = " + str(predicted_err)


		pop = Toplevel()
		pop.title("Difference Method")
		diffMFrame = ttk.Frame(pop, padding="15 20 15 20")
		diffMFrame.grid(column=0, row=0)
		diffMFrame.columnconfigure(0, weight=1)
		diffMFrame.rowconfigure(0, weight=1)

		Label(diffMFrame, text=aproximation_str).grid(row=0, column=0, pady=(0,10))
		Label(diffMFrame, text=aprx).grid(row=1, column=0, pady=(0, 10))
		Label(diffMFrame, text=pred_err).grid(row=2, column=0, pady=(0,10))

	else:
		#check if int
		if checkInt(numh_end.get()):
			numH_end = int(numh_end.get())
		else:
			numH_end = float(numH_end)

		#check if initial h and ending h is the same
		if numH_end == numH:
			print 'ERROR: starting h and ending h is the same'
			sys.exit()

		elif numH < numH_end:
			pop = Toplevel()
			pop.title("Three-point Central Difference Method")
			diffMFrame = ttk.Frame(pop, padding="15 20 15 20")
			diffMFrame.grid(column=0, row=0)
			diffMFrame.columnconfigure(0, weight=1)
			diffMFrame.rowconfigure(0, weight=1)

			lb1 = Listbox(diffMFrame)		#holds the approximation value
			lb2 = Listbox(diffMFrame)		#holds the approximation error
			lb3 = Listbox(diffMFrame)		#holds the predicted approximation error

			inc = 0							#used as an incrementer for Listbox
			h_itr = numH 					#initializes h_itr to the starting h so while loop will start with h init

			while h_itr != numH_end:
				if h_itr > numH_end:
					break
				
				
				number = numX + h_itr												#x + h
				new_num = expr.evalf(5, subs={x: number})							#f(x + h)									
				new_num = new_num - (expr.evalf(5, subs={x: (numX - h_itr)}))		#f(x + h) - f(x - h)
				func_x = new_num / (2*h_itr)										#f(x + h) - f(x - h) / 2h

				derv_fx = expr.diff(x)												#f'(x)
				snd_derv_fx = derv_fx.diff(x)										#f''(x)
				approx_err = func_x -( derv_fx.evalf(5, subs={x: numX}) )			#f'(x) (using the formula) - f'(x) (using derivative)

				c2 = number / 2
				predic_err = (h_itr * (snd_derv_fx.evalf(5, subs={x: c2}))) / 2

				lb1.insert(inc, func_x)
				lb2.insert(inc, approx_err)
				lb3.insert(inc, predic_err)

				h_itr += numH

			num2 = numX + numH_end
			new_num2 = expr.evalf(5, subs={x: num2})
			new_num2 = new_num2 - (expr.evalf(5, subs={x: numX}))
			func_x2 = new_num2 / numH_end

			derv_fx2 = expr.diff(x)
			snd_derv_fx2 = derv_fx2.diff(x)
			approx_err2 = func_x2 -( derv_fx2.evalf(5, subs={x: numX}) )
			c_2 = number / 2
			predic_err2 = (numH_end * (snd_derv_fx2.evalf(5, subs={x: c_2}))) / 2

			lb1.insert(inc, func_x2)
			lb2.insert(inc, approx_err2)
			lb3.insert(inc, predic_err2)

			Label(diffMFrame, text="Approximation Values:").grid(row=0, column=0, pady=(0,10))
			Label(diffMFrame, text="Approximation Error:").grid(row=0, column=1, pady=(0,10))
			Label(diffMFrame, text="Predicted Approximation Error:").grid(row=0, column=2, pady=(0,10))

			lb1.grid(row=1, column=0)
			lb2.grid(row=1, column=1)
			lb3.grid(row=1,column=2)

		else:
			#numh > numh_end
			print 'ERROR: Initial h is bigger than ending h'
			sys.exit()

def ADmultip(num ,x1, y1, x2, y2, exp):
	if num == 1:
		#Variable with just exponent, no constant: x**2
		num_x = lst_x[0]
		num_y = lst_y[0]
		for x in range(0, exp-1):
			#(u, u')*(v,v')=(u*v, u'v + uv')
			num_y = (num_y * lst_x[0]) + (num_x * lst_y[0])
			num_x = num_x * lst_x[0]
			print 'num y = ', num_y
			print 'num x = ', num_x

		lst_y[y1] = num_y
		lst_x[x1] = num_x

	elif num == 2:
		num_x = lst_x[0]
		num_y = lst_y[0]
		for x in range(0, exp):
			#(u, u')*(v,v')=(u*v, u'v + uv')
			num_y = (num_y * lst_x[y1]) + (num_x * lst_y[y1])
			num_x = num_x * lst_x[x1]
			print 'num y = ', num_y
			print 'num x = ', num_x
			
		lst_y[y1] = num_y
		lst_x[x1] = num_x

	else:
		num_x = lst_x[0]
		num_y = lst_y[0]
		for x in range(0, exp-1):
			#(u, u')*(v,v')=(u*v, u'v + uv')
			num_y = (num_y * lst_x[0]) + (num_x * lst_y[0])
			num_x = num_x * lst_x[0]
			print 'num y = ', num_y
			print 'num x = ', num_x
			
		lst_y[y1] = num_y
		lst_x[x1] = num_x


		lst_y[y1-1] = (lst_y[y1-1] * lst_x[x1]) + (lst_x[x1-1] * lst_y[y1])
		lst_x[x1-1] = lst_x[x1-1] * lst_x[x1]

		lst_y[y1] = 0
		lst_x[x1] = 0


def autoD(sf, x1):
	x, y = symbols("x y")
	#sympify converts the string to a sympy expr
	try:
		#create a sympy expression if input is valid
		express = sympify(sf)	
	except ValueError:
		#exit program if input function is not valid
		print 'Inputted function is not valid' 
		sys.exit()

	#no h input from user
	if len(sf) == 0:
		print 'input neededed in function entry field'
		sys.exit()

	#No x input from the user
	if len(x1.get()) == 0:
		print 'input neededed for x'

	#Check if the input value is an int
	if checkInt(x1.get()):
		X = int(x1.get())
	else:
		X = float(x1.get())

	expected_x = express.evalf(5, subs={x: X})
	deriv_fx = express.diff(x)
	expected_y = deriv_fx.evalf(5, subs={x: X})
	exp_str = "Expected pair is (" + str(expected_x) + ", " + str(expected_y) + ")"

	lengt = 0
	lst_x[lengt] = int(X)
	lst_y[lengt] = 1
	lengt += 1
	incr = 0
	while(incr != len(sf) or incr > len(sf)):
		# print 'size of sf: ', len(sf), ' size of incr: ', incr
		if incr == len(sf) or incr > len(sf):
			break

		if sf[incr] == '+' or sf[incr] == '-':
			print '3'
			lengt += 1
			incr += 1

		if sf[incr] == '1' or sf[incr] == '2' or sf[incr] == '3' or sf[incr] == '4' or sf[incr] == '5' or sf[incr] == '6' or sf[incr] == '7' or sf[incr] == '8' or sf[incr] == '9' or sf[incr] == '0':
			#Scenario: just a constant 1, ... 9
			print '1'
			if sf[incr + 1] == '+' or sf[incr + 1] == '-':
				lst_x[lengt] = int(sf[incr])
				lst_y[lengt] = 0
				lengt += 1
				incr+=1 		#move next operator
				if incr == len(sf) or incr > len(sf):
					break
				else:
					incr+=1 	#move next operator

			#Scenario: constant * x -> 9*x
			elif sf[incr + 1] == '*' and sf[incr+2] == 'x':
				print '2'
				lst_x[lengt] = int(sf[incr])
				lst_y[lengt] = 0
				print 
				incr+=1 	#move to '*'
				incr+=1 	#move to 'x'
				incr+=1
				if incr == len(sf) or incr > len(sf):
					ADmultip(2 ,lengt, lengt, 0, 0, 1)
					break		

				elif sf[incr] != '*':
					ADmultip(2 ,lengt, lengt, 0, 0, 1)
					lengt += 1
				else:
					lengt += 1

				#Scenario: 9*x**2
				if sf[incr + 1] == '*':
					incr+=1 	#move to '*'
					print sf[incr + 1]
					print lengt
					ADmultip(3, lengt, lengt, 0, 0, int(sf[incr + 1]))
					incr+=1 	#move to exponent
					if incr == len(sf) or incr > len(sf):
						break			
					else:
						incr += 1 	#move next operator	

				#Scenario: 9*x
				elif sf[incr + 1] == '+' or sf[incr + 1] == '-':
					ADmultip(2 ,lengt, lengt, 0, 0, 1)
					incr+=1

			else:
				print 'ERROR: invalid format. Please read the instructions for Automatic Differentiation'

		#check if the first character is a variable
		elif sf[incr] == 'x' or sf[incr] == 'X':
			if sf[incr + 1] == '*' and sf[incr + 2] == '*':
				ADmultip(1, lengt, lengt, 0, 0, int(sf[incr + 3]))
				lengt += 1
				incr+=1 	#move to '*'
				incr+=1 	#move to '*'
				incr+=1		#move to exp
				incr+=1

			#its just a variable x without constant or exponent
			elif sf[incr + 1] != '*':
				lst_x[lengt] = lst_x[0]
				lst_y[lengt] = lst_y[0]	

		else:
			print 'ERROR: Function format is not valid HERE'
			sys.exit()

	for x in range(0, lengt):
		print 'x[', x, '] = ' ,lst_x[x]
		print 'y[', x, '] = ' ,lst_y[x]
	if lengt >= 2:
		while(lengt != 1):
			lst_x[lengt - 1] = lst_x[lengt - 1] + lst_x[lengt]
			lst_y[lengt - 1] = lst_y[lengt - 1] + lst_y[lengt]
			lengt -= 1

	pop = Toplevel()
	pop.title("Automatic Differentiation")
	diffMFrame = ttk.Frame(pop, padding="15 20 15 20")
	diffMFrame.grid(column=0, row=0)
	diffMFrame.columnconfigure(0, weight=1)
	diffMFrame.rowconfigure(0, weight=1)

	output_AD = "Automatic Differentiation output: (" + str(lst_x[1]) + ", " + str(lst_y[1]) + ")"
	Label(diffMFrame, text=exp_str).grid(row=0, column=0, pady=(0,10))
	Label(diffMFrame, text=output_AD).grid(row=1, column=0, pady=(0,10))




def autoDiffM():
	Sfunc = StringVar()
	Sx = StringVar()
	#Create new pop up window
	top = Toplevel()
	top.title("Difference Method")
	diffMFrame = ttk.Frame(top, padding="15 20 15 20")
	diffMFrame.grid(column=0, row=0)
	diffMFrame.columnconfigure(0, weight=1)
	diffMFrame.rowconfigure(0, weight=1)

	#create label
	Label(diffMFrame, text="Function").grid(row=0, column=0, pady=(0,10))
	Label(diffMFrame, text="x").grid(row=1, column=0, pady=(0,10))

	#Input field for function
	Entry(diffMFrame, textvariable=Sfunc).grid(row=0, column=1, pady=(0, 10))
	Entry(diffMFrame, textvariable=Sx).grid(row=1, column=1, pady=(0, 10))

	buttn_two_frwrd = ttk.Button(diffMFrame, text="Forward Automatic Differentiation", command = lambda: autoD(Sfunc.get(), Sx)).grid(row=2, column=0, pady=(0, 10))










root = Tk()
root.title("Differentiation")
mainframe = ttk.Frame(root, padding="15 20 15 20")
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Buttons
ttk.Button (mainframe, text="Difference Method/Extrapolation", command = differenceM).grid(row=0, pady=(0, 10))
ttk.Button (mainframe, text="Automatic Differentiation", command = autoDiffM).grid(row=1, pady=(0, 0))

root.mainloop()