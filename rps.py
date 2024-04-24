import random
from tkinter import *
from tkinter.font import Font
from PIL import Image,ImageTk

m = Tk()
m.title("ROCK PAPER SCISSOR GAME")
m.config(background='black')
m.geometry("1010x400+100+100")
m.resizable(False,False)
m.overrideredirect(True)

def exit():
    m.destroy()


#user images
rock_user = ImageTk.PhotoImage(Image.open(r"C:\Users\Muqaddas Mehboob\Desktop\rock 2.png"))
paper_user = ImageTk.PhotoImage(Image.open(r"C:\Users\Muqaddas Mehboob\Desktop\paper 2.png"))
scissor_user = ImageTk.PhotoImage(Image.open(r"C:\Users\Muqaddas Mehboob\Desktop\\scissor 2.png"))

#computer images
rock_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\Muqaddas Mehboob\Desktop\rock 3.png"))
scissor_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\Muqaddas Mehboob\Desktop\\scissor 3.png"))
paper_comp = ImageTk.PhotoImage(Image.open(r"C:\Users\Muqaddas Mehboob\Desktop\paper 3.png"))

#insert pictures
user_label = Label(m, image= rock_user,border=0)
comp_label = Label(m, image= rock_comp,border=0)
user_label.grid(row = 1, column=0)
comp_label.grid(row = 1, column=4)

#scores
user_score = Label(m,text=0,font=('times new roman',50),bg="black",fg= "white")
comp_score = Label(m,text=0,font=('times new roman',50),bg="black",fg= "white")
comp_score.grid(row=1,column=3)
user_score.grid(row=1,column=1)

#indicators
user_indicator = Label(m, font=('times new roman',20),text= "USER",bg = "black",fg = "white").grid(row=0,column=1)
comp_indicator = Label(m, font=('times new roman',20),text= "COMPUTER",bg = "black",fg = "white").grid(row=0,column = 3)

#message
msg = Label(m,font=("times new roman",25),bg="light green",fg="gray20",text="PLAY!")
msg.grid(row=1,column=2)

#update message
def updateMessage(x):
    msg['text']=x

#update scores
def update_user_score():
    userScore = int(user_score['text'])
    userScore += 1
    user_score["text"]= str(userScore)

def update_comp_scores():
    compScore = int(comp_score['text'])
    compScore += 1
    comp_score["text"]= str(compScore)

#check winner
def check_winner(user,computer):
    if user == computer:
        updateMessage("It's a tie!")
    elif user == 'rock':
        if computer == 'paper':
            updateMessage("You loose!")
            update_comp_scores()
        else:
            updateMessage("You win!")
            update_user_score()

    elif user == 'paper':
        if computer == 'scissor':
            updateMessage("You loose!")
            update_comp_scores()
        else:
            updateMessage("You win!")
            update_user_score()
    elif user == 'scissor':
        if computer == 'rock':
            updateMessage("You loose!")
            update_comp_scores()
        else:
            updateMessage("You win!")
            update_user_score()
    else:
        pass

#update choices
comp_choice = ['rock','paper','scissor']
    
def update_choices(userChoice):
            #for computer
    choices = comp_choice[random.randint(0,2)]
    if choices == "rock":
        comp_label.configure(image=rock_comp)
    elif choices == 'paper':
        comp_label.configure(image= paper_comp)
    else:
        comp_label.configure(image= scissor_comp)
            #for user
    if userChoice == "rock":
        user_label.configure(image=rock_user)
    elif userChoice == "scissor":
        user_label.configure(image=scissor_user)
    else:
        user_label.configure(image=paper_user)

    check_winner(userChoice,choices)

#buttons
rock = Button(m, font=('times new roman',10),width=25, height=2, text="ROCK", bg = "#FF3E4D",fg= "black",command= lambda:update_choices("rock")).grid(row=2,column=1)
paper = Button(m,font=('times new roman',10),width=25, height=2, text="PAPER", bg = "#FAD02E",fg= "black",command= lambda:update_choices("paper")).grid(row=2,column=2)
scissor = Button(m,font=('times new roman',10), width=25, height=2, text="SCISSOR", bg = "#0ABDE3",fg= "black",command= lambda:update_choices("scissor")).grid(row=2,column=3)

#exit button
exit_button = Button(m, text="EXIT",bg = 'black',fg = 'white',width=20,height=2,font=('times new roman',10,'bold'),command=exit,borderwidth=4).grid(row=3,column=4)
m.mainloop()
