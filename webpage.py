import tkinter as tk
from tkinter import messagebox

def check_login(username, password):
    # Replace this with your authentication logic
    # For simplicity, let's assume username is "admin" and password is "password"
    return username == "admin" and password == "password"

def show_home_screen():
    home_screen = tk.Toplevel(root)
    home_screen.title("Home Screen")

    # Create the menu bar for the home screen with blue background
    menubar = tk.Menu(home_screen, bg="blue", fg="white", activebackground="blue", activeforeground="white", font=("Arial", 12, "bold"))
    menubar.add_command(label="Profile", command=show_profile_screen)
    menubar.add_command(label="Categories", command=show_categories_screen)
    home_screen.config(menu=menubar)

    # Dummy list of items
    items_list = [
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
    ]

    welcome_label = tk.Label(home_screen, text="Welcome to the Home Screen!", fg="black", font=("Arial", 16, "bold"))
    welcome_label.pack(pady=10)

    # Display the list of items
    listbox = tk.Listbox(home_screen, bg="white", fg="black", font=("Arial", 12), selectbackground="lightblue")
    for item in items_list:
        listbox.insert(tk.END, item)
    listbox.pack()

def show_profile_screen():
    profile_screen = tk.Toplevel(root)
    profile_screen.title("Profile Screen")
    label = tk.Label(profile_screen, text="Welcome to the Profile Screen!", fg="black", font=("Arial", 16, "bold"))
    label.pack()

def show_categories_screen():
    categories_screen = tk.Toplevel(root)
    categories_screen.title("Categories Screen")
    label = tk.Label(categories_screen, text="Welcome to the Categories Screen!", fg="black", font=("Arial", 16, "bold"))
    label.pack()

def login():
    username = entry_username.get()
    password = entry_password.get()

    if check_login(username, password):
        show_home_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")

# Create a frame for login elements
login_frame = tk.Frame(root)
login_frame.pack(pady=50)

label_username = tk.Label(login_frame, text="Username", fg="black", font=("Arial", 14))
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(login_frame, font=("Arial", 14))
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(login_frame, text="Password", fg="black", font=("Arial", 14))
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(login_frame, show="*", font=("Arial", 14))
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(login_frame, text="Login", command=login, bg="blue", fg="white", font=("Arial", 14, "bold"))
button_login.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
