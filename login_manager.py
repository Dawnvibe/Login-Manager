from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk, Image
import time
import datetime as dt

root = Tk()
root.title("Test 1 2021")
root.geometry("375x600")
root.resizable(0, 0)

def login():
    # Creating the string for the Background colour palette
    # eg Framing the entire root program
    j = 0
    r = 0

    for i in range(100):
        c = str(276727+r)
        frame1 = Frame(root, width=375, height=575, bg="#"+c).place(x=j, y=25)
        j = j+10
        r = r+1
        # I like to add time and date to my works
        # It helps to know exactly when...what
        def clock():
            day = time.strftime("%A")
            daynumber = time.strftime("%d")
            month = time.strftime("%B")
            year = time.strftime("%Y")
            hour = time.strftime("%H")
            minutes = time.strftime("%M")
            seconds = time.strftime("%S")

            clock_label = Label(frame1, text="", bg='#276727', border=0)
            clock_label.place(x=155, y=575)
            clock_label.config(
                text=day + "  " + daynumber + "  " + month + "  " + year + "  " + hour + ":" + minutes + ":" + seconds)
            clock_label.after(1000, clock)

            def update():
                clock_label.config(update)

        clock()

    # Inserting an extra frame...
    # To place the entry points and the buttons
    frame2 = Frame(frame1, width=250, height=430, bg="#696969").place(x=65, y=100)

    # Configuring specific fonts and font-types
    label1_font = Font(size=15, weight="bold")
    label2_font = Font(size=15, weight="bold")
    # Writing the labels
    label1 = Label(frame2, text="Username", bg="#696969", font=label1_font)
    label1.place(x=95, y=250)

    label2 = Label(frame2, text="Password", bg="#696969", font=label2_font)
    label2.place(x=95, y=350)

    # Writing the Entry Points
    entry1 = Entry(frame2, width=20, border=0, bg="#696969", highlightbackground="#696969", highlightcolor="#696969")
    entry1.place(x=95, y=280)

    entry2 = Entry(frame2, width=20, border=0, bg="#696969", highlightbackground="#696969", highlightcolor="#696969")
    entry2.place(x=95, y=380)

    # Creating the Entry Lines
    frame3 = Frame(frame2, width=180, height=2, bg="#141414").place(x=95, y=300)
    frame4 = Frame(frame2, width=180, height=2, bg="#141414").place(x=95, y=400)

    # Inserting the Login Logo
    image1 = Image.open("login2.png")
    tkimage1 = ImageTk.PhotoImage(image1)

    label3 = Label(image=tkimage1, width=200, height=100, bg="#696969", border=0)
    label3.image = tkimage1
    label3.place(x=90, y=110)

    # Creating the Login Buttons
    button1 = Button(frame2, width=20, height=3, fg="dark green", bg="#200200200", text="L O G I N", border=0)
    button1.configure(borderwidth=0, highlightbackground="#200200200", relief="flat", highlightthickness=0)
    button1.place(x=100, y=425)

    button2 = Button(root, width=20, height=2, fg="black", bg="#200200200", text="Forgot Password ?",
                     border=0)
    button2.configure(borderwidth=0, activeforeground='dark green', highlightbackground="#200200200", relief="flat",
                      highlightthickness=0)
    button2.place(x=100, y=485)


login()

# Creating the Main Buttons
button_login1 = Button(root, width=15, height=0, text="L O G I N", pady=4, command=login, border=0, bg="dark green")
button_login1.configure(activebackground="dark green")
button_login1.configure(borderwidth=0, highlightbackground="#276727", relief="flat", highlightthickness=0)
button_login1.place(x=0, y=0)

button_login2 = Button(root, width=15, height=0, text="Sign Up", pady=4, border=0, bg="#001890")
button_login2.configure(activebackground="#001890")
button_login2.configure(borderwidth=0, highlightbackground="#001890", relief="flat", highlightthickness=0)
button_login2.place(x=130, y=0)

button_login3 = Button(root, width=14, height=0, text="Password Reset", pady=4, border=0, bg="#B2010F")
button_login3.configure(activebackground="#B2010F")
button_login3.configure(borderwidth=0, highlightbackground="#B2010F", relief="flat", highlightthickness=0)
button_login3.place(x=250, y=0)


root.mainloop()
