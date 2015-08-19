class Project:
	
	
	def __init__(self,**a):
		self.Details={
						"name":"None",
						"org":"None",
						"brief":"None",
						"status":"None",
						"dir":"None",
						"exe":"None"}
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
		
		self.Details.update();