import pytest

from common.case import read_case
from common.request import send_request


class TestSubject:


	@pytest.mark.parametrize("parameter",read_case("test.yaml"))
	def test_request(self,parameter:dict):
		send_request(**parameter)