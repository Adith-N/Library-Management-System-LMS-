'''-----------------------------------------------ADMIN WINDOW----------------------------------------'''
"""SERIALISED FIELD"""
import tkinter as tk
from tkinter import messagebox
import mysql.connector as m
import random as r
import datetime as d
import time as t
import Menu as mm
import Admin as a


# Function to clear the terminal
def clear():
    for i in range(10):
        print()

# Function to connect to the MySQL database
def db_connect():
    return m.connect(user='root', host='localhost', password='Ammu2013', database='lms')

def signup(signup_window, user, pas):
    clear()
    try:
        con = db_connect()
        cur = con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS lms")
        conn = db_connect()
        cur = conn.cursor()
        table = """
        CREATE TABLE IF NOT EXISTS login_info(
            username VARCHAR(15) PRIMARY KEY,
            password VARCHAR(8) NOT NULL,
            name VARCHAR(25) NOT NULL,
            phone_number VARCHAR(10)
        )
        """
        cur.execute(table)

        if len(pas) < 5:
            messagebox.showerror("Error", "Password must be at least 5 characters long.")
            return

        ps2 = ps2_var.get()
        if ps2 != pas:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        name = name_var.get()
        mob = phone_var.get()

        if len(mob) != 10:
            messagebox.showerror("Error", "Mobile Number must be 10 digits long.")
            return

        sql = "INSERT INTO login_info (username, password, name, phone_number) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (user, pas, name, mob))
        conn.commit()
        messagebox.showinfo("Success", "Account Successfully Created")
        signup_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

def login(login_window, user, pas):
    clear()
    try:
        conn = db_connect()
        cur = conn.cursor()

        sql = "SELECT * FROM login_info WHERE username=%s AND password=%s"
        cur.execute(sql, (user, pas))
        result = cur.fetchone()

        if result:
            messagebox.showinfo("Success", "Logged into account")
            login_window.destroy()
            if user == 'Admin' and pas == 'amma2007':
                a.adminmenu()
            else:
                mm.u()
                mm.mainmenu()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

def create_signup_gui():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    tk.Label(signup_window, text="Enter Username:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(signup_window, textvariable=username_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Enter Password:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(signup_window, textvariable=password_var, show='*').grid(row=1, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Retype Password:").grid(row=2, column=0, padx=10, pady=10)
    tk.Entry(signup_window, textvariable=ps2_var, show='*').grid(row=2, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Enter Name:").grid(row=3, column=0, padx=10, pady=10)
    tk.Entry(signup_window, textvariable=name_var).grid(row=3, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Enter Mobile No:").grid(row=4, column=0, padx=10, pady=10)
    tk.Entry(signup_window, textvariable=phone_var).grid(row=4, column=1, padx=10, pady=10)

    tk.Button(signup_window, text="Sign Up", command=lambda: signup(signup_window, username_var.get(), password_var.get())).grid(row=5, column=0, columnspan=2, pady=10)

def create_login_gui():
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    tk.Label(login_window, text="Enter Username:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(login_window, textvariable=username_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Enter Password:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(login_window, textvariable=password_var, show='*').grid(row=1, column=1, padx=10, pady=10)

    tk.Button(login_window, text="Login", command=lambda: login(login_window, username_var.get(), password_var.get())).grid(row=2, column=0, columnspan=2, pady=10)


root = tk.Tk()
root.title("Library Management System")

username_var = tk.StringVar()
password_var = tk.StringVar()
ps2_var = tk.StringVar()
name_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Button(root, text="Sign Up", command=create_signup_gui).pack(pady=20)
tk.Button(root, text="Login", command=create_login_gui).pack(pady=20)

root.mainloop()

"""EXECUTION FIELD"""
con = db_connect()
