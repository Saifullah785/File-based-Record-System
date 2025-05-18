from tkinter import *
from tkinter import messagebox


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        F1 = Frame(self.root, bd=10, relief=GROOVE)
        F1.place(x=450, y=150, height=350)

        self.username = StringVar()
        self.password = StringVar()

        title = Label(F1, text="Login System", font=("times new roman", 30, "bold")).grid(row=0, columnspan=2,pady=20)
      
        User = Label(F1, text="Username", font=("times new roman", 25, "bold")).grid(row=1, column=0,pady=10,padx=10)

        txtuser = Entry(F1, bd=7, relief=GROOVE,textvariable=self.username,width=25, font=("arial", 15, "bold")).grid(row=1, column=1, pady=10, padx=10)

        Password = Label(F1, text="Password", font=("times new roman", 20, "bold")).grid(row=2, column=0,pady=10,padx=10)

        txtpass = Entry(F1, bd=7, relief=GROOVE,show="*",textvariable=self.password,width=25, font=("arial", 15, "bold")).grid(row=2, column=1, pady=10, padx=10)

        btnlogin = Button(F1, text="Login", width=10, font=("arial", 15, "bold"), bd=7,command=self.login).place(x=10, y=250)

        btnlogin = Button(F1, text="Reset", width=10,  font=("arial", 15, "bold"), bd=7,command=self.reset).place(x=170, y=250)

        btnlogin = Button(F1, text="Exit", width=10,  font=("arial", 15, "bold"), bd=7,command=self.exit_fun).place(x=320, y=250)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            if self.username.get() == "admin" and self.password.get() == "admin":
                messagebox.showinfo("Success", "Welcome to the system")
            else:
                messagebox.showerror("Error", "Invalid username or password")
    def reset(self):
        self.username.set("")
        self.password.set("")
    def exit_fun(self):

        option=messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if option == True:
            self.root.destroy()
        else:
            return


root=Tk()
ob=login(root)
root.mainloop()
        