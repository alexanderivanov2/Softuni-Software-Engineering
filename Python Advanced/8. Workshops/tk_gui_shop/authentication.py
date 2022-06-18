import json
from tkinter import Button, Entry, Label
from canvas import tk
from helpers import clean_screen
from products import render_products


def login(username, password):
    with open('db/user_credentials.txt', 'r') as file:
        lines = file.readlines()
        find = False
        for line in lines:
            usern, psword = line[:-1].split(", ")
            if username == usern and password == psword:
                with open("db/current_user.txt", "w") as file:
                    file.write(username)
                render_products()
                return

        render_login("Invalid Username or Password")


def register(**user):
    user.update({"products": []})
    with open("db/users.txt", "a") as file:
        file.write(json.dumps(user))
        file.write("\n")
    with open("db/user_credentials.txt", "a") as file:
        file.write(f"{user.get('username')}, {user.get('password')}")
        file.write("\n")
    render_login()


def render_login(errors=None):
    clean_screen()
    tk.title('Login')
    Label(tk, text="Username").grid(row=0, column=0)
    Label(tk, text="Password").grid(row=1, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)
    Button(tk, text="Enter", bg="green", fg="black", command=lambda: login(username.get(), password.get())).grid(row=0,
                                                                                                                 column=2)
    Button(tk, text="Register", bg="yellow", fg='black', command=render_register).grid(row=1, column=2)
    Button(tk, text="Back", bg="blue", fg="white", command=render_main_enter_screen).grid(row=2, column=2)
    if errors:
        Label(tk, text=errors).grid(row=2, column=1)


def render_register():
    clean_screen()
    Label(tk, text="Username").grid(row=0, column=0)
    Label(tk, text="Password").grid(row=1, column=0)
    Label(tk, text="First Name").grid(row=2, column=0)
    Label(tk, text="Last Name").grid(row=3, column=0)
    tk.title('Register')
    username = Entry(tk)
    username.grid(row=0, column=1)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)
    first_name = Entry(tk)
    first_name.grid(row=2, column=1)
    last_name = Entry(tk)
    last_name.grid(row=3, column=1)
    Button(tk, text="Register", bg="blue", fg="white",
           command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(),
                                    last_name=last_name.get())).grid(row=4,
                                                                     column=0)
    Button(tk, text="Back", bg="green", fg="black", command=render_main_enter_screen).grid(row=4, column=1)


def render_main_enter_screen():
    clean_screen()
    Button(tk, text="Login", bg="green", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black", command=render_register).grid(row=0, column=1)
