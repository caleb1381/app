import tkinter as tk
 
root = tk.Tk()

# create a Listbox widget
listbox = tk.Listbox(root)
listbox.pack()
 
# add an item to the listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

root.mainloop()