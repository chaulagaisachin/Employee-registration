# Importing Different modules

import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import DatabaseError


class EmpSys:
    def check_connection(self):
        """This function is used to check the connection between python and MySQL database"""
        try:
            self.connection = mysql.connector.connect(host="localhost", user='root', password='root', database='edb')
            connection = self.connection
            self.cursor = self.connection.cursor()

            if connection:
                print('!!! Connected !!!')
                messagebox.showinfo('Server connection', 'Connected and ready to use ! ')
        except:
            print('!!!Not connected !!!')
            messagebox.showerror('Server connection', 'No server connection')

    def data_in(self):
        ''' Data input to database'''
        name = self.emp_name.get()
        depart = self.emp_depart.get()
        address = self.emp_address.get()
        contact = self.emp_contact.get()
        age = self.emp_age.get()
        if name == '':
            messagebox.showerror('NAME ERROR', 'NAME is EMPTY/INVALID.')
        elif depart == '':
            messagebox.showerror('DEPARTMENT ERROR', 'DEPARTMENT is EMPTY/INVALID.')
        elif address == '':
            messagebox.showerror('ADDRESS ERROR', 'ADDRESS is EMPTY/INVALID.')
        elif contact == '':
            messagebox.showerror('CONTACT ERROR', 'CONTACT is EMPTY/INVALID.')
        elif age == '':
            messagebox.showerror('AGE ERROR', 'AGE is EMPTY/INVALID.')
        elif int(age) <= 16:
            messagebox.showerror('AGE ERROR', 'AGE is EMPTY/INVALID.')
        else:
            try:
                values = (name, depart, address, contact, age)
                query = 'insert into employee_data(Emp_Name, Department, Address, Contact, Age) values(%s,%s,%s,%s,%s);'
                self.cursor.execute(query, values)
                self.connection.commit()
                self.clear_field()
                self.show_tab()
                messagebox.showinfo('Data saved', 'The given details are saved.')
            except DatabaseError:
                messagebox.showerror('Data Error', 'Use strings/alphabets in {Name, Department, Address} '
                                                   'and numeric values in {Contact, Age}')

    def data_update(self):
        ''' Data update to database '''
        name = self.emp_name.get()
        depart = self.emp_depart.get()
        address = self.emp_address.get()
        contact = self.emp_contact.get()
        age = self.emp_age.get()
        if name == '':
            messagebox.showerror('NAME ERROR', 'NAME is EMPTY or INVALID.')
        elif depart == '':
            messagebox.showerror('Department ERROR', 'Department is EMPTY or INVALID.')
        elif address == '':
            messagebox.showerror('ADDRESS ERROR', 'ADDRESS is EMPTY or INVALID.')
        elif contact == '':
            messagebox.showerror('CONTACT ERROR', 'CONTACT is EMPTY or INVALID.')
        elif age == '':
            messagebox.showerror('AGE ERROR', 'AGE is EMPTY or INVALID.')
        elif int(age) <= 16:
            messagebox.showerror('AGE ERROR', 'AGE is INVALID.')
        else:
            point = self.emp_tab.focus()
            content = self.emp_tab.item(point)
            row = content['values']
            print(row)
            try:
                id_index = row[0]
                values = (name, depart, address, int(contact), int(age))
                query = f'update employee_data set Emp_Name=%s, Department=%s, Address=%s,Contact=%s ,Age=%s ' \
                        f'where Emp_ID={id_index};'
                self.cursor.execute(query, values)
                self.connection.commit()
                self.show_tab()
                self.clear_field()
                messagebox.showinfo("Confirmation", "Updated")
            except IndexError:
                messagebox.showerror('Error', 'Please Update the data below!')
            except ValueError:
                messagebox.showerror('Error', 'Please input Numeric value in Contact and Age')
            else:
                pass
            finally:
                pass

    def data_delete(self):
        '''Data delete from database'''
        try:
            point = self.emp_tab.focus()
            content = self.emp_tab.item(point)
            row = content['values']
            print(content['values'])
            EID = row[0]
            query = f'delete from employee_data where Emp_ID = {EID};'
            self.cursor.execute(query)
            self.connection.commit()
            self.show_tab()
            messagebox.showinfo('Confirmed', 'Data deleted successfully!')
            self.clear_field()
        except:
            pass

    def clear_field(self):
        '''Clear input field '''
        self.emp_name.delete(0, END)
        self.emp_depart.delete(0, END)
        self.emp_address.delete(0, END)
        self.emp_contact.delete(0, END)
        self.emp_age.delete(0, END)

    def show_tab(self):
        ''' showing the table of data'''
        query = 'select * from employee_data;'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.emp_tab.delete(*self.emp_tab.get_children())
        for row in rows:
            self.emp_tab.insert('', END, values=row)

    def point_data(self, event):
        ''' Inserting value in field after clicking on data '''
        try:
            point = self.emp_tab.focus()
            content = self.emp_tab.item(point)
            row = content['values']
            print(row)
            self.clear_field()
            self.emp_name.insert(0, row[1])
            self.emp_depart.insert(0, row[2])
            self.emp_address.insert(0, row[3])
            self.emp_contact.insert(0, row[4])
            self.emp_age.insert(0, row[5])
        except IndexError:
            print('Exception')

    def sort_point(self, event):
        ''' Showing value on sort table'''
        try:
            point = self.sortview.focus()
            content = self.sortview.item(point)
            row = content['values']
            print(row)
            self.clear_field()
            self.emp_name.insert(0, row[1])
            self.emp_depart.insert(0, row[2])
            self.emp_address.insert(0, row[3])
            self.emp_contact.insert(0, row[4])
            self.emp_age.insert(0, row[5])
        except IndexError:
            print('Exception')

    def sorted_view(self, list2):
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
        self.sortview = ttk.Treeview(self.swindow, columns=('Emp_ID', 'Name', 'Department',
                                                            'Address', 'Contact', 'Age'), xscrollcommand=self.scrollx,
                                     yscrollcommand=self.scrolly, height=15)
        self.sortview.heading('Emp_ID', text='Emp_ID')
        self.sortview.heading('Name', text='Name')
        self.sortview.heading('Department', text='Department')
        self.sortview.heading('Address', text='Address')
        self.sortview.heading('Contact', text='Contact')
        self.sortview.heading('Age', text='Age')
        self.sortview['show'] = 'headings'
        self.sortview.column('Emp_ID', width=90)
        self.sortview.column('Name', width=120)
        self.sortview.column('Department', width=120)
        self.sortview.column('Address', width=120)
        self.sortview.column('Contact', width=120)
        self.sortview.column('Age', width=120)
        self.scrollx.config(command=self.sortview.xview)
        self.scrolly.config(command=self.sortview.yview)
        self.sortview.pack()

        slist = list2
        print(slist)
        for i in list2:
            query = f'select * from employee_data where Emp_ID = {i};'
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for row in rows:
                self.sortview.insert('', END, values=row)
        self.sortview.bind('<ButtonRelease-1>', self.sort_point)
        self.swindow.mainloop()

    def ascend_list(self):
        '''makeing ascending list for sorting'''

        query = 'select Emp_ID from employee_data;'
        self.cursor.execute(query)
        row = self.cursor.fetchall()
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

    def descend_list(self):
        ''' Making Decending list for sorting '''
        query = 'select Emp_ID from employee_data;'
        self.cursor.execute(query)
        row = self.cursor.fetchall()
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

    def sorted_data(self):
        ''' sorting data'''
        self.list2 = []
        sort_as = self.sort_as.get()
        print(sort_as)
        if sort_as == 'Ascending Emp_ID':
            self.ascend_list()
            print(self.list2)
            self.sorted_view(self.list2)
        elif sort_as == 'Descending Emp_ID':
            self.descend_list()
            print(self.list2)
            self.sorted_view(self.list2)
        else:
            messagebox.showinfo('Info', 'Select sorting method')

    def int_search(self, list1, search_by, search_for):
        ''' searching integer'''
        try:
            for j in list1:
                if int(search_for) == j:
                    query = f' select * from employee_data where {search_by} = {j};'
                    self.cursor.execute(query)
                    rows = self.cursor.fetchall()
                    self.clear_field()
                    self.emp_tab.delete(*self.emp_tab.get_children())
                    for row in rows:
                        self.emp_tab.insert('', END, values=row)
                    return True
            messagebox.showinfo('No data', 'No data found as your requirement, SORRY. ')
        except ValueError:
            messagebox.showerror('Error', 'Please input Emp_ID information <NUMERIC>')
        return True

    def string_search(self, list1, search_by, search_for):
        ''' searching string'''
        for j in list1:
            search_for = search_for.upper()
            j = j.upper()
            if str(search_for) == str(j):
                query = f' select * from employee_data where {search_by} = "{j}";'
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                self.clear_field()
                self.emp_tab.delete(*self.emp_tab.get_children())
                for row in rows:
                    self.emp_tab.insert('', END, values=row)
                return True
        messagebox.showinfo('No data', 'No data found as your requirement, SORRY. ')


    def data_searching(self):
        ''' searching in database'''
        search_by = self.search_box.get()
        search_for = self.entry_search.get()
        print(search_by, search_for)
        if search_for == "" or search_by == "":
            messagebox.showerror('ERROR', 'Empty Field found')
        else:
            list1 = []
            query = f' select {search_by} from employee_data;'
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for i in rows:
                items = i[0]
                list1.append(items)
        if search_by == 'Emp_ID':
            self.int_search(list1, search_by, search_for)
            return True
        elif search_by == 'Emp_Name':
            self.string_search(list1, search_by, search_for)
            return True
        elif search_by == 'Department':
            self.string_search(list1, search_by, search_for)
            return True
        elif search_by == 'Address':
            self.string_search(list1, search_by, search_for)
            return True
        elif search_by == 'Contact':
            self.string_search(list1, search_by, search_for)
            return True
        elif search_by == 'Age':
            self.int_search(list1, search_by, search_for)
            return True
        else:
            return False

    def __init__(self, window):
        ''' Creating interface'''
        # main interface
        self.windows = window
        window.title('Employee Registration System')
        window.geometry('900x800')
        window.resizable(0, 0)
        self.check_connection()
        # Frames in windows
        # Frames
        self.frame1 = Frame(window, bd=3, bg='#99ccff', relief=RIDGE)
        self.frame2 = Frame(window, bd=3, bg='gray', relief=RIDGE)
        self.frame3 = Frame(window, bd=3, bg='#99ff99', relief=RIDGE)
        self.frame1.place(x=25, y=10, width=400, height=200)
        self.frame2.place(x=25, y=225, width=750, height=500)
        self.frame3.place(x=450, y=10, width=325, height=200)
        # Frame1
        Label(self.frame1, text='Registration Form', bg='#99ccff', font='Arial 12 bold').place(x=175, y=5)
        Label(self.frame1, text='Department: ', bg='#99ccff').place(x=25, y=35)
        Label(self.frame1, text='Full Name: ', bg='#99ccff').place(x=25, y=60)
        Label(self.frame1, text='Address: ', bg='#99ccff').place(x=25, y=85)
        Label(self.frame1, text='Contact: ', bg='#99ccff').place(x=25, y=110)
        Label(self.frame1, text='Age: ', bg='#99ccff').place(x=25, y=135)

        self.emp_name = Entry(self.frame1, width=23)
        self.emp_depart = ttk.Combobox(self.frame1, values=['Management', 'IT', 'Administration'], state='readonly')
        self.emp_address = Entry(self.frame1, width=23)
        self.emp_contact = Entry(self.frame1, width=23)
        self.emp_age = Entry(self.frame1, width=23)

        self.emp_depart.place(x=100, y=35)
        self.emp_name.place(x=100, y=60)
        self.emp_address.place(x=100, y=85)
        self.emp_contact.place(x=100, y=110)
        self.emp_age.place(x=100, y=135)

        self.check_button = ttk.Button(self.frame1, text='Check Connection', command=self.check_connection)
        self.submit_button = ttk.Button(self.frame1, text='SUBMIT', command=self.data_in)
        self.clear_button = ttk.Button(self.frame1, text='CLEAR', command=self.clear_field)
        self.update_button = ttk.Button(self.frame1, text='UPDATE', command=self.data_update)
        self.delete_button = ttk.Button(self.frame1, text='DELETE', command=self.data_delete)
        self.exit_button = ttk.Button(self.frame1, text='EXIT', command=window.destroy)

        self.check_button.place(x=30, y=165)
        self.submit_button.place(x=300, y=25)
        self.clear_button.place(x=300, y=55)
        self.update_button.place(x=300, y=85)
        self.delete_button.place(x=300, y=115)
        self.exit_button.place(x=300, y=145)

        # Frame 2

        self.x_scroll = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.y_scroll = Scrollbar(self.frame2, orient=VERTICAL)
        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)

        self.emp_tab = ttk.Treeview(self.frame2, columns=('Emp_ID', 'Name', 'Department', 'Address', 'Contact', 'Age'),
                                      xscrollcommand=self.x_scroll, yscrollcommand=self.y_scroll, height=23)

        self.emp_tab.heading('Emp_ID', text='Emp_ID')
        self.emp_tab.heading('Name', text='Name')
        self.emp_tab.heading('Department', text='Department')
        self.emp_tab.heading('Address', text='Address')
        self.emp_tab.heading('Contact', text='Contact')
        self.emp_tab.heading('Age', text='Age')
        self.emp_tab['show'] = 'headings'
        self.emp_tab.column('Emp_ID', width=120)
        self.emp_tab.column('Name', width=120)
        self.emp_tab.column('Department', width=120)
        self.emp_tab.column('Address', width=120)
        self.emp_tab.column('Contact', width=120)
        self.emp_tab.column('Age', width=120)

        self.x_scroll.config(command=self.emp_tab.xview)
        self.y_scroll.config(command=self.emp_tab.yview)

        self.emp_tab.pack()
        self.show_tab()
        self.emp_tab.bind('<ButtonRelease-1>', self.point_data)

        # Frame 3
        Label(self.frame3, text='Searching Data', bg='#99ff99', font='Arial 12 bold').place(x=100, y=5)
        Label(self.frame3, text='Search by: ', bg='#99ff99').place(x=15, y=30)
        Label(self.frame3, text='Search: ', bg='#99ff99').place(x=15, y=60)
        self.search_box = ttk.Combobox(self.frame3, values=['Emp_ID', 'Emp_Name', 'Department', 'Address',
                                                            'Contact', 'Age'], state='readonly')
        self.search_box.place(x=75, y=30)
        self.entry_search = Entry(self.frame3, width=23)
        self.entry_search.place(x=75, y=60)
        ttk.Button(self.frame3, text='Search Data', command=self.data_searching).place(x=225, y=30)
        Label(self.frame3, text='Sorting Data', bg='#99ff99', font='Arial 12 bold').place(x=100, y=90)
        Label(self.frame3, text='Sort as: ', bg='#99ff99').place(x=15, y=120)
        self.sort_as = ttk.Combobox(self.frame3, values=['Ascending Emp_ID', 'Descending Emp_ID'], state='readonly')
        self.sort_as.place(x=75, y=120)
        self.buttonsort = ttk.Button(self.frame3, text='SORT', command=self.sorted_data)
        self.buttonsort.place(x=150, y=150)

        ttk.Button(self.frame3, text='Show all', command=self.show_tab).place(x=225, y=60)

        messagebox.showwarning('Check Connection', 'Check the database connection before saving data !!!')

    def t_search(self):
        print(self.data_searching())


main_window = Tk()
gui = EmpSys(main_window)
main_window.mainloop()
