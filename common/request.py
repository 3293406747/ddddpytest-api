from common.session import SessionManager

sess = SessionManager()

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
	# 获取session
	if len(sess) == 0:
		sess.create()
	if session_index is None:
		session = sess()
	else:
		session = sess[session_index]
	# 发送请求
	response = session.request(
		method,
		url,
		params=params,
		data=data,
		headers=headers,
		cookies=cookies,
		files=files,
		auth=auth,
		timeout=timeout,
		allow_redirects=allow_redirects,
		proxies=proxies,
		hooks=hooks,
		stream=stream,
		verify=verify,
		cert=cert,
		json=json,
	)
	return response
