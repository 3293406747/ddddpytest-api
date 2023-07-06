import yaml
from openpyxl import load_workbook

def read_yaml(filename, encoding='utf-8'):
	""" 读取yaml文件 """
	with open(file=filename, encoding=encoding) as f:
		return yaml.safe_load(f)

def read_excel(filename, sheet=None):
	""" 读取excel文件 """
	wb = load_workbook(filename=filename, read_only=True)
	ws = wb[sheet] if sheet else wb.active
	rows = ws.values
	columns = next(rows)
	return [dict(zip(columns, row)) for row in rows]
