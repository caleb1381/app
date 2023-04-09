#using sqlite3
import tkinter as tk
from tkinter import *
import sqlite3

window = tk.Tk()
window.geometry("900x700")
window.resizable(False, False)
window.title("Store App")

#create database in sqlite3

conn = sqlite3.connect('store.db')

#create cursor
cur = conn.cursor()

#create table 

cur.execute(
'''
     CREATE TABLE if not exists employee (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        phone_no INTEGER,
        address TEXT
        )
    '''
    )

    
def submit():
    
    conn = sqlite3.connect('store.db')

#create cursor
    cur = conn.cursor()
    
    #insert into employee table  
    
    query = "INSERT INTO employee (id, name, age, phone_no, address) VALUES (?, ?, ?, ?, ?)"
    values = (2, "caleb", 26, 8138380065, "zion_street")
    cur.execute(query, values)

    

    conn.commit()
    cur.close()
    conn.close()
    
def query():
    conn = sqlite3.connect('store.db')

#create cursor
    cur = conn.cursor()
    cur.execute("SELECT *, oid from employee " )
    result = cur.fetchall()
    print(result)
    #commit changes to the database
    
# Delete the row with duplicate id value
    cur.execute("DELETE FROM employee WHERE id=2")
    rest = cur.fetchall()
    print(rest)
    
    cur.close()
    conn.commit()
    conn.close() 

    
    #clear boxes of texbox
    id.delete(0,END)
    name.delete(0, END)
    age.delete(0,END)
    phone_no.delete(0, END)
    address.delete(0,END)
    
    

#create textbox

id = Entry(window, width= 30)
id.grid(row=0, column= 1, padx = 20)

name = Entry(window, width=30)
name.grid(row=1, column=1)

age = Entry(window, width=30)
age.grid(row=2, column=1)

phone_no = Entry(window, width= 30)
phone_no.grid(row=3, column= 1)

address = Entry(window, width= 30)
address.grid(row=4, column= 1)

    #create textbox label
id_label = Label(window, text= "id")
id_label.grid(row=0, column=0)

name_label = Label(window, text= "name")
name_label.grid(row=1, column=0)

age_label = Label(window, text= "age")
age_label.grid(row=2, column=0)

phone_label = Label(window, text= "phone number")
phone_label.grid(row=3, column=0)

address_label = Label(window, text= "address")
address_label.grid(row=4, column=0)

    #clear text boxes
submit_button = Button(window, text=" add record to database ", command=submit)
submit_button.grid(row=5, column=1, padx=10, columnspan=2, pady=10, ipadx=100)
    
query_button = Button(window, text="show records ", command=query)
query_button.grid(row=6, column=1, padx=10, columnspan=2, pady=10, ipadx=137)


#commit changes

conn.commit()
conn.close()

window.mainloop()