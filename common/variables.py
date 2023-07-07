from pathlib import Path

from common.read import read_yaml
from common.write import write_yaml


class GlobalVariables:

	def __init__(self):
		self.filename = Path(__file__).parent.parent.joinpath("variables","global.yaml")
		if not self.filename.exists():
			write_yaml(self.filename)
		self.pool = read_yaml(self.filename) or {}

	def set(self, key, value):
		self.pool[key] = value
		write_yaml(self.filename, self.pool)

	def get(self, key, default=None):
		return self.pool.get(key, default=default)

	def unset(self, key, default=None):
		self.pool.pop(key, default=default)
		write_yaml(self.filename, self.pool)


class EnvironmentVariables:

	def __init__(self, filename):
		self.filename = Path(__file__).parent.parent.joinpath("variables").joinpath(filename)
		if not self.filename.exists():
			write_yaml(self.filename)
		self.pool = read_yaml(self.filename) or {}

	def set(self, key, value):
		self.pool[key] = value
		write_yaml(self.filename, self.pool)

	def get(self, key, default=None):
		return self.pool.get(key, default=default)

	def unset(self, key, default=None):
		self.pool.pop(key, default=default)
		write_yaml(self.filename, self.pool)

globalVariables = GlobalVariables()
environmentVariables = EnvironmentVariables("test.yaml")