from tkinter import*
import tkinter.messagebox
from tkinter.filedialog import*
screen = Tk()
screen.geometry("1000x1000")
screen.title("My Address Book")
screen.config(background = 'gray16')
myAddressBook = {}
def clear_all():
    title3.delete(0, END)
    title5.delete(0, END)
    title7.delete(0, END)
    title9.delete(0, END)
    title11.delete(0, END)

def update_address():
    key = title3.get()
    if key == '':
        tkinter.messagebox.showinfo("Name Not Entered", "Please Enter Your Name")
    else:
        if key not in myAddressBook:
            address_list.insert(END, key)
        myAddressBook[key] = (title5.get(), title7.get(), title9.get(), title11.get())
        print(myAddressBook)
        clear_all()
def delete_address():
    item = address_list.curselection()
    del myAddressBook[address_list.get(item)]
    address_list.delete(item)
    tkinter.messagebox.showinfo("Successfully Deleted", "You Have Deleted This Item")
def save_item():
    file = asksaveasfile(defaultextension = ".txt")
    if file:
        print(myAddressBook, file = file)
    address_list.delete(0, END)
title1 = Label(screen, text = "My Address Book", bg = "dim gray", fg = "snow3", font = ("times", 80, "bold"))
title1.place(x = 100, y = 100)
title2 = Label(screen, text = "Name :", bg = "dim gray", fg = "snow3", font = ("times", 19, "bold"))
title2.place(x = 600, y = 300)
title3 = Entry(screen, bd = 5, bg = "dim gray", fg = "snow3", width = 20, font = ("times", 15, "bold"))
title3.place(x = 750, y = 300)
title4 = Label(screen, text = "Address :", bg = "dim gray", fg = "snow3", font = ("times", 19, "bold"))
title4.place(x = 600, y = 400)
title5 = Entry(screen, bd = 5, bg = "dim gray", fg = "snow3", width = 20, font = ("times", 15, "bold"))
title5.place(x = 750, y = 400)
title6 = Label(screen, text = "Mobile :", bg = "dim gray", fg = "snow3", font = ("times", 19, "bold"))
title6.place(x = 600, y = 500)
title7 = Entry(screen, bd = 5, bg = "dim gray", fg = "snow3", width = 20, font = ("times", 15, "bold"))
title7.place(x = 750, y = 500)
title8 = Label(screen, text = "Email :", bg = "dim gray", fg = "snow3", font = ("times", 19, "bold"))
title8.place(x = 600, y = 600)
title9 = Entry(screen, bd = 5, bg = "dim gray", fg = "snow3", width = 20, font = ("times", 15, "bold"))
title9.place(x = 750, y = 600)
title10 = Label(screen, text = "Birthday :", bg = "dim gray", fg = "snow3", font = ("times", 19, "bold"))
title10.place(x = 600, y = 700)
title11 = Entry(screen, bd = 5, bg = "dim gray", fg = "snow3", width = 20, font = ("times", 15, "bold"))
title11.place(x = 750, y = 700)
edit = Button (screen, text = "Edit", bg = "gray24", fg = "snow3", width = 10, font = ("times", 20, "bold"))
edit.place(x = 50, y = 830)
delete = Button (screen, text = "Delete", bg = "gray24", fg = "snow3", width = 10, font = ("times", 20, "bold"), command = delete_address)
delete.place(x = 300, y = 830)
open = Button (screen, text = "Open", bg = "gray24", fg = "snow3", width = 10, font = ("times", 20, "bold"))
open.place(x = 550, y = 830)
add = Button (screen, text = "Update/Add", bg = "gray24", fg = "snow3", width = 10, font = ("times", 20, "bold"), command = update_address)
add.place(x = 800, y = 830)
save = Button (screen, text = "Save", bg = "gray24", fg = "snow3", width = 40, font = ("times", 20, "bold"), command = save_item)
save.place(x = 200, y = 925)
address_list = Listbox(screen, width = 70, height = 30)
address_list.place(x = 140, y = 300)
print(myAddressBook)
screen.mainloop()
