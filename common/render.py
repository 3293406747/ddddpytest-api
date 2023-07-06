from abc import ABC, abstractmethod
import importlib
import json
import re

# 动态导入`utils.function`模块
utils_function = importlib.import_module("utils.functions")


def replace_function(function_chain: re.Match) -> str:
	"""执行python函数"""
	parent_function = utils_function
	match_function_regex = r"\.?(.+?)\((.*?)\)"
	real_function_chain = function_chain.group(1)
	functions = re.findall(match_function_regex, real_function_chain)

	for name, args in functions:
		parent_function = getattr(parent_function, name)(*args.split(",")) if args else getattr(parent_function, name)()

	if not isinstance(parent_function, str):
		raise RenderTemplateError(f"{parent_function}类型应为str，实际类型为{type(parent_function)}")
	return parent_function


class RenderStrategy(ABC):

	@abstractmethod
	def render(self, key: str | int, sub_template: str | dict | list, template: dict | list) -> None:
		"""抽象渲染方法"""
		pass


class VariablesRenderStrategy(RenderStrategy):
	"""使用变量"""

	def __init__(self):
		# strategy为self
		self.renderTemplate = RenderTemplate(self)
		self.data_for_render = {}

	def render(self, key: str | int, sub_template: str | dict | list, template: dict | list) -> None:
		"""实现抽象渲染方法"""
		if isinstance(sub_template, str) and sub_template.startswith("${") and sub_template.endswith("}"):
			variable_key = sub_template[2:-1]
			variable_value = self.data_for_render.get(variable_key)
			if variable_value: template[key] = variable_value
		elif isinstance(sub_template, (list, dict)):
			template[key] = self.renderTemplate.render(sub_template, self.data_for_render)


class FunctionRenderStrategy(RenderStrategy):
	"""调用python函数"""

	def __init__(self):
		# strategy为self
		self.renderTemplate = RenderTemplate(self)

	def render(self, key: str | int, sub_template: str | dict | list, template: dict | list) -> None:
		"""实现抽象渲染方法"""
		if isinstance(sub_template, str) and sub_template.startswith("{{") and sub_template.endswith("}}"):
			match_function_regex = r"^\{\{(.+?)\}\}$"
			function_chain = re.match(match_function_regex, sub_template)
			template[key] = replace_function(function_chain)
		elif isinstance(sub_template, (list, dict)):
			template[key] = self.renderTemplate.render(sub_template)


class RenderTemplate:

	def __init__(self, strategy: RenderStrategy):
		self.strategy = strategy

	def render(self, template: dict | list, data_for_render: dict | None = None) -> dict:
		"""渲染方法"""
		self.strategy.data_for_render = data_for_render
		if isinstance(template, str): template = json.loads(template)
		if isinstance(template, list):
			for index, sub_template in enumerate(template):
				self.strategy.render(index, sub_template, template)
		elif isinstance(template, dict):
			for key, sub_template in template.items():
				self.strategy.render(key, sub_template, template)
		return template


class RenderTemplateError(Exception):
	pass
