
t):
File "c:\Users\USER\APP\appLayout.py", line 38, in
Frame.pack()
TypeError: Pack.pack_configure() missing 1 required positional argument: 'self'
PS C:\Users\USER\APP>

calskid

The error message you are seeing (TypeError: Pack.pack_configure() missing 1 required positional argument: 'self') suggests that there is an issue with the Frame.pack() call at the end of your code.

Based on what you've provided, it looks like you may have accidentally left off the name of the frame before the .pack() call. Try replacing Frame.pack() with main_frame.pack() (or whatever you named your frame) to see if that resolves the issue.

Here is an example of what your code might look like with this change:

Diff
Copy
Insert
New
import tkinter as tk

def open_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")

    login_frame = tk.Frame(login_window)

    top_label = tk.Label(login_frame, text="LOGIN", font=('arial black', 15), fg='red', bg='blue')
    login_username = tk.Label(login_frame, text="Username ", bg='blue', font=('arial black', 15), fg='red')
    username_entry = tk.Entry(login_frame, font=('arial', 15))

    login_pass = tk.Label(login_frame, text="Password ", bg='blue', font=('arial black', 15), fg='red')
    password_entry = tk.Entry(login_frame, show='*', font=('arial', 15))

    login_button = tk.Button(login_frame, text="Login", font=('arial black', 10), fg='red', bg='black')
    register_button = tk.Button(login_frame, text='Sign up', font=('arial black', 10), fg='red', bg='black')

    top_label.grid(row=0, column=0, columnspan=2, pady=40)
    login_username.grid(row=1, column=0, pady=40)
    username_entry.grid(row=1, column=1)
    login_pass.grid(row=2, column=0, pady=30)
    password_entry.grid(row=2, column=1)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)
    register_button.grid(row=3, column=1, pady=5, padx=5)

    login_frame.pack()

# Create the main window
root = tk.Tk()
root.title("My App")

# Create a frame to hold the main content
main_frame = tk.Frame(root)

# Add main content widgets here...

# Add button to open login page
login_button = tk.Button(main_frame, text="Login", command=open_login_window)
login_button.pack()

main_frame.pack()
root.mainloop()
In this updated version of your code, I've replaced Frame with main_frame in the pack call at the end of the program. Let me know if that helps!

Ask a question...
