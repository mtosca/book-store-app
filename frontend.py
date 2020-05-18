"""
A programs that stores this book inofrmation:
Title , Author, Year, ISBN

User can:
View all records
Search a book
Add a book
Update a book information
Delete a book
Close the aplication
"""

from tkinter import *
from book import Book

class TkinterFrontend():

    def __init__(self):
        super().__init__()

    def set_db(self, storage):
        self.storage = storage

    # function to print results
    def view_command(self):
        self.results_list.delete(0, END)
        for book in self.storage.view():
            self.results_list.insert(END, book)
        self.clear_entries()

    def seach_command(self):
        self.results_list.delete(0, END)
        book = Book(title=self.title_entry.get(), author=self.author_entry.get(), year=self.year_entry.get(), isbn=self.isbn_entry.get())
        rows = self.storage.search(book)
        for row in rows:
            self.results_list.insert(END, row)
        self.clear_entries()

    def insert_command(self):
        book = Book(title=self.title_entry.get(), author=self.author_entry.get(), year=self.year_entry.get(), isbn=self.isbn_entry.get())
        self.storage.insert(book)
        self.clear_entries()
        self.view_command()

    def update_command(self):
        book = Book(id=self.selected_book[0], title=self.title_entry.get(), author=self.author_entry.get(), year=self.year_entry.get(), isbn=self.isbn_entry.get())
        self.storage.update(book)
        self.clear_entries()
        self.view_command()

    def delete_command(self):
        book = Book().from_touple(self.selected_book)
        self.storage.delete(book)
        self.clear_entries()
        self.view_command()

    def exit_command(self):
        self.win.destroy()   

    def get_selected_row(self, event):
        self.set_selected_book()
        self.clear_entries()
        if self.selected_book:
            self.title_entry.insert(END, self.selected_book[1])
            self.author_entry.insert(END, self.selected_book[2])
            self.year_entry.insert(END, self.selected_book[3])
            self.isbn_entry.insert(END, self.selected_book[4])

    def clear_entries(self):
        self.set_selected_book()

        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.isbn_entry.delete(0, END)
    
    def set_selected_book(self):
        self.selected_book = None
        if self.results_list.size() <= 0:
            return

        curse_selection = self.results_list.curselection()
        if curse_selection == None or curse_selection.__len__() < 1:
            return

        self.selected_book = self.results_list.get(curse_selection[0])


    def start(self):
        # create main window, will use a grid layout
        self.win = Tk()
        self.win.wm_title("Book Store")

        # create the labels for each input field
        title_label = Label(self.win, text='Title')
        title_label.grid(row=0, column=0)

        author_label = Label(self.win, text='Author')
        author_label.grid(row=0, column=2)

        year_label = Label(self.win, text='Year')
        year_label.grid(row=1, column=0)

        isbn_label = Label(self.win, text='ISBN')
        isbn_label.grid(row=1, column=2)

        #create every input field
        title_input = StringVar()
        self.title_entry = Entry(self.win, textvariable=title_input)
        self.title_entry.grid(row=0, column=1)

        author_input = StringVar()
        self.author_entry = Entry(self.win, textvariable=author_input)
        self.author_entry.grid(row=0, column=3)

        year_input = StringVar()
        self.year_entry = Entry(self.win, textvariable=year_input)
        self.year_entry.grid(row=1, column=1)

        isbn_input = StringVar()
        self.isbn_entry = Entry(self.win, textvariable=isbn_input)
        self.isbn_entry.grid(row=1, column=3)

        # create a results area with a scroll bar
        scroll_bar = Scrollbar(self.win)
        scroll_bar.grid(row=2, column=5, rowspan=10)

        self.results_list = Listbox(self.win, height=12, width=55)
        self.results_list.grid(row=2, column=0, rowspan=10, columnspan=4)

        self.results_list.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.configure(command=self.results_list.yview)

        # bind select element from list event
        self.results_list.bind('<<ListboxSelect>>', self.get_selected_row)

        # create the buttons for actions
        view_button = Button(self.win, text="View all", width=12, command=self.view_command)
        view_button.grid(row=2, column=6)

        search_button = Button(self.win, text="Search book", width=12, command=self.seach_command)
        search_button.grid(row=3, column=6)

        add_button = Button(self.win, text="Add new book", width=12, command=self.insert_command)
        add_button.grid(row=4, column=6)

        update_button = Button(self.win, text="Update info", width=12, command=self.update_command)
        update_button.grid(row=5, column=6)

        delete_button = Button(self.win, text="Delete book", width=12, command=self.delete_command)
        delete_button.grid(row=6, column=6)

        exit_button = Button(self.win, text="Exit", width=12, command=self.exit_command)
        exit_button.grid(row=7, column=6)

        # keeps the program running until is closed
        self.win.mainloop()