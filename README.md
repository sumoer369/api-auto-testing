# JSONPlaceholder 接口自动化测试框架

## 📖 项目简介
基于 Python + Pytest + Requests + YAML + Allure 搭建的接口自动化测试框架，针对 JSONPlaceholder 公开 API 进行接口测试，覆盖 GET / POST / PUT / DELETE 四种请求方法。

## 🛠️ 技术栈
- 测试框架：Python、Pytest、Requests
- 数据驱动：YAML
- 测试报告：Allure
- 持续集成：GitHub Actions

## 📂 项目结构
- `config/`：多环境配置
- `api/`：接口封装层
- `testcases/`：测试用例层
- `data/`：YAML 测试数据
- `utils/`：请求封装与断言工具
- `reports/`：Allure 报告输出

## 🚀 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 执行测试：`pytest`
3. 生成报告：`allure serve ./reports/allure-results`

## 💡 项目亮点
- **分层设计**：配置层、接口层、用例层、工具层分离，易维护
- **数据驱动**：YAML 管理测试数据，新增用例不改代码
- **Allure 报告**：可视化测试报告，支持用例分类与失败追踪
- **CI 集成**：GitHub Actions 自动触发测试
