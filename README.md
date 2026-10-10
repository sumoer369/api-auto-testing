JSONPlaceholder 接口自动化测试框架
https://github.com/sumoer369/api-auto-testing/actions/workflows/ci.yml/badge.svg

📖 项目简介
基于 Python + Pytest + Requests + YAML 搭建的接口自动化测试框架，针对 JSONPlaceholder 公开 API 进行接口测试，覆盖 GET / POST / PUT / DELETE 四种请求方法，支持数据驱动、多层断言、自动化报告和持续集成。

🛠️ 技术栈
分类	技术
编程语言	Python 3.13
测试框架	Pytest
HTTP请求	Requests
数据驱动	YAML
测试报告	pytest-html
持续集成	GitHub Actions
📂 项目结构
api-auto-testing/
├── config/ # 多环境配置
│ └── config.yaml
├── api/ # 接口封装层
│ └── post_api.py
├── testcases/ # 测试用例层
│ └── test_posts.py
├── data/ # YAML测试数据
│ └── posts_data.yaml
├── utils/ # 工具层
│ ├── request_util.py # 请求封装
│ └── assert_util.py # 断言封装
├── reports/ # 测试报告输出
├── conftest.py # 全局Fixture
├── pytest.ini # Pytest配置
└── requirements.txt

🚀 如何运行
安装依赖：pip install -r requirements.txt

执行测试：pytest

查看报告：打开 reports/report.html

📊 测试覆盖
模块	测试场景	用例数
GET	获取文章详情、获取文章列表、获取不存在的文章	3
POST	创建文章（正常/空标题）	2
PUT	更新文章标题	1
DELETE	删除文章	1
合计		7
💡 项目亮点
1. 分层设计
配置层：多环境地址、超时配置，切换环境只改一行配置

接口层：所有接口统一封装，接口路径变更只改一处

用例层：只写业务逻辑，不关心请求细节

工具层：请求封装、断言封装，公共能力复用

2. 数据驱动
测试数据存放在 data/posts_data.yaml，新增用例只加YAML，不改代码

采用 @pytest.mark.parametrize 参数化，一条函数覆盖多组数据

3. 多层断言
状态码断言：验证HTTP响应状态

字段值断言：验证响应体关键字段

字段存在性断言：验证响应结构完整性

4. CI集成
集成 GitHub Actions，代码提交自动触发测试

每次推送自动运行全部用例，保障代码质量

📈 测试结果
7 passed in 10.86s

通过率：100%

覆盖接口方法：GET / POST / PUT / DELETE