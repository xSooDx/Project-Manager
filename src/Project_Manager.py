
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.


from tkinter import *
from Project import *
from DBManager import *
import time

	

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
			P=Project(name=Name.get(),org=Org.get(),status='Inactive',brief=Brief.get("1.0",END),exe=execT.get(),dir=Dir.get(),date=time.strftime("%d/%m/%Y"))
			DBInsert(P)
			newP.destroy(); 
			update()

		create = Button(newP,text="Create Project",command=addP)
		create.grid(row=6,column=2)
		cancel = Button(newP,text="Cancel",command = newP.destroy)
		cancel.grid(row=6,column=1)
		


def update():
	global project_list
	project_list = GetActive()
	r=4;
	for P in project_list:
		Label(main,text=P.getID(),width=4).grid(row=r,column=0)
		Label(main,text=P.getDate(),width=10).grid(row=r,column=1)
		Label(main,text=P.getName(),width=20).grid(row=r,column=2)
		Label(main,text=P.getOrg(),width=20).grid(row=r,column=3)
		Label(main,text=P.getBrief(),width=50,wraplength=400).grid(row=r,column=4)
		Label(main,text=P.getStatus(),width=10).grid(row=r,column=5)
		Button(main,text="Edit",width=8).grid(row=r,column=6)
		Button(main,text="Go To",width=8).grid(row=r,column=7)
		
		r+=1;

def init():
	DBStart();

	global main
	main = Tk();
	main.title("Project Mnagaer")
	main.geometry("%dx%d+0+0"%(1200,800))
	Title=Label(main,text="Project Manager",font=("Times",24,"bold"),width =50)
	Title.grid(row=0,columnspan=10);

	Label(main,text='ID',width=4).grid(row=2,column=0,pady=30)
	Label(main,text='Date',width=10).grid(row=2,column=1)
	Label(main,text='Name',width=20).grid(row=2,column=2)
	Label(main,text='Organisation',width=20).grid(row=2,column=3)
	Label(main,text='Discription',width=50).grid(row=2,column=4)
	Label(main,text='Status',width=10).grid(row=2,column=5)
	Label(main,width=8).grid(row=2,column=6)
	Label(main,width=8).grid(row=2,column=7)
	Button(main,text = "New Project",command = newProj).grid(row=1,column=1,columnspan=10);
	
	update()

	
init()
main.mainloop();

CloseDB()
