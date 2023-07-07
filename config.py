import sys

from loguru import logger
from pathlib import Path

# 运行目录设置
testDir = "test"
# 环境变量设置
environment = "test.yaml"

# 日志管理
logger.remove()
logger.add(
	level="DEBUG",
	sink=sys.stderr,
	format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>[<level>{level}</level>]<level>{message}</level>",
)
logger.add(
	level="DEBUG",
	sink=Path(__file__).parent.joinpath(testDir).joinpath("logs", "{time:YYYY-MM-DD}", "log_{time:HH_mm_ss}.log"),
	format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>[<level>{level}</level>]<level>{message}</level>",
	rotation="5 MB",
	retention="1 days",
)
logger.add(
	level="ERROR",
	sink=Path(__file__).parent.joinpath(testDir).joinpath("logs", "{time:YYYY-MM-DD}", "log_error.log"),
	format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>[<level>{level}</level>]<level>{message}</level>",
	rotation="5 MB",
	retention="1 days",
)

# 发送邮件管理
email = {
	"flag": False,
	"smtp_server": "smtp.163.com",				# 邮件服务器地址
	"port": 25,									# 邮件服务器端口号
	"from_addr": ...,							# 发件人地址
	"to_addr": ...,								# 收件人地址
	"username": ...,							# 发件人邮箱的用户名
	"password": ...,							# 发件人邮箱的密码
	"subject": ...,								# 邮件主题
	"success_text": "测试用例全部执行通过了",	 	# 用例执行通过文本
	"failed_text": "测试用例执行失败了",			# 用例执行失败文本
}
