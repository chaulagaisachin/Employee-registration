
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import DatabaseError


class ProjectPython:
    def datain(self):
        """                ========== Data Input Function==========
                This function is used to submit the data in the database created
                Name, Course, Address, Contact and Age are added.
                """
        print('data in')
        name = self.entryname.get()
        course = self.entrycourse.get()
        address = self.entryaddress.get()
        contact = self.entrycontact.get()
        age = self.entryage.get()
        if name == '':
            messagebox.showerror('NAME ERROR', 'Given NAME is EMPTY or INVALID.')
        elif course == '':
            messagebox.showerror('COURSE ERROR', 'Given COURSE is EMPTY or INVALID.')
        elif address == '':
            messagebox.showerror('ADDRESS ERROR', 'Given ADDRESS is EMPTY or INVALID.')
        elif contact == '':
            messagebox.showerror('CONTACT ERROR', 'Given CONTACT is EMPTY or INVALID.')
        elif age == '':
            messagebox.showerror('AGE ERROR', 'Given AGE is EMPTY or INVALID.')
        else:
            try:
                values = (name, course, address, contact, age)
                query = 'insert into students(Name, Course, Address, Contact, Age) values(%s,%s,%s,%s,%s);'
                self.cur.execute(query, values)
                self.con.commit()
                self.clear()
                self.show_info()
                messagebox.showinfo('Data saved', 'The given details are saved.')
            except DatabaseError:
                messagebox.showerror('Data Error', 'Use strings/alphabets in {Name, Course, Address} '
                                                   'and numeric values in {Contact, Age}')

    def clear(self):
        """                ========== Clear the ENTRY BOX Function==========
                This function is used to clear the data in the ENTRY BOX of the registration frame.
                Name, Course, Address, Contact and Age entry boxes are cleared.
                """
        self.entryname.delete(0, END)
        self.entrycourse.delete(0, END)
        self.entryaddress.delete(0, END)
        self.entrycontact.delete(0, END)
        self.entryage.delete(0, END)

    def update(self):
        """                ========== Update the data Function==========
                This function is used to update the data of current data inside the database.
                Name, Course, Address, Contact and Age can be updated.
                """
        name = self.entryname.get()
        course = self.entrycourse.get()
        address = self.entryaddress.get()
        contact = self.entrycontact.get()
        age = self.entryage.get()
        if name == '':
            messagebox.showerror('NAME ERROR', 'Given NAME is EMPTY or INVALID.')
        elif course == '':
            messagebox.showerror('COURSE ERROR', 'Given COURSE is EMPTY or INVALID.')
        elif address == '':
            messagebox.showerror('ADDRESS ERROR', 'Given ADDRESS is EMPTY or INVALID.')
        elif contact == '':
            messagebox.showerror('CONTACT ERROR', 'Given CONTACT is EMPTY or INVALID.')
        elif age == '':
            messagebox.showerror('AGE ERROR', 'Given AGE is EMPTY or INVALID.')
        else:
            point = self.tstudents.focus()
            content = self.tstudents.item(point)
            row = content['values']
            print(row)
            try:
                id_index = row[0]
                values = (name, course, address, int(contact), int(age))
                query = f'update students set Name=%s, Course=%s, Address=%s,Contact=%s ,Age=%s where Sid={id_index};'
                self.cur.execute(query, values)
                self.con.commit()
                self.show_info()
                self.clear()
                messagebox.showinfo("Confirmation", "Updated")
            except IndexError:
                messagebox.showerror('Error', 'Please Update the data below!')
            except ValueError:
                messagebox.showerror('Error', 'Please input Numeric value in Contact and Age')
            else:
                pass
            finally:
                pass

    def ccheck(self):
        """                ========== Connection Function==========
                        This function is used to check the connection of python interpreter and MySQL database.
                        """
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password='root', database='db1')
            con = self.con
            self.cur = self.con.cursor()

            if con:
                print('!!! Connected !!!')
                messagebox.showinfo('Server connection', 'Server is connected and ready to use ! ')
        except:
            print('!!!Not connected !!!')
            messagebox.showerror('Server connection', 'No server connection')

    def pointer(self, event):
        """      Data in EntryBox Function
                        This function is used to submit input the data of the main table in the EntryBox of registration
                        frame. Name, Course, Address, Contact and Age are inputted.
                        """
        try:
            point = self.tstudents.focus()
            content = self.tstudents.item(point)
            row = content['values']
            print(row)
            self.clear()
            self.entryname.insert(0, row[1])
            self.entrycourse.insert(0, row[2])
            self.entryaddress.insert(0, row[3])
            self.entrycontact.insert(0, row[4])
            self.entryage.insert(0, row[5])
        except IndexError:
            print('Exception')

    def sortpointer(self, event):
        """    Data in EntryBox Function
                submit input the data of the sorted view table in the EntryBox of
                registration frame. Name, Course, Address, Contact and Age are inputted.
                """
        try:
            point = self.sortview.focus()
            content = self.sortview.item(point)
            row = content['values']
            print(row)
            self.clear()
            self.entryname.insert(0, row[1])
            self.entrycourse.insert(0, row[2])
            self.entryaddress.insert(0, row[3])
            self.entrycontact.insert(0, row[4])
            self.entryage.insert(0, row[5])
        except IndexError:
            print('Exception')

    def show_info(self):
        """         ========== Show data in the table Function ==========
                This function is used to show data in tabular format from database. Data shown in tables are Name,
                Course, Address, Contact and Age
                """
        query = 'select * from students;'
        self.cur.execute(query)
        rows = self.cur.fetchall()
        self.tstudents.delete(*self.tstudents.get_children())
        for row in rows:
            self.tstudents.insert('', END, values=row)

    def searchint(self, list1, searchby, searchfor):
        """         ========== Search Integer values Function ==========
                This function is used to search the values of the data which are in integer values such as
                Sid and age. This program stores "Contact" as string.
                List1: contains the data of Sid to be listed.
                Searchby: data categorised as
                Searchfor: data to be searched specifically
        """
        try:
            for j in list1:
                if int(searchfor) == j:
                    query = f' select * from students where {searchby} = {j};'
                    self.cur.execute(query)
                    rows = self.cur.fetchall()
                    self.clear()
                    self.tstudents.delete(*self.tstudents.get_children())
                    for row in rows:
                        self.tstudents.insert('', END, values=row)
                    return True
            messagebox.showinfo('No data', 'No data found as your requirement, SORRY. ')
        except ValueError:
            messagebox.showerror('Error', 'Please input Sid information <NUMERIC>')
        return True

    def searchstr(self, list1, searchby, searchfor):
        """     ========== Search String values Function ==========
                This function is used to search the values of the data which are in String form such as
                Name, Course, Address and contact This program stores "Contact" as string.
                List1: contains the data of Sid to be listed.
                Searchby: data categorised as
                Searchfor: data to be searched specifically
               """
        for j in list1:
            searchfor = searchfor.upper()
            j = j.upper()
            if str(searchfor) == str(j):
                query = f' select * from students where {searchby} = "{j}";'
                self.cur.execute(query)
                rows = self.cur.fetchall()
                self.clear()
                self.tstudents.delete(*self.tstudents.get_children())
                for row in rows:
                    self.tstudents.insert('', END, values=row)
                return True
        messagebox.showinfo('No data', 'No data found as your requirement, SORRY. ')


    def searching(self):
        """     ========== Search Function ==========
                This function is used to search and creates a list of Sid needed to be displayed.
                List1: contains the data of Sid to be listed.
                Searchby: data categorised as
                Searchfor: data to be searched specifically
        """
        searchby = self.sbox.get()
        searchfor = self.entrysearch.get()
        print(searchby, searchfor)
        if searchfor == "" or searchby == "":
            messagebox.showerror('ERROR', 'Empty Field found')
        else:
            list1 = []
            query = f' select {searchby} from students;'
            self.cur.execute(query)
            rows = self.cur.fetchall()
            for i in rows:
                items = i[0]
                list1.append(items)
        if searchby == 'Sid':
            self.searchint(list1, searchby, searchfor)
            return True
        elif searchby == 'Name':
            self.searchstr(list1, searchby, searchfor)
            return True
        elif searchby == 'Course':
            self.searchstr(list1, searchby, searchfor)
            return True
        elif searchby == 'Address':
            self.searchstr(list1, searchby, searchfor)
            return True
        elif searchby == 'Contact':
            self.searchstr(list1, searchby, searchfor)
            return True
        elif searchby == 'Age':
            self.searchint(list1, searchby, searchfor)
            return True
        else:
            return False

    def datadelete(self):
        """ ========== Function to delete Data==========
        This function is used to delete the data from the table as well as data base."""
        try:
            point = self.tstudents.focus()
            content = self.tstudents.item(point)
            row = content['values']
            print(content['values'])
            Sid = row[0]
            query = f'delete from students where Sid = {Sid};'
            self.cur.execute(query)
            self.con.commit()
            self.show_info()
            messagebox.showinfo('Confirmed', 'Data deleted successfully!')
            self.clear()
        except:
            pass

    def sortedview(self, list2):
        """ ========== Sorted View of the data function ==========
                This function is used to sort the data from database and Display."""
        self.swindow = Tk()
        self.swindow.resizable(0, 0)
        self.swindow.title('Sorted View')
        self.swindow.geometry('700x350')
        self.scrollx = Scrollbar(self.swindow, orient=HORIZONTAL)
        self.scrolly = Scrollbar(self.swindow, orient=VERTICAL)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.sortview = ttk.Treeview(self.swindow, columns=('Sid', 'Name', 'Course', 'Address', 'Contact', 'Age'),
                                xscrollcommand=self.scrollx, yscrollcommand=self.scrolly, height=15)
        self.sortview.heading('Sid', text='SID')
        self.sortview.heading('Name', text='Name')
        self.sortview.heading('Course', text='Course')
        self.sortview.heading('Address', text='Address')
        self.sortview.heading('Contact', text='Contact')
        self.sortview.heading('Age', text='Age')
        self.sortview['show'] = 'headings'
        self.sortview.column('Sid', width=90)
        self.sortview.column('Name', width=120)
        self.sortview.column('Course', width=120)
        self.sortview.column('Address', width=120)
        self.sortview.column('Contact', width=120)
        self.sortview.column('Age', width=120)
        self.scrollx.config(command=self.sortview.xview)
        self.scrolly.config(command=self.sortview.yview)
        self.sortview.pack()

        # Sorted view in the table
        slist = list2
        print(slist)
        for i in list2:
            query = f'select * from students where Sid = {i};'
            self.cur.execute(query)
            rows = self.cur.fetchall()
            for row in rows:
                self.sortview.insert('', END, values=row)
        self.sortview.bind('<ButtonRelease-1>', self.sortpointer)
        self.swindow.mainloop()

    def alistout(self):
        """ ========== Sorting function ==========
            This function is used to sort the data from database in ascending format to display. """
        query = 'select Sid from students;'
        self.cur.execute(query)
        row = self.cur.fetchall()
        for i in row:
            item = i[0]
            self.list2.append(item)
        for i in range(len(self.list2) - 1, 0, -1):
            for j in range(i):
                if self.list2[j] > self.list2[j + 1]:
                    temp = self.list2[j]
                    self.list2[j] = self.list2[j + 1]
                    self.list2[j + 1] = temp
        return self.list2

    def dlistout(self):
        """ ========== Sorting function ==========
            This function is used to sort the data from database in descending format to display. """
        query = 'select Sid from students;'
        self.cur.execute(query)
        row = self.cur.fetchall()
        for i in row:
            item = i[0]
            self.list2.append(item)
        for i in range(len(self.list2) - 1, 0, -1):
            for j in range(i):
                if self.list2[j] < self.list2[j + 1]:
                    temp = self.list2[j]
                    self.list2[j] = self.list2[j + 1]
                    self.list2[j + 1] = temp
        return self.list2

    def sorted(self):
        """ ========== Sort Collab function ==========
             This function is used to sort the data from database and display. """
        self.list2 = []
        sortas = self.sortas.get()
        print(sortas)
        if sortas == 'Ascending SID':
            self.alistout()
            print(self.list2)
            self.sortedview(self.list2)
        elif sortas == 'Descending SID':
            self.dlistout()
            print(self.list2)
            self.sortedview(self.list2)
        else:
            messagebox.showinfo('Info', 'Select sorting method')

    def __init__(self, windows):
        """ ============ The main interface of the application==========="""
        # main interface
        self.windows = windows
        windows.title('Students Data')
        windows.geometry('800x750')
        windows.resizable(0, 0)
        self.ccheck()
        # Frames
        self.frame1 = Frame(windows, bd=3, bg='#99ccff', relief=RIDGE)
        self.frame2 = Frame(windows, bd=3, bg='gray', relief=RIDGE)
        self.frame3 = Frame(windows, bd=3, bg='#99ff99', relief=RIDGE)
        self.frame1.place(x=25, y=10, width=400, height=200)
        self.frame2.place(x=25, y=225, width=750, height=500)
        self.frame3.place(x=450, y=10, width=325, height=200)
        # Frame1
        Label(self.frame1, text='Registration', bg='#99ccff', font='Arial 12 bold').place(x=175, y=5)
        Label(self.frame1, text='Full Name: ', bg='#99ccff').place(x=25, y=35)
        Label(self.frame1, text='Course: ', bg='#99ccff').place(x=25, y=60)
        Label(self.frame1, text='Address: ', bg='#99ccff').place(x=25, y=85)
        Label(self.frame1, text='Contact: ', bg='#99ccff').place(x=25, y=110)
        Label(self.frame1, text='Age: ', bg='#99ccff').place(x=25, y=135)

        self.entryname = Entry(self.frame1, width=23)
        self.entrycourse = ttk.Combobox(self.frame1, values=['Ethical Hacking', 'Computing'], state='readonly')
        self.entryaddress = Entry(self.frame1, width=23)
        self.entrycontact = Entry(self.frame1, width=23)
        self.entryage = Entry(self.frame1, width=23)

        self.entryname.place(x=100, y=35)
        self.entrycourse.place(x=100, y=60)
        self.entryaddress.place(x=100, y=85)
        self.entrycontact.place(x=100, y=110)
        self.entryage.place(x=100, y=135)

        self.buttoncheck = ttk.Button(self.frame1, text='Check Connection', command=self.ccheck)
        self.buttonsubmit = ttk.Button(self.frame1, text='SUBMIT', command=self.datain)
        self.buttonclear = ttk.Button(self.frame1, text='CLEAR', command=self.clear)
        self.buttonupdate = ttk.Button(self.frame1, text='UPDATE', command=self.update)
        self.buttondelete = ttk.Button(self.frame1, text='DELETE', command=self.datadelete)
        self.buttonexit = ttk.Button(self.frame1, text='EXIT', command=windows.destroy)

        self.buttoncheck.place(x=30, y=165)
        self.buttonsubmit.place(x=300, y=25)
        self.buttonclear.place(x=300, y=55)
        self.buttonupdate.place(x=300, y=85)
        self.buttondelete.place(x=300, y=115)
        self.buttonexit.place(x=300, y=145)

        # Frame2
        self.scrollx = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.scrolly = Scrollbar(self.frame2, orient=VERTICAL)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrolly.pack(side=RIGHT, fill=Y)

        self.tstudents = ttk.Treeview(self.frame2, columns=('Sid', 'Name', 'Course', 'Address', 'Contact', 'Age'),
                                      xscrollcommand=self.scrollx, yscrollcommand=self.scrolly, height=23)

        self.tstudents.heading('Sid', text='SID')
        self.tstudents.heading('Name', text='Name')
        self.tstudents.heading('Course', text='Course')
        self.tstudents.heading('Address', text='Address')
        self.tstudents.heading('Contact', text='Contact')
        self.tstudents.heading('Age', text='Age')
        self.tstudents['show'] = 'headings'
        self.tstudents.column('Sid', width=120)
        self.tstudents.column('Name', width=120)
        self.tstudents.column('Course', width=120)
        self.tstudents.column('Address', width=120)
        self.tstudents.column('Contact', width=120)
        self.tstudents.column('Age', width=120)

        self.scrollx.config(command=self.tstudents.xview)
        self.scrolly.config(command=self.tstudents.yview)

        self.tstudents.pack()
        self.show_info()
        self.tstudents.bind('<ButtonRelease-1>', self.pointer)

        # Frame 3
        Label(self.frame3, text='Searching Data', bg='#99ff99', font='Arial 12 bold').place(x=100, y=5)
        Label(self.frame3, text='Search by: ', bg='#99ff99').place(x=15, y=30)
        Label(self.frame3, text='Search: ', bg='#99ff99').place(x=15, y=60)
        self.sbox = ttk.Combobox(self.frame3, values=['Sid', 'Name', 'Course', 'Address', 'Contact', 'Age'],
                                 state='readonly')
        self.sbox.place(x=75, y=30)
        self.entrysearch = Entry(self.frame3, width=23)
        self.entrysearch.place(x=75, y=60)
        ttk.Button(self.frame3, text='Search Data', command=self.searching).place(x=225, y=30)
        Label(self.frame3, text='Sorting Data', bg='#99ff99', font='Arial 12 bold').place(x=100, y=90)
        Label(self.frame3, text='Sort as: ', bg='#99ff99').place(x=15, y=120)
        self.sortas = ttk.Combobox(self.frame3, values=['Ascending SID', 'Descending SID'], state='readonly')
        self.sortas.place(x=75, y=120)
        self.buttonsort = ttk.Button(self.frame3, text='SORT', command=self.sorted)
        self.buttonsort.place(x=150, y=150)

        ttk.Button(self.frame3, text='Show all', command=self.show_info).place(x=225, y=60)

        messagebox.showwarning('Check Connection', 'Check the database connection before saving data !!!')

    def t_search(self):
        print(self.searching())


root = Tk()
gui = ProjectPython(root)
root.mainloop()