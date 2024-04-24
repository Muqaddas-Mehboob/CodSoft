from tkinter import*
import tkinter
from PIL import Image, ImageTk

def close():
    m.destroy()

def add_task():
    task = entryBox.get()
    if task:
        listBox.insert(END,task)
        entryBox.delete(0,END)

def delete_task():
    index = listBox.curselection()
    listBox.delete(index)

def edit_task():
    index = listBox.curselection()
    if index:
        new_task = entryBox.get()
        if new_task:
            listBox.delete(index)
            listBox.insert(index,new_task)
            entryBox.delete(0,END)


def complete_task():
    index = listBox.curselection()
    if index:
        task = listBox.get(index)
        if task.endswith("(✓)"):
            return
        listBox.delete(index)
        listBox.insert(index, f"{task} (✓)")

m = Tk()
m.title("TO-DO LIST")
m.geometry('462x580+55+13')
m.resizable(False,False)
m.overrideredirect(True)

main_image = Image.open(r"C:\Users\Muqaddas Mehboob\Downloads\\background (1).png")
new_image = ImageTk.PhotoImage(main_image)
canvas = Canvas(m,width=800,height = 4000)
canvas.place(x=0,y=0)
canvas.create_image(0,0,anchor=NW, image = new_image)

entryBox = Entry(m,font=('garet',20),fg='white', bg = '#536F5D',width=21,border=0)
entryBox.place(x=10,y=100)
entryBox.focus()

heading = Label(m,text="To Do List",fg = "#536F5D",bg = '#BACDBA',font=("times new roman",30),width=50,height=1,justify='center',anchor='center')
heading.pack(fill=BOTH)

add_button = Button(m,text='Add Task',font=('garet',14),fg='white', bg = '#536F5D',width=9,height=1,border=0,command=add_task)
add_button.place(x=340,y=100)

delete_button = Button(m,text='Delete',font=('garet',14),fg='white', bg = '#536F5D',width=9,height=1,border=0,command=delete_task)
delete_button.place(x=340,y=150)

edit_button = Button(m,text='Edit',font=('garet',14),fg='white', bg = '#536F5D',width=9,height=1,border=0,command=edit_task)
edit_button.place(x=340,y=200)

complete_button = Button(m,text='Complete',font=('garet',14),fg='white', bg = '#536F5D',width=9,height=1,border=0,command=complete_task)
complete_button.place(x=340,y=250)

close_button = Button(m,text='Close',font=('garet',14),fg='white', bg = '#536F5D',width=9,height=1,border=0,command=close)
close_button.place(x=140,y=530)

listBox = Listbox(m,font=('garet',14),fg='black',bg = '#BACDBA',width=29,height=15,activestyle=tkinter.NONE,selectbackground='#F1EFDC',selectforeground="black")
listBox.place(x=10,y=150)

m.mainloop()

