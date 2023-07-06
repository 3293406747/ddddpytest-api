import os

from common.read import read_yaml
from common.write import write_yaml


class GlobalVariables:

	def __init__(self):
		if not os.path.exists("variables/gobal.yaml"):
			write_yaml("variables/gobal.yaml")
		self.pool = read_yaml("variables/gobal.yaml") or {}

	def set(self,key,value):
		self.pool[key] = value
		write_yaml("variables/gobal.yaml",self.pool)

	def get(self,key,default=None):
		return self.pool.get(key,default=default)

	def unset(self,key,default=None):
		self.pool.pop(key,default=default)
		write_yaml("variables/gobal.yaml", self.pool)



class EnvironmentVariables:

	def __init__(self,filename):
		if not os.path.exists(filename):
			write_yaml(filename)
		self.filename = filename
		self.pool = read_yaml(self.filename) or {}

	def set(self,key,value):
		self.pool[key] = value
		write_yaml(self.filename,self.pool)

	def get(self,key,default=None):
		return self.pool.get(key,default=default)

	def unset(self,key,default=None):
		self.pool.pop(key,default=default)
		write_yaml(self.filename, self.pool)