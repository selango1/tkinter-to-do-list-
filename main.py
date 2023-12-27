#!/usr/bin/env python
# coding: utf-8



#import packages
import tkinter
from tkinter import *
#import tkinter.messagebox

import datetime as dt

window= Tk()




#giving a title
window.title("To-do-list")
window.geometry("400x600+800+70")
window.resizable(False,False)


# In[ ]:


#frame widget to hold the listbox and scrollin

task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)
        update_file()
            

def deleteTask():
    global task_list
    marked = listbox.curselection()
    if marked:
        temp = marked[0]
        task = str(listbox.get(ANCHOR))

        if task in task_list:
            task_list.remove(task)

            with open("tasklist.txt",'w') as taskfile:
                for t  in task_list:
                    taskfile.write(t + "\n")
            listbox.delete(temp)


            


def markCompleted():
    marked=listbox.curselection()
    if marked:
        temp=marked[0]
        task = str(listbox.get(ANCHOR))
        if task in task_list:
            listbox.itemconfig(temp,{'fg':'green'})

           

def update_file():
    with open("tasklist.txt",'w') as taskfile:
        for task in task_list:
            taskfile.write(task + "\n")
            

            
            
        


            
def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
#icon
image_icon = PhotoImage(file="image/icon2.png")
window.iconphoto(False, image_icon)


#top_bar
top_image = PhotoImage(file="image/topbar.png")
Label(window, image=top_image).pack()

#dock image
dockImage = PhotoImage(file="image/dock3.png")
Label(window, image=dockImage,bg="#f7be11").place(x=30,y=40)

#note image
noteImage = PhotoImage(file="image/icon2.png")
Label(window,image=noteImage,bg="#f7be11").place(x=340,y=40)


#heading
heading = Label(window,text="ALL TASKS",font="arial 20 bold",fg="black",bg="#f7be11")
heading.place(x=130,y=20)

#adding date
date=dt.datetime.now()
label=Label(window, text=f"{date:%A,%B %d,%Y}", font="ariel 9",fg="black",bg="#f7be11")
label.place(x=130,y=50)


#main
frame = Frame(window, width =200,height=30,bg="white")
frame.place(x=100,y=170)

task=StringVar()
task_entry=Entry(frame,width=28,font="ariel 10",bd=0)
task_entry.place(x=0,y=10)
#add button
button = Button(window,text="ADD",font="arial 10 bold",width=4,bg="#276be6",fg="#fff",bd=0,command=addTask)
button.place(x=100,y=210)
#complete button

markButton=Button(window,text="COMPLETED",font="ariel 10 bold",width=10,bg="green",fg="#fff",bd=0,command=markCompleted)
markButton.place(x=145,y=210)

#delete button
deleteButton=Button(window,text="DELETE",font="ariel 10 bold",width=6,bg="red",fg="#fff",bd=0,command=deleteTask)
deleteButton.place(x=240,y=210)
#listbox
frame1 = Frame(window, bd=3, width =700, height=280, bg="#f7be11")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('ariel',12),width=40,height=16,bg="#f7be11",fg="black",cursor="hand2",selectbackground="#276be6")
listbox.pack(side=LEFT,fill=BOTH, padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()

#check tasklist




#delete
#deleteImage=PhotoImage(file="image/trash2_48.png")
#Button(window, image=deleteImage,bd=0,command=deleteTask).pack(side=BOTTOM, pady=13)
















window.mainloop()



