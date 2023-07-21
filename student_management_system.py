from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from time import strftime


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x680+0+0')
        self.root.title("STUDENT MANAGEMENT SYSTEM USING PYTHON")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_enroll = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_state = StringVar()
        self.var_pincode = StringVar()

        # Title 
        lbl_title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 37, "bold"), fg="white",
                          bg="teal")
        lbl_title.place(x=0, y=0, width=1350, height=45)
    
        # Time Function
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=("times new roman",16,"bold"),bg="teal",fg="yellow")
        lbl.place(x=0,y=0,width=120,height=45)
        time()
     
        # Background Label
        bg_lbl = Label(self.root,bg="azure", bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=45, width=1350, height=635)

        # First image
        img = Image.open("stu3.jpg")
        img = img.resize((450, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(bg_lbl, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=450, height=130)

        # Second image
        img2 = Image.open("stu2.jpg")
        img2 = img2.resize((450, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.btn_2 = Button(bg_lbl, image=self.photoimg2, cursor="hand2")
        self.btn_2.place(x=450, y=0, width=450, height=130)

        # Third image
        img3 = Image.open("stu1.jpg")
        img3 = img3.resize((450, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.btn_3 = Button(bg_lbl, image=self.photoimg3, cursor="hand2")
        self.btn_3.place(x=900, y=0, width=450, height=130)

        # Manage Frame
        manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        manage_frame.place(x=15, y=135, width=1320, height=490)

        # left frame
        Dataleftframe = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information",
                                   font=("times new roman", 12, "bold"), fg="blue", bg="white")
        Dataleftframe.place(x=10, y=10, width=600, height=470)

        std_info = LabelFrame(Dataleftframe, bd=4, relief=RIDGE, padx=2, text="Current Course Information",
                              font=("times new roman", 12, "bold"), fg="blue", bg="white")
        std_info.place(x=0, y=0, width=590, height=115)

        
        # Labels and combobox

        # Department
        lbl_dpt = Label(std_info, text="Department : ", font=("arial", 12, "bold"), bg="white")
        lbl_dpt.grid(row=0, column=0, padx=2, sticky=W)

        combo_dpt = ttk.Combobox(std_info, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17,
                                 state="readonly")
        combo_dpt["value"] = (
            "Select Department", "Computer Science", "IT", "Mech", "ECE", "EEE", "Civil", "Biotechnology")
        combo_dpt.current(0)
        combo_dpt.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        lbl_course = Label(std_info, text=" Course : ", font=("arial", 12, "bold"), bg="white")
        lbl_course.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        combo_course = ttk.Combobox(std_info, textvariable=self.var_course, font=("times new roman", 12, "bold"),
                                    width=17, state="readonly")
        combo_course["value"] = ("Select Course", "BTech", "MTech")
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        lbl_year = Label(std_info, text=" Year : ", font=("arial", 12, "bold"), bg="white")
        lbl_year.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        combo_year = ttk.Combobox(std_info, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17,
                                  state="readonly")
        combo_year["value"] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        combo_year.current(0)
        combo_year.grid(row=1, column=1, padx=2, sticky=W)

        # Semester
        lbl_sem = Label(std_info, text=" Semester : ", font=("arial", 12, "bold"), bg="white")
        lbl_sem.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        combo_sem = ttk.Combobox(std_info, textvariable=self.var_semester, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        combo_sem["value"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        combo_sem.current(0)
        combo_sem.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # student class labelframe information
        std_class = LabelFrame(Dataleftframe, bd=4, relief=RIDGE, padx=2, text="Student Class Information",
                               font=("times new roman", 12, "bold"), fg="blue", bg="white")
        std_class.place(x=0, y=115, width=590, height=235)

        # Enrollment number
        lbl_enroll = Label(std_class, text=" Enrollment No. : ", font=("arial", 11, "bold"), bg="white")
        lbl_enroll.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        enroll_entry = ttk.Entry(std_class, textvariable=self.var_std_enroll, font=("arial", 11, "bold"), width=18)
        enroll_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_name = Label(std_class, text=" Student Name : ", font=("arial", 11, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        name_entry = ttk.Entry(std_class, textvariable=self.var_std_name, font=("arial", 11, "bold"), width=18)
        name_entry.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # Roll number
        lbl_roll = Label(std_class, text=" Roll Number : ", font=("arial", 11, "bold"), bg="white")
        lbl_roll.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        roll_entry = ttk.Entry(std_class, textvariable=self.var_roll, font=("arial", 11, "bold"), width=18)
        roll_entry.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # division
        lbl_division = Label(std_class, text=" Division : ", font=("arial", 11, "bold"), bg="white")
        lbl_division.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        combo_division = ttk.Combobox(std_class, textvariable=self.var_div, font=("arial", 11, "bold"), width=16,
                                      state="readonly")
        combo_division["value"] = ("Select Division", "A", "B", "C")
        combo_division.current(0)
        combo_division.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Gender
        lbl_gender = Label(std_class, text=" Gender : ", font=("arial", 11, "bold"), bg="white")
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        combo_gender = ttk.Combobox(std_class, textvariable=self.var_gender, font=("arial", 11, "bold"), width=16,
                                    state="readonly")
        combo_gender["value"] = ("Select Gender", "Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # DOB
        lbl_dob = Label(std_class, text=" Date Of Birth : ", font=("arial", 11, "bold"), bg="white")
        lbl_dob.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        dob_entry = ttk.Entry(std_class, textvariable=self.var_dob, font=("arial", 11, "bold"), width=18)
        dob_entry.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Email
        lbl_email = Label(std_class, text=" Email : ", font=("arial", 11, "bold"), bg="white")
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        email_entry = ttk.Entry(std_class, textvariable=self.var_email, font=("arial", 11, "bold"), width=18)
        email_entry.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # Phone Number
        lbl_phn = Label(std_class, text=" Mobile No. : ", font=("arial", 11, "bold"), bg="white")
        lbl_phn.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        phn_entry = ttk.Entry(std_class, textvariable=self.var_phone, font=("arial", 11, "bold"), width=18)
        phn_entry.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Address
        lbl_adrs = Label(std_class, text=" State : ", font=("arial", 11, "bold"), bg="white")
        lbl_adrs.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        adrs_entry = ttk.Entry(std_class, textvariable=self.var_state, font=("arial", 11, "bold"), width=18)
        adrs_entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # Pincode
        lbl_pincode = Label(std_class, text=" Pincode : ", font=("arial", 11, "bold"), bg="white")
        lbl_pincode.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        pincode_entry = ttk.Entry(std_class, textvariable=self.var_pincode, font=("arial", 11, "bold"), width=18)
        pincode_entry.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # Button Frame
        btn_frame = Frame(Dataleftframe, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=340, width=590, height=43)

        btn_Add = Button(btn_frame, text="Save", command=self.add_data, font=("arial", 11, "bold"), width=15, bg="blue",
                         fg="white")
        btn_Add.grid(row=0, column=0, padx=2, pady=4)

        btn_update = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 11, "bold"), width=15,
                            bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=2, pady=4)

        btn_delete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 11, "bold"), width=15,
                            bg="blue", fg="white")
        btn_delete.grid(row=0, column=2, padx=2, pady=4)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 11, "bold"), width=15,
                           bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=2, pady=4)

        # Right frame
        Datarightframe = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information",
                                    font=("times new roman", 12, "bold"), fg="blue", bg="white")
        Datarightframe.place(x=630, y=10, width=670, height=470)
        

        # Search frame
        Search_frame = LabelFrame(Datarightframe, bd=4, relief=RIDGE, padx=2, text="Search Student Information",
                                  font=("times new roman", 12, "bold"), fg="blue", bg="white")
        Search_frame.place(x=0, y=0, width=660, height=70)

        lbl_search = Label(Search_frame, text=" Search By : ", font=("arial", 11, "bold"), fg="white", bg="green")
        lbl_search.grid(row=0, column=0, padx=5, sticky=W)

        # Search combobox
        self.var_com_search = StringVar()
        combo_search = ttk.Combobox(Search_frame, textvariable=self.var_com_search,
                                    font=("times new roman", 12, "bold"), width=15, state="readonly")
        combo_search["value"] = ("Select Option", "Roll", "Mobile", "`Enrollment_No.`","Gender")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5, sticky=W)

        # Search entry field
        self.var_search = StringVar()
        search_entry = ttk.Entry(Search_frame, textvariable=self.var_search, font=("arial", 11, "bold"), width=15)
        search_entry.grid(row=0, column=2, padx=5)

        btn_search = Button(Search_frame, command=self.search_data, text="Search", font=("arial", 11, "bold"), width=12,
                            bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=5)

        btn_show = Button(Search_frame, command=self.fetch_data, text="ShowAll", font=("arial", 11, "bold"), width=12,
                          bg="blue", fg="white")
        btn_show.grid(row=0, column=4, padx=5)


        # ========================= Student Table and Scroll bar ========================
        
        table_frame = LabelFrame(Datarightframe, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=70, width=660, height=370)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.stu_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "year", "sem", "enroll", "name", "div", "roll", "gender", "dob", "email", "phone", "state",
            "pincode"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

        self.stu_table.heading("dep", text="Department")
        self.stu_table.heading("course", text="Course")
        self.stu_table.heading('year', text='Year')
        self.stu_table.heading('sem', text="Semester")
        self.stu_table.heading("enroll", text="Enrollment")
        self.stu_table.heading("name", text="Student Name")
        self.stu_table.heading("div", text="Division")
        self.stu_table.heading("roll", text="Roll No.")
        self.stu_table.heading("gender", text="Gender")
        self.stu_table.heading("dob", text="DOB")
        self.stu_table.heading("email", text="Email")
        self.stu_table.heading("phone", text="Mobile No.")
        self.stu_table.heading("state", text="State")
        self.stu_table.heading("pincode", text="Pincode")

        self.stu_table["show"] = "headings"

        self.stu_table.column("dep", width=100)
        self.stu_table.column("course", width=100)
        self.stu_table.column("year", width=100)
        self.stu_table.column("sem", width=100)
        self.stu_table.column("enroll", width=100)
        self.stu_table.column("name", width=100)
        self.stu_table.column("div", width=100)
        self.stu_table.column("roll", width=100)
        self.stu_table.column("gender", width=100)
        self.stu_table.column("dob", width=100)
        self.stu_table.column("email", width=100)
        self.stu_table.column("phone", width=100)
        self.stu_table.column("state", width=100)
        self.stu_table.column("pincode", width=100)

        self.stu_table.pack(fill=BOTH, expand=1)
        self.stu_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Add_data function
    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_enroll.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Bhuvana@123",
                                               database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into stu_manage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_enroll.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_state.get(),
                    self.var_pincode.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}",parent=self.root)

    # Fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Bhuvana@123",
                                       database="student")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from stu_manage")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in data:
                self.stu_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get cursor
    def get_cursor(self, event=""):
        cursor_row = self.stu_table.focus()
        content = self.stu_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_enroll.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_state.set(data[12])
        self.var_pincode.set(data[13])

    # Update
    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "" or self.var_std_enroll.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure to update this student data?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Bhuvana@123",
                                                   database="student")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update stu_manage set Dep = %s,course=%s,Year=%s,Semester=%s,Name=%s,"
                                      "Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Mobile=%s,State=%s,Pincode=%s "
                                      "where `Enrollment_No.`=%s", (
                                          self.var_dep.get(),
                                          self.var_course.get(),
                                          self.var_year.get(),
                                          self.var_semester.get(),
                                          self.var_std_name.get(),
                                          self.var_div.get(),
                                          self.var_roll.get(),
                                          self.var_gender.get(),
                                          self.var_dob.get(),
                                          self.var_email.get(),
                                          self.var_phone.get(),
                                          self.var_state.get(),
                                          self.var_pincode.get(),
                                          self.var_std_enroll.get()
                                      ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student information successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}",parent=self.root)

    # Delete function
    def delete_data(self):
        if self.var_std_enroll.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Bhuvana@123",
                                                   database="student")
                    my_cursor = conn.cursor()
                    sql = "delete from stu_manage where `Enrollment_No.`=%s"
                    value = (self.var_std_enroll.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "Student record has been deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}",parent=self.root)

    # Reset  function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_enroll.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_pincode.set("")

    # Search data
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Bhuvana@123",
                                               database="student")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from stu_manage where binary " +str(self.var_com_search.get())+" LIKE '%"+str(
                    self.var_search.get())+"%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.stu_table.delete(*self.stu_table.get_children())
                    for j in rows:
                        self.stu_table.insert("", END, values=j)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
