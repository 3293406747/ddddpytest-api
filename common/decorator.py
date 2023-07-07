from config import logger
from requests import Response

def write_log(send_request):
	def decorator(**kwargs):
		logger.debug(f"用例名称: {kwargs['name']}")
		response:Response = send_request(**kwargs['request'])
		logger.debug(f"url: {response.url}")
		logger.debug(f"method: {response.request.method}")
		logger.debug(f"headers: {response.request.headers}")
		logger.debug(f"body: {response.request.body}\n")
		return response
	return decorator

