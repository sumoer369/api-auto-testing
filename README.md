# 🚀 JSONPlaceholder 接口自动化测试框架

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-9.1-green?logo=pytest)
![Requests](https://img.shields.io/badge/Requests-2.32-orange)
![CI](https://github.com/sumoer369/api-auto-testing/actions/workflows/ci.yml/badge.svg)

> 基于 Python + Pytest + Requests + YAML 搭建的接口自动化测试框架，覆盖 GET / POST / PUT / DELETE 四种请求方法。
> ## 📖 项目简介

本项目模拟企业级接口测试工作流，采用 **分层设计 + 数据驱动 + 多层断言 + CI 集成** 的工程化方案。

## 🛠️ 技术栈

| 分类 | 技术 |
| :--- | :--- |
| 编程语言 | Python 3.13 |
| 测试框架 | Pytest |
| HTTP请求 | Requests |
| 数据驱动 | YAML |
| 测试报告 | pytest-html |
| 持续集成 | GitHub Actions |
## 📂 项目结构

- config/ — 多环境配置
- api/ — 接口封装层
- testcases/ — 测试用例层
- data/ — YAML测试数据
- utils/ — 请求与断言工具
- reports/ — 测试报告输出

## 🚀 快速开始

1. 安装依赖：pip install -r requirements.txt
2. 执行测试：pytest
3. 查看报告：打开 reports/report.html
4. ## 📊 测试覆盖

| 模块 | 测试场景 | 用例数 |
| :---: | :--- | :---: |
| GET | 获取文章详情、列表、不存在的文章 | 3 |
| POST | 创建文章（正常/空标题） | 2 |
| PUT | 更新文章标题 | 1 |
| DELETE | 删除文章 | 1 |
| 合计 | | 7 |
## 💡 项目亮点

### 🏗️ 分层设计
- 配置层：多环境地址、超时配置
- 接口层：所有接口统一封装
- 用例层：只写业务逻辑
- 工具层：请求、断言公共封装

### 📦 数据驱动
- 测试数据存于 data/posts_data.yaml
- 新增用例只加 YAML，不改代码

### ✅ 多层断言
- 状态码断言
- 字段值断言
- 字段存在性断言

### ⚙️ CI 集成
- GitHub Actions 自动触发测试
- 每次推送自动运行全部用例

## 📈 测试结果

- 用例总数：7
- 通过数：7
- 通过率：100%
- 覆盖方法：GET / POST / PUT / DELETE

## 🔗 相关链接

- JSONPlaceholder：https://jsonplaceholder.typicode.com/
- Pytest 文档：https://docs.pytest.org/
- Requests 文档：https://requests.readthedocs.io/