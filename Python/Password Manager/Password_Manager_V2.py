# ---------------------------- IMPORTS -------------------------------------#
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------ #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {username} "
            f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                # Try opening the file for reading existing data
                with open("data.json", "r") as data_file:
                    # Load existing data
                    data = json.load(data_file)

            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Update existing data with new data
                data.update(new_data)
                # Save the updated data back to the file
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD -----------------------------#


def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=
                f"Email: {email}\nUsername: {username}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error",
                                message=f"No details for {website} exist.")

    finally:
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ----------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Entries
website_entry = Entry(width=23)
username_entry = Entry(width=41)
password_entry = Entry(width=23)

website_entry.focus()
username_entry.insert(0, "no@gmail.com")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=37, command=add_password)
search_button = Button(text="Search", width=15, command=search_password)

# Grid
canvas.grid(row=0, column=1, columnspan=1)

website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1, columnspan=1)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=1)

generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

# Main Loop
window.mainloop()
