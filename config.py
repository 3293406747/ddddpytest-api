import sys

from loguru import logger
from pathlib import Path

testDir = "test"
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
	sink=Path(__file__).parent.joinpath(testDir).joinpath("logs","{time:YYYY-MM-DD}","log_{time:HH_mm_ss}.log"),
	format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>[<level>{level}</level>]<level>{message}</level>",
	rotation="5 MB",
	retention="1 days",
)
logger.add(
	level="ERROR",
	sink=Path(__file__).parent.joinpath(testDir).joinpath("logs","{time:YYYY-MM-DD}","log_error.log"),
	format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>[<level>{level}</level>]<level>{message}</level>",
	rotation="5 MB",
	retention="1 days",
)
