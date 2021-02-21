# Sample program about class and object

from tkinter import Tk, Label, Button, Entry


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("800x500")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.submit_button = Button(master, text="Submit", command=self.submit_data)
        self.submit_button.pack()

        self.inputbox1 = Entry(master)
        self.inputbox1.pack()

        self.clear_button = Button(master, text="Clear", command=self.clear_field)
        self.clear_button.pack()

    def clear_field(self):
        self.inputbox1.delete(0, "end")

    def greet(self):
        print("Greetings!")

    def submit_data(self):
        name = self.inputbox1.get()
        print(name)
        try:
            with open("The_data_file.txt", "a") as f:
                f.write(name)
                f.close()
        except FileNotFoundError:
            with open("file.txt", "w") as f:
                f.write(name)
                f.close()



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

