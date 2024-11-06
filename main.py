from tkinter import *
import tkinter.ttk as table
import webbrowser as web
import people
import dashboard
import transaction
import passbook
from PIL import ImageTk,Image


# TODO: Testing the switching between frames (change_frame meethod)

def change_frame(frame, name, prev="None"):
    global window, people_button, transactions_button, passbook_button
    frame.destroy()
    if name == "Dashboard":
        frame = dashboard.get_frame(window)
        frame.pack(side=TOP)
        if prev == "People" or prev == "Transaction" or prev == "Passbook":
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Dashboard"))
            transactions_button.config(text="Transaction",
                                       command=lambda: change_frame(frame, "Transaction", "Dashboard"))
            passbook_button.config(text="Passbook", command=lambda: change_frame(frame, "Passbook", "Dashboard"))
            people_button.pack(side=LEFT)
            transactions_button.pack(side=LEFT)
            passbook_button.pack(side=LEFT)

    elif name == "People":
        if prev == "Transaction":
            people_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "People"))
            transactions_button.config(text="Transaction", command=lambda: change_frame(frame, "Transaction", "People"))
            passbook_button.config(text="Passbook", command=lambda: change_frame(frame, "Passbook", "People"))
        if prev == "Passbook":
            people_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "People"))
            transactions_button.config(text="Transaction", command=lambda: change_frame(frame, "Transaction", "People"))
            passbook_button.config(text="Passbook", command=lambda: change_frame(frame, "Passbook", "People"))
        if prev == "Dashboard":
            people_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "People"))
            transactions_button.config(command=lambda: change_frame(frame, "Transaction", "People"))
            passbook_button.config(command=lambda: change_frame(frame, "Passbook", "People"))

        frame = people.get_frame(window)
        frame.pack(side=TOP)

    elif name == "Transaction":
        if prev == "People":
            transactions_button.config(text="Dashboard",
                                       command=lambda: change_frame(frame, "Dashboard", "Transaction"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Transaction"))
            passbook_button.config(text="Passbook", command=lambda: change_frame(frame, "Passbook", "Transaction"))
        if prev == "Passbook":
            transactions_button.config(text="Dashboard",
                                       command=lambda: change_frame(frame, "Dashboard", "Transaction"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Transaction"))
            passbook_button.config(text="Passbook", command=lambda: change_frame(frame, "Passbook", "Transaction"))
        if prev == "Dashboard":
            transactions_button.config(text="Dashboard",
                                       command=lambda: change_frame(frame, "Dashboard", "Transaction"))
            people_button.config(command=lambda: change_frame(frame, "People", "Transaction"))
            passbook_button.config(command=lambda: change_frame(frame, "Passbook", "Transaction"))
        frame = transaction.get_frame(window)
        frame.pack(side=TOP)

    elif name == "Passbook":
        if prev == "People":
            passbook_button.config(text="Dashboard",
                                   command=lambda: change_frame(frame, "Dashboard", "Passbook"))
            transactions_button.config(text="Transaction",
                                       command=lambda: change_frame(frame, "Transaction", "Passbook"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Passbook"))
        if prev == "Transaction":
            passbook_button.config(text="Dashboard",
                                   command=lambda: change_frame(frame, "Dashboard", "Passbook"))
            people_button.config(text="People", command=lambda: change_frame(frame, "People", "Passbook"))
            transactions_button.config(text="Transaction",
                                       command=lambda: change_frame(frame, "Transaction", "Passbook"))
        if prev == "Dashboard":
            passbook_button.config(text="Dashboard", command=lambda: change_frame(frame, "Dashboard", "Passbook"))
            transactions_button.config(command=lambda: change_frame(frame, "Transaction", "Passbook"))
            people_button.config(command=lambda: change_frame(frame, "People", "Passbook"))
        frame = passbook.get_frame(window)
        frame.pack(side=TOP)


# This method adds the menu to the program.
def add_menu(window):
    menu = Menu(window)
    window.config(menu=menu)

    files_menu = Menu(menu)
    help_menu = Menu(menu)

    files_menu.add_command(label="Exit", command=window.quit)

    about_menu = Menu(help_menu)
    about_menu.add_command(label="Arcot Prashanth",
                           command=lambda: web.open("https://www.linkedin.com/"))
    about_menu.add_command(label="Manoj Kumar",
                           command=lambda: web.open("https://www.linkedin.com/"))

    help_menu.add_cascade(label="About", menu=about_menu)

    menu.add_cascade(label="File", menu=files_menu)
    menu.add_cascade(label="Help", menu=help_menu)
def check():
    if name_input.get() == "admin":
        if pass_input.get() == "admin": 
            name_input.delete(0, END)
            pass_input.delete(0,END)
            main1()
    else:
        messagebox.showerror("UNAUTHORIZED ACCESS !","INCORRECT PASSWORD")

# Main Logic of the function
def main1():
    main_screen.destroy()
    window = Tk()
    window.title("Family Transaction Management System")
    add_menu(window)
    frame = dashboard.get_frame(window)
    frame.pack(side=TOP)
    navigation_frame = Frame(window)
    people_button = Button(navigation_frame, text="People", command=lambda: change_frame(frame, "People", "Dashboard"))
    transactions_button = Button(navigation_frame, text="Transactions",
                                command=lambda: change_frame(frame, "Transaction", "Dashboard"))
    passbook_button = Button(navigation_frame, text="Passbook",
                            command=lambda: change_frame(frame, "Passbook", "Dashboard"))
    quit_button = Button(navigation_frame, text="Quit", command=window.quit)
    people_button.pack(side=LEFT)
    transactions_button.pack(side=LEFT)
    passbook_button.pack(side=LEFT)
    quit_button.pack(side=LEFT)
    navigation_frame.pack(side=BOTTOM)
    window.mainloop()
    
main_screen = Tk()
main_screen.title("Account Login")
password=StringVar()
main_screen.geometry("1560x845")


img = ImageTk.PhotoImage(Image.open("image.png"))
img_label = Label(main_screen, image=img,text="School Iamge")
img_label.place(x=0,y=0)

namelbl=Label(main_screen,text="USER NAME",font=('Papyrus 18 bold'),fg="Black",bg="Blue")
namelbl.place(x=300,y=300)

passlbl=Label(main_screen,text="PASSWORD",font=('Papyrus 18 bold'))
passlbl.place(x=300,y=400)

name_input=Entry(main_screen,width=10,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN,fg="White",bg="Blue")
name_input.place(x=600,y=300)

pass_input=Entry(main_screen,width=10,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN)
pass_input.place(x=600,y=400)
pass_input.config(show="*")
# admin_b=Button(main_screen,text="ADMIN", height="2", width="30",font=("Courier 25 bold"),bg="Tomato")
# admin_b.place(relx=0.37,rely=0.28,relheight=0.11,relwidth=0.25)
# admin_e= Entry(main_screen, textvariable=password,font=("Courier 23 bold"),show="*")
# admin_e.place(relx=0.37,rely=0.40)
# print(admin_e.get())

# coun1=Button(main_screen,text="Counter-1", height="2", width="30",font=("Courier 25 bold"), bg="DodgerBlue")
# coun1.place(relx=0.231,rely=0.715,relheight=0.13,relwidth=0.205)

coun2=Button(main_screen,text="LOGIN", height="2", width="30",font=("Courier 25 bold"), bg="MediumSeaGreen",command=check)
coun2.place(relx=0.553,rely=0.715,relheight=0.13,relwidth=0.205)
main_screen.mainloop()


