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
canvas.pack()


window.mainloop()
