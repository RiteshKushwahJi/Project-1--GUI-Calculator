import tkinter as tk
from tkinter import *
expression = "" 


def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression)


def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 
		
	except: 

		equation.set(" error..... ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="light gray") 

	# set the title of GUI window 
	gui.title("GUI CALCULATOR") 

	# set the configuration of GUI window 
	gui.geometry("310x250")
	gui.resizable(0,0)
	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(gui, textvariable=equation,bg="light green",font=("Arial",20,'bold')) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=4, ipadx=5)

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(gui, text=' 1 ', fg='white', bg='gray',command=lambda: press(1), height=1, width=5,font=('Arial',10,'bold')) 
	button1.grid(row=4, column=0) 

	button2 = Button(gui, text=' 2 ', fg='white', bg='gray',command=lambda: press(2), height=1, width=5,font=('Arial',10,'bold')) 
	button2.grid(row=4, column=1) 

	button3 = Button(gui, text=' 3 ', fg='white', bg='gray',command=lambda: press(3), height=1, width=5,font=('Arial',10,'bold')) 
	button3.grid(row=4, column=2) 

	button4 = Button(gui, text=' 4 ', fg='white', bg='gray',command=lambda: press(4), height=1, width=5,font=('Arial',10,'bold')) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='white', bg='gray',command=lambda: press(5), height=1, width=5,font=('Arial',10,'bold')) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='white', bg='gray',command=lambda: press(6), height=1, width=5,font=('Arial',10,'bold')) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='white', bg='gray',command=lambda: press(7), height=1, width=5,font=('Arial',10,'bold')) 
	button7.grid(row=2, column=0) 

	button8 = Button(gui, text=' 8 ', fg='white', bg='gray',command=lambda: press(8), height=1, width=5,font=('Arial',10,'bold')) 
	button8.grid(row=2, column=1) 

	button9 = Button(gui, text=' 9 ', fg='white', bg='gray',command=lambda: press(9), height=1, width=5,font=('Arial',10,'bold')) 
	button9.grid(row=2, column=2) 

	button0 = Button(gui, text=' 0 ', fg='white', bg='gray',command=lambda: press(0), height=1, width=5,font=('Arial',10,'bold')) 
	button0.grid(row=5, column=1) 
    
	percent = Button(gui, text=' % ', fg='black', bg='#FFBF00',command=lambda: press("*1/100*"), height=1, width=5,font=('Arial',10,'bold')) 
	percent.grid(row=5, column=2)
	
	plus = Button(gui, text=' + ', fg='black', bg='#FFBF00',command=lambda: press("+"), height=1, width=5,font=('Arial',10,'bold')) 
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' − ', fg='black', bg='#FFBF00',command=lambda: press("-"), height=1, width=5,font=('Arial',10,'bold')) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' × ', fg='black', bg='#FFBF00',command=lambda: press("*"), height=1, width=5,font=('Arial',10,'bold')) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' ÷ ', fg='black', bg='#FFBF00',command=lambda: press("/"), height=1, width=5,font=('Arial',10,'bold')) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='#FFBF00',command=equalpress, height=1, width=5,font=('Arial',10,'bold')) 
	equal.grid(row=6, column=3) 

	clear = Button(gui, text='AC', fg='black', bg='light gray',command=clear, height=1, width=5,font=('Arial',10,'bold')) 
	clear.grid(row=7, column='1')
	
	Decimal= Button(gui, text='.', fg='white', bg='gray',command=lambda: press('.'), height=1, width=5,font=('Arial',10,'bold')) 
	Decimal.grid(row=5, column=0)
	
	power= Button(gui, text='aᵇ', fg='black', bg='light gray',command=lambda: press('**'), height=1, width=5,font=('Arial',10,'bold'))
	power.grid(row=6, column=1)
	
	lb = Button(gui, text=' ( ', fg='black', bg='light gray',command=lambda: press('('), height=1, width=5,font=('Arial',10,'bold')) 
	lb.grid(row=6, column=0) 

	rb = Button(gui, text=')', fg='black', bg='light gray',command=lambda: press(')'), height=1, width=5,font=('Arial',10,'bold')) 
	rb.grid(row=6, column='2')  

	Exit = Button(gui, text=' Exit ', fg='red', bg='black',command=exit, height=1, width=5,font=('Arial',10,'bold')) 
	Exit.grid(row=1, column='3') 

	# start the GUI 
	gui.mainloop() 
