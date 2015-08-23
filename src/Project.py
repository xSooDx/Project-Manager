
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.
import subprocess

class Project:
	
	
	def __init__(self,**a):
		self.Details={
						"ID":"0",
						"name":"None",
						"org":"None",
						"brief":"None",
						"status":"None",
						"dir":"None",
						"exe":"None",
						"date":"None"}
		self.Details.update(a);
	def getID(self):
		return self.Details["ID"];
	def getName(self):
		return self.Details["name"];
	def getOrg(self):
		return self.Details["org"];
	def getBrief(self):
		return self.Details["brief"];
	def getStatus(self):
		return self.Details["status"];
	def getDate(self):
		return self.Details["date"];
	def getDir(self):
		return self.Details["dir"];
	def getExe(self):
		return self.Details["exe"];
	def runExe(self):
		pass
	def openDir(self):
		subprocess.Popen(r'explorer '+self.dir)
	def __str__(self):
		return str(self.Details)
		
		