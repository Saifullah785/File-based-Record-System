from tkinter import *
from tkinter import ttk, messagebox
import time
import os

class File_App:
    def __init__(self, root):
        self.root = root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="File Based Record System",bd=10,pady=10,relief=GROOVE, font=("times new roman", 35, "bold")).pack( fill=X)
        Student_frame = Frame(self.root, bd=10, relief=GROOVE)
        Student_frame.place(x=20, y=100, height=450)

        stitle = Label(Student_frame, text="Student Details", font=("times new roman", 20, "bold")).grid(row=0, columnspan=4, pady=20)

        lbsid = Label(Student_frame, text="Student ID", font=("times new roman", 20, "bold")).grid(row=1, column=0, pady=10, padx=20,sticky="w")
        txtsid = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=1, column=1, pady=10, padx=10)

        lblcontact = Label(Student_frame, text="Contact No", font=("times new roman", 20, "bold")).grid(row=1, column=2, pady=10, padx=20,sticky="w")
        txtcontact = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=1, column=3, pady=10, padx=10)

        lbname = Label(Student_frame, text="Name", font=("times new roman", 20, "bold")).grid(row=2, column=0, pady=10, padx=20,sticky="w")
        txtname = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=2, column=1, pady=10, padx=10)

        lbldate = Label(Student_frame, text="Date (dd/mm/yyyy)", font=("times new roman", 20, "bold")).grid(row=2, column=2, pady=10, padx=20,sticky="w")
        txtdate = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=2, column=3, pady=10, padx=10)

        lblcourse = Label(Student_frame, text="Course", font=("times new roman", 20, "bold")).grid(row=3, column=0, pady=10, padx=20,sticky="w")
        txtcourse = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=3, column=1, pady=10, padx=10)
 
        lbladdress = Label(Student_frame, text="Address", font=("times new roman", 20, "bold")).grid(row=4, column=0, pady=10, padx=20,sticky="w")
        txtaddress = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=4, column=1, pady=10, padx=10)

        lblcity = Label(Student_frame, text="City", font=("times new roman", 20, "bold")).grid(row=5, column=0, pady=10, padx=20,sticky="w")
        txtcity = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, relief=GROOVE,width=22).grid(row=5, column=1, pady=10, padx=10)

        lblselect_degree = Label(Student_frame, text="Select Degree", font=("times new roman", 20, "bold")).grid(row=3, column=2, pady=10, padx=20,sticky="w")
        lblid_proof = Label(Student_frame, text="ID Proof", font=("times new roman", 20, "bold")).grid(row=4, column=2, pady=10, padx=20,sticky="w")
        lblpayment = Label(Student_frame, text="Payment Mode", font=("times new roman", 20, "bold")).grid(row=5, column=2, pady=10, padx=20,sticky="w")

        degreecombo = ttk.Combobox(Student_frame, font=("times new roman", 15, "bold"), state='readonly', width=22)
        degreecombo['value'] = ("BCA", "BBA", "MCA", "MBA", "B.Com", "M.Com")
        degreecombo.grid(row=3, column=3, pady=10, padx=10)

        idproofcombo = ttk.Combobox(Student_frame, font=("times new roman", 15, "bold"), state='readonly', width=22)
        idproofcombo['value'] = ("ID Card", "Driving License", "Passport")
        idproofcombo.grid(row=4, column=3, pady=10, padx=10)

        paymentcombo = ttk.Combobox(Student_frame, font=("times new roman", 15, "bold"), state='readonly', width=22)
        paymentcombo['value'] = ("Credit Card", "Debit Card", "Net Banking", "VISA", "MasterCard")
        paymentcombo.grid(row=5, column=3, pady=10, padx=10)

        btnframe = Frame(self.root, bd=10, relief=GROOVE)
        btnframe.place(x=10, y=570)

        btnsave = Button(btnframe, text="Save", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=0, padx=12, pady=10)
        btndelete = Button(btnframe, text="Delete", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=1, padx=12, pady=10)
        btnclear = Button(btnframe, text="Clear", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=2, padx=12, pady=10)
        btnlogout = Button(btnframe, text="Logout", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=3, padx=12, pady=10)
        btnexit = Button(btnframe, text="Exit", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=4, padx=12, pady=10)


        File_frame = Frame(self.root, bd=10, relief=GROOVE)
        File_frame.place(x=1040, y=100, width=300, height=450)

        ftitle = Label(File_frame, text="All Files", font=("times new roman", 20, "bold"), bd=5, relief=GROOVE).pack(side=TOP, fill=X)

        scroll_y = Scrollbar(File_frame, orient=VERTICAL)
        file_list = Listbox(File_frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        file_list.pack(fill=BOTH, expand=1)
        scroll_y.config(command=file_list.yview)




root=Tk()
ob=File_App(root)
root.mainloop()
