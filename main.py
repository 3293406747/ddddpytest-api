#!/usr/bin/env python
import os

import pytest
from pathlib import Path

from config import testDir

msg = r"""
                    _ooOoo_
                   o8888888o  
                   88" . "88   
                   (| -_- |)   
                    O\ = /O   
                ____/`---'\____
              .   ' \\| |// `.
               / \\||| : |||// \
             / _||||| -:- |||||- \
               | | \\\ - /// | |
             | \_| ''\---/'' | |
              \ .-\__ `-` ___/-. /
           ___`. .' /--.--\ `. . __
        ."" '< `.___\_<|>_/___.' >'"".
       | | : `- \`.;`\ _ /`;.`/ - ` : | |
         \ \ `-. \_ __\ /__ _/ .-` / /
 ======`-.____`-.___\_____/___.-`____.-'======
                    `=---='
 .............................................
          佛祖保佑             永无BUG
"""
print(msg)

if __name__ == '__main__':
	pytest.main()
	report_path = str(Path(__file__).parent.joinpath(testDir,'reports'))
	os.system(f'allure generate ./temp -o {report_path} --clean')