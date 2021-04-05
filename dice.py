from tkinter import *
from random import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
import os

root=tk.ThemedTk()
root.get_themes()
root.set_theme("breeze")
root.title("   Dice Thrower")
root.iconbitmap(r'images/dice_ico.ico')
root.resizable(FALSE,FALSE)
root.geometry('400x400+600+50')

def give_number():
    a=randint(1,6)
    change_number(a)

def change_number(a1):
    if a1==1:
        numberBtn.configure(image=one_image)
        dice_btn.configure(image=dice1_photo)
    elif a1==2:
        numberBtn.configure(image=two_image)
        dice_btn.configure(image=dice2_photo)
    elif a1==3:
        numberBtn.configure(image=three_image)
        dice_btn.configure(image=dice3_photo)
    elif a1==4:
        dice_btn.configure(image=dice4_photo)
        numberBtn.configure(image=four_image)
    elif a1==5:
        dice_btn.configure(image=dice5_photo)
        numberBtn.configure(image=five_image)        
    else:
        dice_btn.configure(image=dice6_photo)
        numberBtn.configure(image=six_image)

text=Label(root,text='Click on Dice')
text.pack()

dice_image=PhotoImage(file='images/dice.png')
diceBtn=ttk.Button(root,image=dice_image, command=give_number)
diceBtn.pack()

one_image=PhotoImage(file='images/one.png')
two_image=PhotoImage(file='images/two.png')
three_image=PhotoImage(file='images/three.png')
four_image=PhotoImage(file='images/four.png')
five_image=PhotoImage(file='images/five.png')
six_image=PhotoImage(file='images/six.png')

number_image=PhotoImage(file='images/zero.png')
numberBtn=ttk.Label(root,image=number_image)
numberBtn.pack(side='left',padx=40,pady=40)

dice1_photo=PhotoImage(file='images/dice_1.png')
dice2_photo=PhotoImage(file='images/dice_2.png')
dice3_photo=PhotoImage(file='images/dice_3.png')
dice4_photo=PhotoImage(file='images/dice_4.png')
dice5_photo=PhotoImage(file='images/dice_5.png')
dice6_photo=PhotoImage(file='images/dice_6.png')

dice_photo=PhotoImage(file='images/square.png')
dice_btn=ttk.Label(root,image=dice_photo)
dice_btn.pack(side='left',padx=30,pady=40)

root.mainloop()