import copy


class CaseVerification:
	"""用例格式校验器"""

	def __init__(self):
		self._next_handler = None

	def set_next_handler(self, handler):
		self._next_handler = handler
		return handler

	def verify_case(self, case: dict) -> dict:
		pass


class VerifyMustKeys(CaseVerification):
	"""必选参数校验"""

	REQUIRED_KEYS = ("name", "request")

	def verify_case(self, case: dict) -> dict:
		new_case = copy.deepcopy(case)
		for key in VerifyMustKeys.REQUIRED_KEYS:
			if key not in new_case:
				msg = f"用例必须包含一级关键字{key}"
				raise CaseVerificationError(msg)
		new_case.pop("name")
		self._next_handler.verify_case(new_case)
		return case


class VerifyRequestKeys(CaseVerification):
	"""请求参数校验"""

	REQUIRED_KEYS = ("url", "method")
	ALLOWED_KEYS = ("params", "data", "json", "files", "headers")

	def verify_case(self, case: dict) -> dict:
		request = case.pop("request")
		for key in VerifyRequestKeys.REQUIRED_KEYS:
			if key not in request:
				msg = f"用例的request关键字下必须包含二级关键字{key}"
				raise CaseVerificationError(msg)
			else:
				request.pop(key)

		unexpected_keys = set(request) - set(VerifyRequestKeys.ALLOWED_KEYS)  # 集合时间复杂度比遍历时间复杂度低
		if unexpected_keys:
			msg = f"用例的request关键字下不能包含以下关键字：{', '.join(unexpected_keys)}"
			raise CaseVerificationError(msg)

		self._next_handler.verify_case(case)
		return case


class VerifyNotMustKeys(CaseVerification):
	"""非必选参数校验"""

	ALLOWED_KEYS = ("data_path", "data_sheet", "session_index")

	def verify_case(self, case: dict) -> dict:
		if case == {}:
			return case
		unexpected_keys = set(case) - set(VerifyNotMustKeys.ALLOWED_KEYS)
		if unexpected_keys:
			msg = f"用例的一级关键字不能包含以下关键字：{', '.join(unexpected_keys)}"
			raise CaseVerificationError(msg)
		self._next_handler.verify_case(case)
		return case


class VerifySessionKeys(CaseVerification):
	"""session参数校验"""

	def verify_case(self, case: dict) -> dict:
		if case.get("session_index") and not isinstance(case.get("session_index"), int):
			msg = f"用例的session关键字下必须整数格式。"
			raise CaseVerificationError(msg)

		self._next_handler.verify_case(case)
		return case


class CaseVerificationError(Exception):
	pass