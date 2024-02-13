from textblob import*
from tkinter import *

def correct_spell():
    get_data=input.get()
    opt=TextBlob(get_data)
    correct=opt.correct()
    output.delete(0,END)
    output.insert(0,correct)

global input, output
win = Tk()
win.geometry("600x600")
win.title("Spelling Checker")
win.resizable(False, False)
win.configure(bg="crimson")

welcome = Label(win, text="Welcome to Spelling Corrector", font=("algerian", 25, "bold"), bg="cyan", fg="black")
welcome.place(x=10, y=50)
intext = Label(win, text="Enter Text", font=("sans-sherif", 25, "bold"), bg="grey", fg="white")
intext.place(x=150, y=100, height=50, width=300)

input = Entry(win, font=("sans-sherif", 18), )
input.place(x=150, y=175, height=40, width=300)

outtext = Label(win, text="Correct Spelling", font=("sans-sherif", 25, "bold"), bg="grey", fg="white")
outtext.place(x=150, y=250, height=50, width=300)

output = Entry(win, font=("sans-sherif", 18))
output.place(x=150, y=325, height=40, width=300)

button = Button(win, text="Click", font=("Sans-sherif", 30, "bold"), command=correct_spell)
button.place(x=230, y=400, height=40, width=120)
win.mainloop()