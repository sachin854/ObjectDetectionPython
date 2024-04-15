import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Dummy login credentials
USERNAME = "admin"
PASSWORD = "password"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome to Hacking World, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("700x400")

# Function to resize the background image
def resize_background(event):
    global background_photo
    root_width, root_height = event.width, event.height
    background_image_resized = background_image.resize((root_width, root_height), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image_resized)
    background_label.config(image=background_photo)

# Fetch Network Image
image_url = "https://as2.ftcdn.net/v2/jpg/04/60/71/01/1000_F_460710131_YkD6NsivdyYsHupNvO3Y8MPEwxTAhORh.jpg"  # Replace with the URL of your network image
response = requests.get(image_url)
if response.status_code == 200:
    background_image = Image.open(BytesIO(response.content))
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bind the root window to the resize_background function
root.bind("<Configure>", resize_background)

# Username Label and Entry with Styles
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14, "bold"), foreground="white", background="transparent")
style.configure("TEntry", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 12, "bold"), foreground="white", background="#062775", padding=5, borderwidth=2, relief="ridge") 

label_username = ttk.Label(root, text="Username:")
label_username.pack(pady=10, anchor="center")
entry_username = ttk.Entry(root)
entry_username.pack(anchor="center")

# Password Label and Entry with Styles
label_password = ttk.Label(root, text="Password:")
label_password.pack(anchor="center")
entry_password = ttk.Entry(root, show="*")
entry_password.pack(anchor="center")

# Login Button with Styles
style.configure("TButton", font=("Arial", 12, "bold"), foreground="white", background="#062775", padding=5)
button_login = ttk.Button(root, text="Login", command=login)
button_login.pack(pady=10, anchor="center")

root.mainloop()
