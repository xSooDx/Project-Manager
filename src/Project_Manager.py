
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.


from tkinter import *
from tkinter.ttk import *
from Project import *
from DBManager import *
from tkinter import filedialog

import time

	

project_list=[];

def newProj():	
		w=75
		newP = Toplevel()
		newP.title("New Project")
		newP.lift()
		
		Title = Label(newP,text ="New Project Details")
		Title.grid(row=-0,column=0,columnspan=4);
		
		namL = Label(newP,text="Name: ")
		namL.grid(row=1,column=0)
		Name = Entry(newP,width=w)
		Name.grid(row=1,column=1)
		
		orgL = Label(newP,text="Organization: ")
		orgL.grid(row=2,column=0)
		Org = Entry(newP,width=w)
		Org.grid(row=2,column=1)
		
		briefL = Label(newP,text="Brief Description: ")
		briefL.grid(row=3,column =0,sticky=N)
		
		Brief = Text(newP,height = 3,width = w-15)
		Brief.grid(row=3,column =1)
		
		execL = Label(newP,text="Executable Path: ")
		execL.grid(row=4,column=0)
		def getExecutable():
			F=filedialog.askopenfilename(parent=newP,initialdir=Dir.get())
			execT.delete(0,END)
			execT.insert(0,F)
		
		execT = Entry(newP,width = w)
		execT.grid(row=4,column=1)
		Button(newP,text="...",command=getExecutable).grid(row=4,column=2)
		
		dirL = Label(newP,text="Project Folder: ")
		dirL.grid(row=5,column=0)
		
		def getDirectory():
			F=filedialog.askdirectory(parent=newP,initialdir=Dir.get())
			Dir.delete(0,END)
			Dir.insert(0,F)
		Dir = Entry(newP,width = w)
		Dir.grid(row=5,column=1)
		Button(newP,text="...",command=getDirectory).grid(row=5,column=2)
		
		def addP():
			P=Project(name=Name.get(),org=Org.get(),status='Inactive',brief=Brief.get("1.0",END),exe=execT.get(),dir=Dir.get(),date=time.strftime("%d/%m/%Y"))
			DBInsert(P)
			newP.destroy(); 
			update()

		create = Button(newP,text="Create Project",command=addP)
		create.grid(row=6,column=0)
		cancel = Button(newP,text="Cancel",command = newP.destroy)
		cancel.grid(row=6,column=1)

def editP(P):
	w=75
	eP = Toplevel()
	eP.title(P.getName())
	eP.lift()
	TitleF = Frame(eP)
	TitleF.pack()
	DetailsF=Frame(eP)
	DetailsF.pack()
	Title = Label(DetailsF,text =P.getName())
	Title.grid(row=-0,column=0,columnspan=4);
	
	namL = Label(DetailsF,text="Name: ")
	namL.grid(row=1,column=0)
	Name = Entry(DetailsF,width = w)
	Name.grid(row=1,column=1)
	Name.delete(0,END)
	Name.insert(0,P.getName())
	
	orgL = Label(DetailsF,text="Organization: ")
	orgL.grid(row=2,column=0)
	Org = Entry(DetailsF,width = w)
	Org.grid(row=2,column=1)
	Org.delete(0,END)
	Org.insert(0,P.getOrg())
	
	briefL = Label(DetailsF,text="Brief Description: ")
	briefL.grid(row=3,column =0,sticky=N)
		
	Brief = Text(DetailsF,height = 3,width = w-15)
	Brief.grid(row=3,column =1)
	Brief.insert(END,P.getBrief())
	
	execL = Label(DetailsF,text="Executable Path: ")
	execL.grid(row=4,column=0)
	def getExecutable():
		F=filedialog.askopenfilename(parent=DetailsF,initialdir=Dir.get())
		execT.delete(0,END)
		execT.insert(0,F)
	
	execT = Entry(DetailsF,width = w)
	execT.grid(row=4,column=1)
	execT.delete(0,END)
	execT.insert(0,P.getExe())
	Button(DetailsF,text="...",command=getExecutable).grid(row=4,column=2)
	
	dirL = Label(DetailsF,text="Project Folder: ")
	dirL.grid(row=5,column=0)
	
	def getDirectory():
		F=filedialog.askdirectory(parent=DetailsF,initialdir=Dir.get())
		Dir.delete(0,END)
		Dir.insert(0,F)
	Dir = Entry(DetailsF,width = w)
	Dir.grid(row=5,column=1)
	Dir.delete(0,END)
	Dir.insert(0,P.getDir())
	
	Button(DetailsF,text="...",command=getDirectory).grid(row=5,column=2)
	Label(DetailsF,text="Status: ").grid(row=6, column=0)
	statusO = Combobox(DetailsF,values=["Inactive","Active","Urgent","Complete","Failed"])
	statusO.grid(row=6,column=1)
		
def update():
	global project_list
	project_list = GetActive()
	r=4;
	for P in project_list:
		print(P)
		Label(main,text=P.getID(),width=4).grid(row=r,column=0)
		Label(main,text=P.getDate(),width=10).grid(row=r,column=1)
		Label(main,text=P.getName(),width=20).grid(row=r,column=2)
		Label(main,text=P.getOrg(),width=20).grid(row=r,column=3)
		Label(main,text=P.getBrief(),width=50,wraplength=400).grid(row=r,column=4)
		Label(main,text=P.getStatus(),width=10).grid(row=r,column=5)
		
		Button(main,text="Open",command=P.openDir,width=8).grid(row=r,column=6)			
			
		#Button(main,text="Edit",command=P.editProject,width=8).grid(row=r,column=7)
		r+=1;

def init():
	DBStart()

	global main
	global root
	root = Tk()
	root.title("Project Mnagaer")
	root.geometry("%dx%d+0+0"%(1200,800))
	titleFrame= Frame(root)
	Title=Label(titleFrame,text="Project Manager",font=("Times",24,"bold"))
	Title.pack()
	titleFrame.pack()
	npbFrame = Frame(root)
	Button(npbFrame,text = "New Project",command = newProj).pack()
	npbFrame.pack()
	main=Frame(root)
	main.pack()
	
	Label(main,text='ID',width=4).grid(row=2,column=0,pady=30)
	Label(main,text='Date',width=10).grid(row=2,column=1)
	Label(main,text='Name',width=20).grid(row=2,column=2)
	Label(main,text='Organisation',width=20).grid(row=2,column=3)
	Label(main,text='Discription',width=50).grid(row=2,column=4)
	Label(main,text='Status',width=10).grid(row=2,column=5)
	Label(main,width=8).grid(row=2,column=6)
	Label(main,width=8).grid(row=2,column=7)
	
	
	update()


init()
main.mainloop();

CloseDB()
