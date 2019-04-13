from tkinter import *
import BookStoreCode

def view_command():
    display_w.delete(0,END)
    for row in BookStoreCode.view():
        display_w.insert(END,row)

def search_command():
    display_w.delete(0,END)
    for row in BookStoreCode.search(title.get(),author.get(),year.get(),isbn.get()):
        display_w.insert(END,row)

def add_command():
    BookStoreCode.insert(title.get(),author.get(),year.get(),isbn.get())
    display_w.delete(0,END)
    for row in BookStoreCode.view():
        display_w.insert(END,row)

def get_selected_row(event): #when we declare the name of this function inside bind method then "event" is made compulsory to be passed
    try:
        global selected_tuple
        index=display_w.curselection()[0] #curselection is a method which returns the index no. of cursor Selected
        #return index
        selected_tuple=display_w.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass


def delete_command():
    BookStoreCode.delete(selected_tuple[0])
    display_w.delete(0,END)
    for row in BookStoreCode.view():
        display_w.insert(END,row)

def update_command():
    BookStoreCode.update(selected_tuple[0],title.get(),author.get(),year.get(),isbn.get())

def about():
    display_w.delete(0,END)
    display_w.insert(END,'Developed by Chanchal Kumar')

window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title") #For Labels
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title=StringVar()
e1=Entry(window,textvariable=title) #For EditText
e1.grid(row=0,column=1)

author=StringVar()
e2=Entry(window,textvariable=author)
e2.grid(row=0,column=3)

year=StringVar()
e3=Entry(window,textvariable=year)
e3.grid(row=1,column=1)

isbn=StringVar()
e4=Entry(window,textvariable=isbn)
e4.grid(row=1,column=3)

display_w=Listbox(window,height=6,width=30) #displayWindow
display_w.grid(row=2,column=0,rowspan=7,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=7)

display_w.configure(yscrollcommand=sb1.set)
sb1.configure(command=display_w.yview)

display_w.bind('<<ListboxSelect>>',get_selected_row) #Used to extract data from displayWindow

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=8,column=3)

b7=Button(window,text="About",width=12,command=about)
b7.grid(row=7,column=3)

window.mainloop()
