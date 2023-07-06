import yaml


def write_yaml(filename, content='', encoding='utf-8'):
	with open(filename, mode="w", encoding=encoding) as f:
		yaml.safe_dump(content, f)
