
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.

import sqlite3
from Project import *

def DBStart():
	global DB
	DB= sqlite3.connect("Projects.db")
	global C
	C=DB.cursor();
	
	C.execute("CREATE TABLE IF NOT EXISTS Active_Projects (id integer PRIMARY KEY, name text NOT NULL, org text, brief text, status NOT NULL, date DATE, dir text, exe text)")
	C.execute("CREATE TABLE IF NOT EXISTS Inactive_Projects (id integer PRIMARY KEY, name text NOT NULL, org text, brief text, status NOT NULL, date DATE, dir text, exe text)")

def DBInsert(P):
	global DB
	C.execute("INSERT INTO Active_Projects (name,org,brief,status,date,dir,exe) VALUES ('"+P.getName()+"','"+P.getOrg()+"','"+P.getBrief()+"','"+P.getStatus()+"','"+P.getDate()+"','"+P.getDir()+"','"+P.getExe()+"')")
	DB.commit()
	
def GetActive():
	PL=[]
	for row in C.execute("SELECT * FROM Active_Projects ORDER BY id"):
		P=Project(ID=row[0],name=row[1],org=row[2],brief=row[3],status=row[4],date=row[5],dir=row[6],exe=row[7])
		PL.append(P)
	return PL
	
def CloseDB():
	global DB
	DB.close()