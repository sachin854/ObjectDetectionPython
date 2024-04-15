import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def check_login(username, password):
    # Replace this with your authentication logic
    # For simplicity, let's assume username is "admin" and password is "password"
    return username == "admin" and password == "password"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if check_login(username, password):
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        # Add code to open the home screen or main application here
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.config(bg="#f0f0f0")  # Set the background color

# Load the logo image from an online URL
logo_url = "https://as2.ftcdn.net/v2/jpg/04/60/71/01/1000_F_460710131_YkD6NsivdyYsHupNvO3Y8MPEwxTAhORh.jpg"
response = requests.get(logo_url)
logo_image = Image.open(BytesIO(response.content))
logo_image = logo_image.resize((100, 100))  # Resize the image to fit the UI
logo_image = ImageTk.PhotoImage(logo_image)

# Create a frame for login elements
login_frame = tk.Frame(root, bg="#ffffff")  # Set frame background color
login_frame.pack(pady=20, padx=20)

# Add the logo to the login page
logo_label = tk.Label(root, image=logo_image, bg="#f0f0f0")
logo_label.pack(pady=10)

label_username = tk.Label(login_frame, text="Username", fg="#000000", font=("Arial", 14))
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(login_frame, font=("Arial", 14))
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(login_frame, text="Password", fg="#000000", font=("Arial", 14))
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(login_frame, show="*", font=("Arial", 14))
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(login_frame, text="Login", command=login, bg="#007BFF", fg="#ffffff", font=("Arial", 14, "bold"))
button_login.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
