# ddddpytest-api

本项目实现接口自动化的技术选型：**python+request+pytest+allure**。request用于发送HTTP协议的请求，pytest作为测试执行器，allure用于生成测试报告。

## 特征

- 采用关键字驱动设计，yaml文件管理用例关键字，可关联excel中数据；
- 可使用变量和python函数渲染用例，在发送请求前自动渲染；
- 采用统一请求封装，session自动关联，支持多个session之间进行切换；
- 采用yaml文件管理全局变量和环境变量；
- 项目运行生成log日志和allure报告；

## 流程

读取yaml用例 --> 校验用例格式 --> 关联excel数据 --> 渲染用例 --> 获取session --> session发送请求 --> 生成日志和allure报告

## 关于

目前作者还在做功能测试，会写一些python代码，最近有时间结合已学的知识写了这个项目。希望这个项目对正在学习自动化或者从事自动化的你有所帮助。
项目并不完善，可能存在很多问题，如果你有任何建议或遇到了任何问题，希望你能为该项目提issue。如果喜欢该项目，可以为该项目star。
你也可以加我微信，我们一起交流探讨。微信号: QM85329140

# 部署

```shell
# 运行下面的命令下载源码
git clone https://github.com/3293406747/ddddpytest-api.git
# 切换到项目所在目录
cd ddddpytest-api
# 确认python和pip工具已安装，在命令行运行下面的命令安装项目运行依赖
pip install requirements.txt
# 切换到flask目录
cd test/flask_app
# 启动flask服务
python app.py
```
新建一个命令行确保所在目录为项目根目录，执行下面的命令。
```shell
python main.py
```

