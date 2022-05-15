from tkinter import *
from backend import Database

database = Database("./books.db")


"""
  A Program that stores book information:
  Title, Author
  Year, ISBN

  User can:
  View all records
  Search an entry
  Add an entry
  Update an entry
  Delete an entry
  Close application
"""


class Frontend:

    def __init__(self, e1, e2, e3, e4, list1, database, title_text, author_text, year_text, isbn_text):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
        self.list1 = list1
        self.database = database
        self.title_text = title_text
        self.author_text = author_text
        self.year_text = year_text
        self.isbn_text = isbn_text
        self.selected_tuple = None

    def clear_input_fields(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

    def view_command(self):
        self.list1.delete(0, END)
        self.clear_input_fields()

        for row in self.database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in self.database.search(title=self.title_text.get(),
                                        author=self.author_text.get(),
                                        year=self.year_text.get(),
                                        isbn=self.isbn_text.get()):
            self.list1.insert(END, row)

    def insert_command(self):
        self.database.insert(title=self.title_text.get(),
                             author=self.author_text.get(),
                             year=self.year_text.get(),
                             isbn=self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(), self.isbn_text.get()))
        self.clear_input_fields()

    def get_selected_row(self, event):
        # global selected_tuple
        # if len(list1.curselection()) > 0:
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def delete_command(self):
        if self.selected_tuple:
            database.delete(self.selected_tuple[0])
            self.clear_input_fields()
            self.view_command()

    def update_command(self):
        if self.selected_tuple:
            database.update(self.selected_tuple[0], title_text.get(
            ), author_text.get(), year_text.get(), isbn_text.get())
            self.view_command()


window = Tk()

window.wm_title("Book store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)


l2 = Label(window, text="Author")
l2.grid(row=0, column=2)


l3 = Label(window, text="Year")
l3.grid(row=1, column=0)


l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Input boxes

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)


year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)


isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# List box to show list of data
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# configure scrollbar and listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

frontend = Frontend(e1, e2, e3, e4, list1, database,
                    title_text, author_text, year_text, isbn_text)


# Bind a function to listbox to get selected item in listbox
list1.bind("<<ListboxSelect>>", frontend.get_selected_row)


# buttons
b1 = Button(window, text="View All", width=12, command=frontend.view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12,
            command=frontend.search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12,
            command=frontend.insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=frontend.update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=frontend.delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
