# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 09:10:58 2022

@author: HP
"""

from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Heart_Diagnostic_report")
root.geometry("500x600")
root.configure(bg="red")

question1_radioButton=StringVar(value="0")
Question1=Label(root,text="do you have shortness in breath during routine activities?")
Question1.place(relx=0.5,rely=0.05,anchor=CENTER)
question1_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes")
question1_r1.place(relx=0.5,rely=0.10,anchor=CENTER)
question1_r2=Radiobutton(root,text="no",variable=question1_radioButton,value="no")
question1_r2.place(relx=0.5,rely=0.15,anchor=CENTER)

question2_radioButton=StringVar(value="0")
Question2=Label(root,text="Do you have swelling in feet/ankles/legs(shoes feel tighter)or abomen?")
Question2.place(relx=0.5,rely=0.20,anchor=CENTER)
question2_r1=Radiobutton(root,text="yes",variable=question2_radioButton,value="yes")
question2_r1.place(relx=0.5,rely=0.25,anchor=CENTER)
question2_r2=Radiobutton(root,text="no",variable=question2_radioButton,value="no")
question2_r2.place(relx=0.5,rely=0.30,anchor=CENTER)


question3_radioButton=StringVar(value="0")
Question3=Label(root,text="Do you feel any od theses symptons-confusion,diffusion,or loss of memory?")
Question3.place(relx=0.5,rely=0.35,anchor=CENTER)
question3_r1=Radiobutton(root,text="yes",variable=question3_radioButton,value="yes")
question3_r1.place(relx=0.5,rely=0.40,anchor=CENTER)
question3_r2=Radiobutton(root,text="no",variable=question3_radioButton,value="no")
question3_r2.place(relx=0.5,rely=0.45,anchor=CENTER)

question4_radioButton=StringVar(value="0")
Question4=Label(root,text="do you exprience shortness of breath while at rest/laying down?")
Question4.place(relx=0.5,rely=0.50,anchor=CENTER)
question4_r1=Radiobutton(root,text="yes",variable=question4_radioButton,value="yes")
question4_r1.place(relx=0.5,rely=0.55,anchor=CENTER)
question4_r2=Radiobutton(root,text="no",variable=question4_radioButton,value="no")
question4_r2.place(relx=0.5,rely=0.60,anchor=CENTER)

question5_radioButton=StringVar(value="0")
Question5=Label(root,text="Do you experience constant wheezing/coughing that produces white or pink tinged mucus?")
Question5.place(relx=0.5,rely=0.65,anchor=CENTER)
question5_r1=Radiobutton(root,text="yes",variable=question5_radioButton,value="yes")
question5_r1.place(relx=0.5,rely=0.75,anchor=CENTER)
question5_r2=Radiobutton(root,text="no",variable=question5_radioButton,value="no")
question5_r2.place(relx=0.5,rely=0.80,anchor=CENTER)

def symptons():
    score=0
    if question1_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+10
        print(score)  
    if question4_radioButton.get()=="yes":
              score = score+10
              print(score)
    if question5_radioButton.get()=="yes":
              score = score+10
              print(score)
    if score <= 10:
        messagebox.showinfo("Report","You Dont need to visit a doctor")
    elif score > 10 and score <=30:
        messagebox.showinfo("Report","You perhaps might want to visit a doctor")
    else:
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")

btn=Button(root,text="Advise",command=symptons)
btn.place(relx=0.5,rely=0.90,anchor=CENTER)

root.mainloop()

