from tkinter import *
from db import Database
root = Tk()

db = Database('store.db')


def populate_items():
    parts_list.delete(0, END)

    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    db.add(part_text.get(), customer_text.get(),
           retailer_text.get(), price_text.get())
    clear_text()

    populate_items()


def select_item(event):
    global selected_item
    try:

        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])

        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])

        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])

        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_items()


def update_item():
    db.update(selected_item[0],
              part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    clear_text()
    populate_items()


def clear_text():
    part_entry.delete(0, END)

    customer_entry.delete(0, END)

    retailer_entry.delete(0, END)

    price_entry.delete(0, END)


root.title("Part Manager")
root.geometry('700x400')

# Text
part_text = StringVar()
part_label = Label(root, text="Part Name", font=('bold', 14))
part_label.grid(row=0, column=0, sticky=W, pady=20)
part_entry = Entry(root, textvariable=part_text, font=('bold', 12))
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(root, text="Customer Name", font=('bold', 14))
customer_label.grid(row=0, column=3, sticky=W)
customer_entry = Entry(root, textvariable=customer_text, font=('bold', 12))
customer_entry.grid(row=0, column=4)

# retailer
retailer_text = StringVar()
retailer_label = Label(root, text="Retailer", font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W, pady=20)
retailer_entry = Entry(root, textvariable=retailer_text, font=('bold', 12))
retailer_entry.grid(row=1, column=1)


price_text = StringVar()
price_label = Label(root, text="Price", font=('bold', 14))
price_label.grid(row=1, column=3, sticky=W, pady=20)
price_entry = Entry(root, textvariable=price_text, font=('bold', 12))
price_entry.grid(row=1, column=4)

# Buttons
add_btn = Button(root, text="Add Item", command=add_item)
add_btn.grid(row=2, column=0)

remove_btn = Button(root, text="Remove Item", command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(root, text="Update Item", command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(root, text="Clear Inputs", command=clear_text)
clear_btn.grid(row=2, column=3)

# Parts Lists
parts_list = Listbox(root, width=50, height=8, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=10, padx=0, pady=20)
parts_list.bind('<<ListboxSelect>>', select_item)

populate_items()
root.config()

root.mainloop()
