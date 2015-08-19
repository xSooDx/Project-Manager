
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.


from tkinter import *
from Project import *

	

project_list=[];

def newProj():	
		w=80
		newP = Tk()
		newP.title("New Project")
		newP.geometry("%dx%d+0+0"%(780,600))
		
		Title = Label(newP,text ="New Project Details")
		Title.grid(row=-0,column=0,columnspan=4);
		
		namL = Label(newP,text="Name: ")
		namL.grid(row=1,column=0)
		Name = Entry(newP,width=w)
		Name.grid(row=1,column=1,columnspan=2)
		
		orgL = Label(newP,text="Organization: ")
		orgL.grid(row=2,column=0)
		Org = Entry(newP,width=w)
		Org.grid(row=2,column=1,columnspan=2)
		
		briefL = Label(newP,text="Brief Description: ")
		briefL.grid(row=3,column =0,sticky=N)
		
		Brief = Text(newP,height = 3,width = w-16)
		Brief.grid(row=3,column =1,columnspan=2)
		
		execL = Label(newP,text="Executable Path: ")
		execL.grid(row=4,column=0)
		
		execT = Entry(newP,width = w)
		execT.grid(row=4,column=1,columnspan=2)
		
		dirL = Label(newP,text="Project Folder: ")
		dirL.grid(row=5,column=0)
		
		Dir = Entry(newP,width = w)
		Dir.grid(row=5,column=1,columnspan=2)
		
		def addP():
			P=Project(name=Name.get(),org=Org.get(),brief=Brief.get("1.0",END),exe=execT.get(),dir=Dir.get())
			project_list.append(P)
			newP.destroy(); 
		create = Button(newP,text="Create Project",command=addP)
		create.grid(row=6,column=2)
		cancel = Button(newP,text="Cancel",command = newP.destroy)
		cancel.grid(row=6,column=1)
		

main = Tk();
main.title("Project Mnagaer")
main.geometry("%dx%d+0+0"%(1200,800))
Title=Label(main,text="Project Manager",font=("Times",24,"bold"))
Title.pack();
B=Button(main,text = "New Project",command = newProj)
B.pack()
main.mainloop();
