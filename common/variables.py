from pathlib import Path

from common.read import read_yaml
from common.write import write_yaml
from config import environment


class GlobalVariables:
	"""全局变量"""
	def __init__(self):
		self.filename = Path(__file__).parent.parent.joinpath("variables","global.yaml")
		if not self.filename.exists():
			write_yaml(self.filename)
		self.pool = read_yaml(self.filename) or {}

	def set(self, key, value):
		"""设置全局变量"""
		self.pool[key] = value
		write_yaml(self.filename, self.pool)

	def get(self, key, default=None):
		"""获取全局变量"""
		return self.pool.get(key, default=default)

	def unset(self, key, default=None):
		"""删除全局变量"""
		self.pool.pop(key, default=default)
		write_yaml(self.filename, self.pool)


class EnvironmentVariables:
	"""环境变量"""
	def __init__(self, filename):
		self.filename = Path(__file__).parent.parent.joinpath("variables").joinpath(filename)
		if not self.filename.exists():
			write_yaml(self.filename)
		self.pool = read_yaml(self.filename) or {}

	def set(self, key, value):
		"""设置环境变量"""
		self.pool[key] = value
		write_yaml(self.filename, self.pool)

	def get(self, key, default=None):
		"""获取环境变量"""
		return self.pool.get(key, default=default)

	def unset(self, key, default=None):
		"""删除环境变量"""
		self.pool.pop(key, default=default)
		write_yaml(self.filename, self.pool)

globalVariables = GlobalVariables()
environmentVariables = EnvironmentVariables(environment)