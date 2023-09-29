from tkinter import *

def Login():
    print("Welcome " + e1.get())
    print("Your id is " + e2.get())

m = Tk()

m.title('Login')

# button = tk.Button(m, text = 'stop', width = 25, command = m.destroy)

# button.pack()

Label(m, text= 'First name').grid(row = 0)

Label(m, text= 'ID').grid(row = 1)

e1 = Entry(m)
e2 = Entry(m)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

btn = Button(m, text = 'Login', command = Login).grid(row = 2, column = 1)

m.mainloop()