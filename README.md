

# my-ai-journey

大二信安暑假 8 周：从零 Python 到 AI Agent

## Week 1 — Python 基础

| Day | 内容 | 文件 |
|-----|------|------|
| 1 | 变量、类型、`if/for/while`，全部加类型注解 | `src/basics.py` |
| 2 | 函数、参数、作用域 | `src/function.py` |
| 3 | 文件读写 JSON、`try/except`、logging | `src/file_io.py` |
| 4 | OOP：`class`、`@dataclass`、`Enum` | `src/oop_basics.py` |
| 5 | 记账本项目：数据类 + JSON 持久化 | `src/account_book_single.py` |
| 6 | 拆为包结构 + pytest | `src/account_book/` + `tests/test_account.py` |
| 7 | Git 整理 + 复习 | |

## Week 2 — 标准库 + HTTP + 代码规范

| Day | 内容 | 文件 |
|-----|------|------|
| 1 | pathlib / datetime / re | `src/file_explorer.py` |
| 2 | 日志分析 Top 10 单词 | `src/log_analyzer.py` + `tests/test_log.py` |
| 3 | CSV 清洗（pandas 去空行去重） | `src/csv_cleaner.py` + `tests/test_csv.py` |
| 4 | 免费天气 API（requests） | `src/weather.py` + `tests/test_weather.py` |
| 5 | SQLite 建表/插入/查询 | `src/db_demo.py` + `tests/test_db.py` |
| 6 | ruff / black / mypy 配置 | `pyproject.toml` |
| 7 | GitHub 推送 + README | |

## Week 3 — FastAPI + 异步

| Day | 内容 | 文件 |
|-----|------|------|
| 1 | FastAPI + uvicorn 起步 | `src/fastapi_demo/hello_fastapi.py` |
| 2 | async/await + asyncio.gather | `src/fastapi_demo/async_demo.py` |
| 3 | pydantic-settings + .env | `src/fastapi_demo/settings.py` |
| 4 | 天气 API 封装（httpx 异步） | `src/fastapi_demo/weather_api.py` |
| 5 | CORS + POST 批量请求 | `src/fastapi_demo/cors_post.py` + `tests/test_cors_post.py` |
| 6 | Postman 测试 | |
| 7 | 复习 + README 更新 | |

## Week 4 — LLM API + Prompt 工程

| Day | 内容 | 文件 |
|-----|------|------|
| 1 | Transformer 科普 + Token 概念 | |
| 2 | DeepSeek API 第一个对话 | `src/prompt_eng/chat_v1.py` |
| 3 | temperature / tenacity / 流式输出 | `src/prompt_eng/llm_utils.py` |
| 4 | Zero-shot / Few-shot / CoT 对比 | `src/prompt_eng/prompt_compare.py` |
| 5 | 结构化输出：杂乱文本 → JSON | `src/prompt_eng/info_extractor.py` |
| 6 | 批量测试 10 条 + 准确率 | `src/prompt_eng/eval_report.py` |
| 7 | 评测报告 + 面试话术 | `src/prompt_eng/eval_report.md` |

## Week 5 — 手写 ReAct Agent（工具调用）

| Day | 内容 | 文件 |
|-----|------|------|
| 1 | Agent 工具 Schema + system prompt 构建 | `src/agent/schemas.py` |
| 2 | 工具实现：时间查询 / 安全计算器（ast） | `src/agent/tool.py` |
| 3 | ReAct 主循环：思考→调用→观察 | `src/agent/agent_v1.py` |
| 4 | 知识库基础：文档加载 + 文本切分 | `src/agent/doc_loader.py` + `src/agent/text_splitter.py` |
| 5 | 字符袋向量 + SQLite 向量存储检索 | `src/agent/embedder.py` + `src/agent/db.py` |
| 6 | 5 场景测试集验证 + structured logging | `tests/test_agent.py` |
| 7 | 复习 + README 更新 | |

## 运行

```bash
pip install -r requirements.txt
pytest tests/ -v

# 启动 FastAPI 服务
uvicorn src.fastapi_demo.cors_post:app --reload
```

## 工具链
- Python 3.12+
- ruff / black / mypy
- pytest
