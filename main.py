from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()
