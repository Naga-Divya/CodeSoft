
from tkinter import *
import random
def password_generator( entry_field):
    numeric="0123456789"
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case="abcdefghijklmnopqrstuvwxyz"
    spcl_char="!@#$%^&*(){}:"
    password=""
    length=int(entry_field.get())
    characters=numeric+upper_case+lower_case+spcl_char
    password = ''.join(random.choice(characters) for _ in range(length))
    output_var.set( password)
    
window = Tk()
window.geometry("700x350")
window.title("Password Generator")
window.configure(bg="#00f2fe")

# Create a frame with border settings
frame1 = Frame(window, bd=3, bg="#fed6e3" , highlightbackground="black", highlightthickness=1, highlightcolor='blue'  )
frame1.pack(padx=200, pady=100 )
#frame1.configure( width=50 , height=500 )

pass_title = Label(frame1, text="PASSWORD GENERATOR" ,fg="blue" , bg="#fed6e3" ,font=("Arial", 12, "bold"))
pass_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

pass_label = Label(frame1, text="Enter password length:", fg="green" )
pass_label.grid(row=1, column=0, padx=(10, 5), pady=(0, 5))

entry_field =Entry(frame1)
entry_field.grid(row=1, column=1, padx=(5, 10), pady=(0, 5))

generate_button = Button(frame1, text="Generate password",width=15 , height=2 , fg="blue" , bg="#fed6e3" , command= lambda:password_generator(entry_field))
generate_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

output_var=StringVar()
output_field = Entry(frame1 , width = 20 ,textvariable=output_var)
output_field.grid(row=3, column=0,columnspan = 2 , padx=(5, 10), pady=(10, 5))

copy_button = Button(frame1,text="copy to clipboard",width=15 , height=2)
copy_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))



window.mainloop()

