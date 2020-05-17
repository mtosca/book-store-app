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

class TkinterFrontend():

    def __init__(self, database):
        self.database = database

    # function to print results
    def view_command(self):
        self.results_list.delete(0, END)
        for row in self.database.view():
            self.results_list.insert(END, row)

    def seach_command(self):
        self.results_list.delete(0, END)
        rows = self.database.search(title=self.title_entry.get(), author=self.author_entry.get(), year=self.year_entry.get(), isbn=self.isbn_entry.get())
        for row in rows:
            self.results_list.insert(END, row)

    def insert_command(self):
        self.database.insert(title=self.title_entry.get(), author=self.author_entry.get(), year=self.year_entry.get(), isbn=self.isbn_entry.get())
        self.results_list.delete(0, END)
        self.results_list.insert(END, (self.title_entry.get(), self.author_entry.get(), self.year_entry.get(), self.isbn_entry.get()))

    def update_command(self):
        self.database.update(self.selected_book[0], self.title_entry.get(), self.author_entry.get(), self.year_entry.get(), self.isbn_entry.get())

    def delete_command(self):
        self.database.delete(self.selected_book[0])

    def exit_command(self):
        self.win.destroy()   

    def get_selected_row(self, event):
        if self.results_list.size() <= 0:
            return

        selected_index = self.results_list.curselection()[0]
        self.selected_book = self.results_list.get(selected_index)

        self.title_entry.delete(0, END)
        self.title_entry.insert(END, self.selected_book[1])
        self.author_entry.delete(0, END)
        self.author_entry.insert(END, self.selected_book[2])
        self.year_entry.delete(0, END)
        self.year_entry.insert(END, self.selected_book[3])
        self.isbn_entry.delete(0, END)
        self.isbn_entry.insert(END, self.selected_book[4])


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

        self.results_list = Listbox(self.win, height=12, width=50)
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