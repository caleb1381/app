import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window = tk.Tk()
window.geometry("800x700")
window.resizable(False, False)
window.title("Store App")
window.config(bg='blue')
main_window = tk.Frame(window)


def login():
        #creating widgets
        # Create a new top-level window for the login page
        my_window = tk.Toplevel()
        my_window.config(bg='blue')
        my_window.title("LOGIN")

        # Create a frame to hold the login page widgets
        Frame = tk.Frame(my_window)
        Frame.config(bg='blue')

        top_label = tk.Label(Frame, text= "LOGIN", font=('arial black', 15), fg='red', bg='blue' ) 
        login_username = tk.Label(Frame, text="Username ",  bg= 'blue', font=('arial black', 15), fg= 'red')
        username_entry = tk.Entry(Frame, font=('arial', 15))
        
        login_pass = tk.Label(Frame, text="Password ", bg= 'blue', font=('arial black', 15),  fg= 'red')
        password_entry = Entry(Frame, show='*', font=('arial', 15))

        myusername = username_entry.get()
        mypassword = password_entry.get()
        def validation():
            if myusername == mypassword and  mypassword == mypassword:
                
                messagebox.showerror("sucessful", myusername)
            else:
                messagebox.showerror("failed", "login failed")
        
        login_button = tk.Button(Frame, text="Login", font=('arial black', 10),  fg='red', bg='black', command=validation)
        register_button = tk.Button(Frame, text='Sign up', font=('arial black', 10), fg='red', bg='black')
     
        #adding the widgets to the screen
        top_label.grid(row=0 , column=0, columnspan=2, pady=40)
        login_username.grid(row= 1, column= 0, pady= 40)
        username_entry.grid(row=1 , column= 1)
        login_pass.grid(row=2, column=0, pady= 30)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0, columnspan=2, pady= 20)
        register_button.grid(row=3, column=1, pady=5, padx= 5)
        Frame.pack()
        
def register():
    #creating widgets
    # Create a new top-level window for the login page
     register_window = tk.Toplevel()
     register_window.config(bg='blue')
     register_window.title("REGISTER")

    # Create a frame to hold the login page widgets
     Frame1 = tk.Frame(register_window)
     Frame1.config(bg='blue')
    #creating my widgets
     sign_up_label = tk.Label(Frame1, text= "REGISTER", font=('arial black', 15), fg='red', bg= 'blue')
     Fname = tk.Label(Frame1, text= "FirstName", font=('arial black', 15), fg='red', bg= 'blue')
     F_name = tk.Entry(Frame1, font=('arial black', 15))
     Lname = tk.Label(Frame1, text='LastName', font=('arial black', 15), fg='red', bg='blue')
     L_name= tk.Entry(Frame1, font=('arial black', 15))
     email = tk.Label(Frame1, text='Email', font=('arial black', 15), fg='red', bg='blue')
     email_entry = tk.Entry(Frame1, font=('arial black', 15))
     login_username = tk.Label(Frame1, text="Username ",  bg= 'blue', font=('arial black', 15), fg= 'red')
     username_entry = tk.Entry(Frame1, font=('arial black', 15))
     login_pass = tk.Label(Frame1, text="Password ", bg= 'blue', font=('arial black', 15),  fg= 'red')
     password_entry = Entry(Frame1, show='*', font=('arial black', 15))
     register_button = tk.Button(Frame1, text='Sign up ', font=('arial black', 10), fg='red', bg='black')
     login_button = tk.Button(Frame1, text="Login", font=('arial black', 10),  fg='red', bg='black')
     
     #add the widget to the screen
     
     sign_up_label.grid(row=0 , column=0, columnspan=2, pady=40)
     Fname.grid(row=1, column=0, pady= 30)
     F_name.grid(row=1, column=1)
     Lname.grid(row= 2, column= 0, pady=30 )
     L_name.grid(row=2, column=1)
     email.grid(row=3, column=0, pady=30)
     email_entry.grid(row=3, column=1, pady=30)
     login_username.grid(row=4, column=0, pady=30)
     username_entry.grid(row=4, column=1)
     login_pass.grid(row=5, column=0)
     password_entry.grid(row=5, column=1)
     register_button.grid(row=6, column=0, columnspan=2, pady= 20)
     login_button.grid(row=6, column=1, pady=5, padx= 5)
      
     Frame1.pack()
    
def addItem():
   
    #work here
    addItem_window = Tk()
    addItem_window.geometry("800x700")
    addItem_window.config(bg='blue')
    addItem_window.title("ADD ITEM")
    tab = ttk.Notebook(addItem_window)
    
    window1= ttk.Frame(tab)
    window2=ttk.Frame(tab)

    tab.add(window1, text ='stock') 
    tab.add(window2, text ='sell') 
    tab.pack(expand = 1, fill ="both") 
     
    window1 =tk.Frame(tab)
    
    
def function2():
    print("Function 2")

def function3():
    print("Function 3")
    
def function4():
    print("function 4")
 
    
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="FILE", menu=file_menu)
file_menu.add_command(label="SAVE")
file_menu.add_command(label="PRINT")


edit_menu = tk.Menu(menu)
menu.add_cascade(label="ITEMS", menu=edit_menu)
edit_menu.add_command(label="ADD ITEM", command=addItem)
file_menu.add_command(label="EXIT", command=window.quit)

view_menu = tk.Menu(menu)
menu.add_cascade(label="VIEW ITEM", menu=view_menu)
view_menu.add_command(label="VIEW ITEM", command=function4 )



login_P = tk.Menu(menu)
menu.add_cascade(label="LOGIN", menu=login_P)
login_P.add_command(label='LOGIN', command=login)

register_B= tk.Menu(menu)
menu.add_cascade(label="REGISTER", menu=register_B)
register_B.add_command(label='REGISTER', command=register)


help_menu = tk.Menu(menu)
menu.add_cascade(label="HELP", menu=help_menu)
help_menu.add_command(label="Function 3", command=function3)

main_window.pack()
window.mainloop()

