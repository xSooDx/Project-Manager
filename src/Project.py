
# Copyright (C) 2015 Saurabh Sood
# This file is licensed under the terms of the GNU General Public License
# version 2.  This program is licensed "as is" without any warranty of any
# kind, whether express or implied.

class Project:
	
	
	def __init__(self,**a):
		self.Details={
						"name":"None",
						"org":"None",
						"brief":"None",
						"status":"None",
						"dir":"None",
						"exe":"None"}
		self.Details.update();
	def getName(self):
		return self.Details["name"];
	def getOrg(self):
		return self.Details["org"];
	def getBrief(self):
		return self.Details["brief"];
	def getStatus(self):
		return self.Details["status"];
	def runExe(self):
		pass
	def openDir(self):
		pass
		
		