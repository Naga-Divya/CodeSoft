from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator")

# Starting with functions

# Function to update the input field whenever a number button is clicked
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the input field
def bt_clear():
    global expression 
    expression = "" 
    input_text.set("")

# Function to delete the last character in the input field
def bt_back():
    current = input_text.get()
    new_text = current[:-1]
    input_text.set(new_text)

# Function to evaluate the expression and display the result
def bt_equal():
    try:
        result = str(eval(expression)) 
        input_text.set(result)
    except:
        input_text.set("Error")

expression = ""

input_text = StringVar()
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

# First row
clear = Button(btns_frame, text="AC", fg="white", width=32, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: bt_clear())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
back = Button(btns_frame, text="DEL", fg="white", width=15, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: bt_back())
back.grid(row=0, column=1, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click("/"))
divide.grid(row=0, column=3,columnspan=2, padx=1, pady=1)

# Second row
seven = Button(btns_frame, text="7", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(7))
seven.grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(8))
eight.grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(9))
nine.grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

# Third row
four = Button(btns_frame, text="4", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(4))
four.grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(5))
five.grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(6))
six.grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click("-"))
minus.grid(row=2, column=3, padx=1, pady=1)

# Fourth row
one = Button(btns_frame, text="1", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(1))
one.grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(2))
two.grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(3))
three.grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

# Fourth row
zero = Button(btns_frame, text="0", fg="white", width=21, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click(0))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: btn_click("."))
point.grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2", relief="raised", command=lambda: bt_equal())
equals.grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
