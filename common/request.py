from common.case import render_case
from common.decorator import write_log, write_allure
from common.session import sess
from common.variables import globalVariables, environmentVariables


@write_log
@write_allure
def send_request(
		method,
		url,
		params=None,
		data=None,
		headers=None,
		cookies=None,
		files=None,
		auth=None,
		timeout=None,
		allow_redirects=True,
		proxies=None,
		hooks=None,
		stream=None,
		verify=None,
		cert=None,
		json=None,
		session_index: int = None,
):
	"""发送请求"""
	parameter = {
		"method": method,
		"url": url,
		"params": params,
		"data": data,
		"headers": headers,
		"cookies": cookies,
		"files": files,
		"auth": auth,
		"timeout": timeout,
		"allow_redirects": allow_redirects,
		"proxies": proxies,
		"hooks": hooks,
		"stream": stream,
		"verify": verify,
		"cert": cert,
		"json": json,
		"session_index": session_index,
	}
	# 渲染用例
	variables = {**globalVariables.pool, **environmentVariables.pool}
	parameter = render_case(parameter, variables)
	# 获取session
	if len(sess) == 0:
		sess.create()
	session_index = parameter.pop("session_index")
	if session_index is None:
		session = sess()
	else:
		session = sess[session_index]
	# 发送请求
	response = session.request(**parameter)
	return response
