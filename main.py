import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def generat_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols =[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range(nr_letters)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    #entry_password.delete(0,END)
    entry_password.insert(0,password)
    pyperclip.copy(password)


def search():
    website = entry_website.get()
    try:
        with open("saver.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=f"{entry_website.get()}", message=f"Email: {data[website]["email"]}\n"
                                                                f"Password: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.") 
    
# ---------------------------- SAVE PASSWORD ------------------------------- 
def saver():

    new_data = {
        entry_website.get():{
            "email": entry_email.get(),
            "password": entry_password.get()
        }
    }

    if len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields entry")

    else:
            try:
                with open("saver.json", "r") as data_file :
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("saver.json", "w") as data_file :
                    json.dump(new_data, data_file, indent=4)       
            else:
                data.update(new_data)
                with open("saver.json", "w") as data_file :
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0,END)
                entry_password.delete(0,END),

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generater")
window.config(padx=50, pady=50)
window.configure(bg="white")


canvas = Canvas(width=200, height=200,bg="white",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:",bg="white",highlightthickness=0)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:",bg="white",highlightthickness=0)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:",bg="white",highlightthickness=0)
password_label.grid(column=0, row=3)


#entry
entry_website = Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_email = Entry(width=40)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0,"berkayberk.bektas@hotmail.com")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

#button
button_search = Button(text="Search",width=15, command=search,bg="white",highlightthickness=0)
button_search.grid(column=2,row=1)

button_generate = Button(text="Generate Password",command=generat_password,bg="white",highlightthickness=0)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add",width=35, command=saver,bg="white",highlightthickness=0)
button_add.grid(column=1,row=4,columnspan=2)






window.mainloop()
