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
from backend import DataBase

database = DataBase()

# function to print results
def view_command():
    results_list.delete(0, END)
    for row in database.view():
        results_list.insert(END, row)

def seach_command():
    results_list.delete(0, END)
    rows = database.search(title=title_entry.get(), author=author_entry.get(), year=year_entry.get(), isbn=isbn_entry.get())
    for row in rows:
        results_list.insert(END, row)

def insert_command():
    database.insert(title=title_entry.get(), author=author_entry.get(), year=year_entry.get(), isbn=isbn_entry.get())
    results_list.delete(0, END)
    results_list.insert(END, (title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()))

def update_command():
    database.update(selected_book[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())

def delete_command():
    database.delete(selected_book[0])

def exit_command():
    win.destroy()   

def get_selected_row(event):
    if results_list.size() <= 0:
        return

    global selected_book
    selected_index = results_list.curselection()[0]
    selected_book = results_list.get(selected_index)

    title_entry.delete(0, END)
    title_entry.insert(END, selected_book[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_book[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_book[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_book[4])


# create main window, will use a grid layout
win = Tk()
win.wm_title("Book Store")

# create the labels for each input field
title_label = Label(win, text='Title')
title_label.grid(row=0, column=0)

author_label = Label(win, text='Author')
author_label.grid(row=0, column=2)

year_label = Label(win, text='Year')
year_label.grid(row=1, column=0)

isbn_label = Label(win, text='ISBN')
isbn_label.grid(row=1, column=2)

#create every input field
title_input = StringVar()
title_entry = Entry(win, textvariable=title_input)
title_entry.grid(row=0, column=1)

author_input = StringVar()
author_entry = Entry(win, textvariable=author_input)
author_entry.grid(row=0, column=3)

year_input = StringVar()
year_entry = Entry(win, textvariable=year_input)
year_entry.grid(row=1, column=1)

isbn_input = StringVar()
isbn_entry = Entry(win, textvariable=isbn_input)
isbn_entry.grid(row=1, column=3)

# create a results area with a scroll bar
scroll_bar = Scrollbar(win)
scroll_bar.grid(row=2, column=5, rowspan=10)

results_list = Listbox(win, height=12, width=50)
results_list.grid(row=2, column=0, rowspan=10, columnspan=4)

results_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=results_list.yview)

# bind select element from list event
results_list.bind('<<ListboxSelect>>', get_selected_row)

# create the buttons for actions
view_button = Button(win, text="View all", width=12, command=view_command)
view_button.grid(row=2, column=6)

search_button = Button(win, text="Search book", width=12, command=seach_command)
search_button.grid(row=3, column=6)

add_button = Button(win, text="Add new book", width=12, command=insert_command)
add_button.grid(row=4, column=6)

update_button = Button(win, text="Update info", width=12, command=update_command)
update_button.grid(row=5, column=6)

delete_button = Button(win, text="Delete book", width=12, command=delete_command)
delete_button.grid(row=6, column=6)

exit_button = Button(win, text="Exit", width=12, command=exit_command)
exit_button.grid(row=7, column=6)

# keeps the program running until is closed
win.mainloop()