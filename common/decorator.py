import json

from config import logger
from requests import Response
import allure


def write_log(send_request):
	"""记录日志装饰器"""
	def decorator(**kwargs):
		logger.debug(f"用例名称: {kwargs['name']}")
		response: Response = send_request(**kwargs['request'])
		logger.debug(f"url: {response.url}")
		logger.debug(f"method: {response.request.method}")
		logger.debug(f"headers: {response.request.headers}")
		logger.debug(f"body: {response.request.body}")
		logger.debug(f"response: {response.content}\n")
		return response

	return decorator


def write_allure(send_request):
	"""记录allure报告装饰器"""
	def decorator(**kwargs):
		response: Response = send_request(**kwargs)
		allure.attach(response.request.url,"url",allure.attachment_type.TEXT)
		allure.attach(response.request.method,"method",allure.attachment_type.TEXT)
		allure.attach(json.dumps(dict(response.request.headers)),"headers",allure.attachment_type.JSON)
		body = "null" if response.request.body is None else response.request.body.decode('utf-8')
		allure.attach(body,"body",allure.attachment_type.TEXT)
		allure.attach(response.content,"response",allure.attachment_type.TEXT)
		return response
	return decorator
