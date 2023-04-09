from tkinter import *
import tkinter.messagebox as messagebox

class LoginPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=0, column=0)
        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=1)

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=1, column=0)
        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0)

        self.signup_button = Button(self, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=2, column=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # check if username and password are correct
        if username == "username" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome " + username + "!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def signup(self):
        # create a new window for signing up
        signup_window = Toplevel(self.master)
        signup_page = SignupPage(signup_window)


class SignupPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=0, column=0)
        self.username_entry = Entry(self)
        self.username_entry.grid(row=0, column=1)

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=1, column=0)
        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        self.confirm_password_label = Label(self, text="Confirm Password")
        self.confirm_password_label.grid(row=2, column=0)
        self.confirm_password_entry = Entry(self, show="*")
        self.confirm_password_entry.grid(row=2, column=1)

        self.signup_button = Button(self, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=3, column=0)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        # check if passwords match and username is not taken
        if password == confirm_password:
            messagebox.showinfo("Sign Up Successful", "Welcome " + username + "!")
            self.master.destroy()
        else:
            messagebox.showerror("Sign Up Failed", "Passwords do not match")

root = Tk()
login_page = LoginPage(root)
root.mainloop()
