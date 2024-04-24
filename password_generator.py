import tkinter
from tkinter import *
import customtkinter as ct
import string
import random


def check_strength(password):
    length = len(password)
    if length < 10:
        return "Strength: Weak"
    elif length < 20:
        return "Strength: Medium"
    else:
        return "Strength: Strong"

def sliding(value):
    slider_label.configure(text = int(value))

def generate_password():
    length = slider.get()
    use_uppercase = switch1_var.get()
    use_lowercase = switch2_var.get()
    use_symbols = switch3_var.get()
    use_numbers = switch4_var.get()
    
    chars = ""
    if use_symbols:
        chars += string.punctuation
    if use_numbers:
        chars += string.digits
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase

    password = ''.join(random.choice(chars) for _ in range(int(length)))
    
    # Clear previous text and insert new password
    entry.delete(0, 'end')
    entry.insert(0, password)

    strength1 = check_strength(password)
    strength.delete(0,END)
    strength.insert(0,strength1)


m = Tk()
m.config(bg="#209CFF")
m.title("PASSWORD GENERATOR")
m.geometry("500x600+400+50")
m.resizable(False,False)

frame = Frame(m,width=400, height=500,bg='#0A0E31')
frame.place(relx=0.5,rely=0.5,anchor = CENTER)

heading = Label(frame,text="Password Generator",font=("Georgia",25),fg='white', bg='#0A0E31')
heading.place(x=10,y=10)

entry = ct.CTkEntry(master=frame,placeholder_text="Click Generate",width=370,height=50,
                    border_width=2,corner_radius=10,placeholder_text_color='white',font=("helvetica",20),justify= ct.CENTER)
entry.configure(fg_color='#4F4F6A')
entry.place(x=12,y=70)

slider_heading = ct.CTkLabel(master=frame, text = "Password length:",font=("Georgia",11))
slider_heading.place(x=12,y=130)

slider = ct.CTkSlider(master=frame, from_=0, to=50,orientation='horizontal',width=370,height=20,command = sliding)
slider.configure(fg_color = "#4F4F6A",button_color = "#909090",)
slider.place(x=10,y=160)
slider.set(0)

slider_label = ct.CTkLabel(master=frame,text =str(slider.get()),font = ("helvetica",12))
slider_label.place(x=115,y=130)

setting = ct.CTkLabel(master=frame, text = "Settings:",font=("Georgia",11))
setting.place(x=12,y=200)

switch1_var = tkinter.BooleanVar()
switch2_var = tkinter.BooleanVar()
switch3_var = tkinter.BooleanVar()
switch4_var = tkinter.BooleanVar()


switch1 = ct.CTkCheckBox(master=frame,text='Include Uppercase',fg_color="#764BA2",hover_color='white',border_color='#5D68E2'
                         ,variable=switch1_var)
switch2 = ct.CTkCheckBox(master=frame,text='Include Lowercase',fg_color="#764BA2",hover_color='white',border_color='#5D68E2'
                         ,variable=switch2_var)
switch3 = ct.CTkCheckBox(master=frame,text='Include Symbols',fg_color="#764BA2",hover_color='white',border_color='#5D68E2',
                        variable = switch3_var)
switch4 = ct.CTkCheckBox(master=frame,text='Include Numbers',fg_color="#764BA2",hover_color='white',border_color='#5D68E2',
                        variable = switch4_var)
switch1.place(x = 12,y = 210)
switch2.place(x = 12,y = 250)
switch3.place(x = 12,y = 290)
switch4.place(x = 12,y = 330)

generate_button = ct.CTkButton(master = frame, text="Generate Password",font=("Georgia",15),fg_color="#5D68E2",command=generate_password,
                               width = 300,height = 30,corner_radius=15,hover_color='#667EEA',)
generate_button.place(x = 50,y=400)

strength = ct.CTkEntry(master=frame,placeholder_text="Strength: ",font=("Georgia",15),fg_color="#5D68E2",placeholder_text_color='white',
                       width = 300,height = 30,corner_radius=15)
strength.place(x=50,y=450)
m.mainloop()
