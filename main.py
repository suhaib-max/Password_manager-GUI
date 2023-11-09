from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def submit_add():
    #delete function to delete when a user entered then delete(first, and last index) or (0, END)

    data_web = website_entry.get()
    data_email = Email_entry.get()
    data_pass = password_entry.get()
    is_ok = messagebox.askokcancel(title="Website",message=f"These are details entered: \nEmail: {data_email}"
                                                   f"\n password: {data_pass}\n Is it ok to save")
    if is_ok:
        with open("data.txt","a") as data:
            data.write(f"{data_web} | {data_email} | {data_pass}\n")
            #after apppending
            website_entry.delete(0, END)
            Email_entry.delete(0, END)
            password_entry.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_loc = PhotoImage(file="logo.png")
canvas.create_image(100,100,image =image_loc)
canvas.grid(column=1,row=0)

#label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#input / entry

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=2)
Email_entry.insert(0,"sshuhaib274@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Button

Generate_pass_button = Button(text="Generate Password")
Generate_pass_button.grid(column=2, row=3, columnspan=2)

pass_add_button = Button(text="Add", width=36,command=submit_add)
pass_add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
