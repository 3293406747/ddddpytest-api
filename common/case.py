import json
import re
from string import Template

from pathlib import Path
import yaml

from common.read import read_yaml, read_excel
from common.render import RenderTemplate, VariablesRenderStrategy, FunctionRenderStrategy, replace_function
from common.verify import VerifyMustKeys, VerifyRequestKeys, VerifyNotMustKeys, VerifySessionKeys
from config import testDir


def verify_case(case: dict) -> dict:
	"""校验用例格式"""
	handler1 = VerifyMustKeys()
	handler2 = VerifyRequestKeys()
	handler3 = VerifyNotMustKeys()
	handler4 = VerifySessionKeys()
	handler1.set_next_handler(handler2).set_next_handler(handler3).set_next_handler(handler4)
	return handler1.verify_case(case)


def read_case(filename, index: int = None, encoding='utf-8') -> list:
	"""读取用例"""
	case_pool = []
	file_path = Path(__file__).parent.parent.joinpath(testDir,"cases", filename)
	if index is None:
		all_cases = read_yaml(file_path, encoding=encoding)
	else:
		all_cases = [read_yaml(file_path, encoding=encoding)[index]]
	for case in all_cases:
		# 用例格式校验
		verify_case(case)
		# 合并excel数据
		data_path = case.pop("data_path", None)
		if data_path is None:
			case_pool.append(case)
			continue
		sheet = case.pop("data_sheet", None)
		case_json = json.dumps(case, ensure_ascii=False)
		excel_data = read_excel(Path(__file__).parent.parent.joinpath(testDir, "datas", data_path), sheet)
		case_pool += [yaml.safe_load(Template(case_json).safe_substitute(data)) for data in excel_data]
		# for data in excel_data:
		# 	case = yaml.safe_load(Template(case_json).safe_substitute(data))
		# 	case_pool.append(case)
	return case_pool


def render_case(case: dict, variables: dict) -> dict:
	"""渲染用例"""
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
	return json.loads(last_case)
