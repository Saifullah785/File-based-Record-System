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

        #===================All variables=========================
        self.s_id = StringVar()
        self.name = StringVar()
        self.contact = StringVar()
        self.date = StringVar()
        self.course = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.degree = StringVar()
        self.id_proof = StringVar()
        self.payment = StringVar()

        lbsid = Label(Student_frame, text="Student ID", font=("times new roman", 20, "bold")).grid(row=1, column=0, pady=10, padx=20,sticky="w")
        txtsid = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7,textvariable=self.s_id, relief=GROOVE,width=22).grid(row=1, column=1, pady=10, padx=10)

        lblcontact = Label(Student_frame, text="Contact No", font=("times new roman", 20, "bold")).grid(row=1, column=2, pady=10, padx=20,sticky="w")
        txtcontact = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, textvariable=self.contact, relief=GROOVE,width=22).grid(row=1, column=3, pady=10, padx=10)

        lbname = Label(Student_frame, text="Name", font=("times new roman", 20, "bold")).grid(row=2, column=0, pady=10, padx=20,sticky="w")
        txtname = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7,textvariable=self.name, relief=GROOVE,width=22).grid(row=2, column=1, pady=10, padx=10)

        lbldate = Label(Student_frame, text="Date (dd/mm/yyyy)", font=("times new roman", 20, "bold")).grid(row=2, column=2, pady=10, padx=20,sticky="w")
        txtdate = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, textvariable=self.date, relief=GROOVE,width=22).grid(row=2, column=3, pady=10, padx=10)

        lblcourse = Label(Student_frame, text="Course", font=("times new roman", 20, "bold")).grid(row=3, column=0, pady=10, padx=20,sticky="w")
        txtcourse = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7, textvariable=self.course, relief=GROOVE,width=22).grid(row=3, column=1, pady=10, padx=10)

        lbladdress = Label(Student_frame, text="Address", font=("times new roman", 20, "bold")).grid(row=4, column=0, pady=10, padx=20,sticky="w")
        txtaddress = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7,textvariable=self.address, relief=GROOVE,width=22).grid(row=4, column=1, pady=10, padx=10)

        lblcity = Label(Student_frame, text="City", font=("times new roman", 20, "bold")).grid(row=5, column=0, pady=10, padx=20,sticky="w")
        txtcity = Entry(Student_frame, font=("times new roman", 15, "bold"), bd=7,textvariable=self.city, relief=GROOVE,width=22).grid(row=5, column=1, pady=10, padx=10)

        lblselect_degree = Label(Student_frame, text="Select Degree", font=("times new roman", 20, "bold")).grid(row=3, column=2, pady=10, padx=20,sticky="w")
        lblid_proof = Label(Student_frame, text="ID Proof", font=("times new roman", 20, "bold")).grid(row=4, column=2, pady=10, padx=20,sticky="w")
        lblpayment = Label(Student_frame, text="Payment Mode", font=("times new roman", 20, "bold")).grid(row=5, column=2, pady=10, padx=20,sticky="w")

        degreecombo = ttk.Combobox(Student_frame, font=("times new roman", 15, "bold"),textvariable=self.degree, state='readonly', width=22)
        degreecombo['value'] = ("BCA", "BBA", "MCA", "MBA", "B.Com", "M.Com")
        degreecombo.grid(row=3, column=3, pady=10, padx=10)

        idproofcombo = ttk.Combobox(Student_frame, font=("times new roman", 15, "bold"), textvariable=self.id_proof, state='readonly', width=22)
        idproofcombo['value'] = ("ID Card", "Driving License", "Passport")
        idproofcombo.grid(row=4, column=3, pady=10, padx=10)

        paymentcombo = ttk.Combobox(Student_frame, font=("times new roman", 15, "bold"), textvariable=self.payment, state='readonly', width=22)
        paymentcombo['value'] = ("Credit Card", "Debit Card", "Net Banking", "VISA", "MasterCard")
        paymentcombo.grid(row=5, column=3, pady=10, padx=10)

        btnframe = Frame(self.root, bd=10, relief=GROOVE)
        btnframe.place(x=10, y=570)

        btnsave = Button(btnframe, text="Save", width=18, font=("arial", 15, "bold"),command=self.save_data, bd=7).grid(row=0, column=0, padx=12, pady=10)
        btndelete = Button(btnframe, text="Delete", width=18,command=self.delete, font=("arial", 15, "bold"), bd=7).grid(row=0, column=1, padx=12, pady=10)
        btnclear = Button(btnframe, text="Clear", width=18,command=self.clear, font=("arial", 15, "bold"), bd=7).grid(row=0, column=2, padx=12, pady=10)    
        btnlogout = Button(btnframe, text="Logout", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=3, padx=12, pady=10)
        btnexit = Button(btnframe, text="Exit", width=18, font=("arial", 15, "bold"), bd=7).grid(row=0, column=4, padx=12, pady=10)


        File_frame = Frame(self.root, bd=10, relief=GROOVE)
        File_frame.place(x=1040, y=100, width=300, height=450)

        ftitle = Label(File_frame, text="All Files", font=("times new roman", 20, "bold"), bd=5, relief=GROOVE).pack(side=TOP, fill=X)

        scroll_y = Scrollbar(File_frame, orient=VERTICAL)
        self.file_list = Listbox(File_frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.file_list.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.bind("<ButtonRelease-1>", self.get_data)
        self.show_files()

        #===================All functions=========================
    def save_data(self):
        present="no"
        if self.s_id.get() == "":
            messagebox.showerror("Error", "Please enter Student ID")
        else:
            f=os.listdir('files/')
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Update", "File already present \n Do you want to update it?")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Success", "File updated successfully")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Success", "File saved successfully")
                    self.show_files()
            else:
                self.save_file()
                messagebox.showinfo("Success", "File saved successfully")
                self.show_files()


    def save_file(self):

        f=open('files/'+str(self.s_id.get())+'.txt','w')
        f.write(
                str(self.s_id.get()) + "," +
                str(self.name.get()) + "," +
                str(self.contact.get()) + "," +
                str(self.date.get()) + "," +
                str(self.course.get()) + "," +
                str(self.address.get()) + "," +
                str(self.city.get()) + "," +
                str(self.degree.get()) + "," +
                str(self.id_proof.get()) + "," +
                str(self.payment.get()) + "\n"
              )
        f.close()
        self.clear()
        self.show_files()
        
           

    def show_files(self):
        files=os.listdir('files/')
        self.file_list.delete(0, END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END, i)
    

    def get_data(self, ev):
        get_cursor = self.file_list.curselection()

        f1=open('files/'+self.file_list.get(get_cursor))
        values=[]
        for f in f1:
            values=f.split(",")

        self.s_id.set(values[0])
        self.name.set(values[1])
        self.contact.set(values[2])
        self.date.set(values[3])
        self.course.set(values[4])
        self.address.set(values[5])
        self.city.set(values[6])
        self.degree.set(values[7])
        self.id_proof.set(values[8])
        self.payment.set(values[9])

    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.contact.set("")
        self.date.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.degree.set("")
        self.id_proof.set("")
        self.payment.set("")

    # def delete(self):
    #     get_cursor = self.file_list.curselection()
    #     if messagebox.askyesno("Confirm", "Are you sure you want to delete this file?"):
    #         os.remove('files/'+self.file_list.get(get_cursor))
    #         messagebox.showinfo("Success", "File deleted successfully")
    #         self.show_files()
    #     else:
    #         pass
    def delete(self):
        present="no"
        if self.s_id.get() == "":
            messagebox.showerror("Error", "Please enter Student ID")
        else:
            f=os.listdir('files/')
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Confirm", "Are you sure you want to delete this file?")
                    if ask>0:
                        os.remove('files/'+self.s_id.get()+'.txt')
                        messagebox.showinfo("Success", "File deleted successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error", "File not found")



root=Tk()
ob=File_App(root)
root.mainloop()
