import json
import re
from string import Template

from common.render import RenderTemplate, VariablesRenderStrategy, FunctionRenderStrategy, replace_function
from common.verify import VerifyMustKeys, VerifyRequestKeys, VerifyNotMustKeys, VerifySessionKeys


def verify_case(case: dict) -> dict:
	"""校验用例格式"""
	handler1 = VerifyMustKeys()
	handler2 = VerifyRequestKeys()
	handler3 = VerifyNotMustKeys()
	handler4 = VerifySessionKeys()
	handler1.set_next_handler(handler2).set_next_handler(handler3).set_next_handler(handler4)
	return handler1.verify_case(case)


def read_case(case: dict, index: int = None, encoding='utf-8'):
	"""读取用例"""
	...


def render_case(case: dict, variables: dict) -> dict:
	"""渲染用例"""
	# 合并字典
	# merge = variables.pool | environments.pool
	# 第一次渲染 使用变量渲染
	last_case = RenderTemplate(VariablesRenderStrategy()).render(case, variables)
	# 第二次渲染 使用python函数
	last_case = RenderTemplate(FunctionRenderStrategy()).render(last_case)
	# 第三次渲染 使用变量渲染
	json_template = json.dumps(last_case, ensure_ascii=False)
	last_case = Template(json_template).safe_substitute(variables)
	# 第四次渲染 使用python函数
	json_template = json.dumps(last_case, ensure_ascii=False)
	match_function_regex = r"\{\{(.*?)\}\}"  # 匹配python函数
	json_template = re.sub(match_function_regex, replace_function, json_template)
	# 返回字典格式模板
	last_case = json.loads(json_template)
	return json.loads(last_case) if isinstance(last_case, str) else last_case