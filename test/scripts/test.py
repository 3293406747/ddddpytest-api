import allure
import pytest

from common.case import read_case
from common.request import send_request


@allure.epic("ddddpytest-api接口自动化测试项目")
@allure.feature("测试课题")
class TestSubject:

	@allure.story("测试请求")
	@pytest.mark.parametrize("parameter",read_case("test.yaml"))
	def test_request(self,parameter:dict):
		allure.dynamic.title(parameter["name"])
		response = send_request(**parameter)
		assert response.json()["code"] == 200