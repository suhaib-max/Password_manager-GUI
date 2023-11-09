from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
image_loc = PhotoImage(file="logo.png")
canvas.create_image(100,100,image =image_loc)
canvas.grid(column=1,row=0)

#label
website_label = Label(text="website:")
website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
window.mainloop()

