# my-ai-journey

零基础 → AI Agent 学习路线项目（Week 6-7：Agent + RAG）。

## 功能

- `src/agent/`：ReAct Agent（3 个工具：时间、计算器、本地文档搜索）
- `src/rag/`：RAG 管线（ChromaDB 向量库 + 检索 + 问答）
- `tests/`：pytest 测试

## 目录结构

```
src/
  agent/
    schemas.py        # 工具 Schema 标准化
    tool.py           # 工具实现 + call_tool
    agent_v1.py       # ReAct 循环
    agent_v3.py       # 三工具调度测试
    doc_loader.py     # 读 txt/pdf/docx
    text_splitter.py  # 三种切分 + overlap
    embedder.py       # 字符袋向量（离线兜底）
  rag/
    vectordb.py       # ChromaDB 向量库
    rag_v1.py         # 问答
    experiment_report.py  # 调参实验
  main.py             # FastAPI 入口
tests/
  test_agent.py
  test_rag.py
```

## 运行

```bash
python -m src.agent.agent_v3        # 跑 Agent V3 测试
python -m pytest tests/ -q          # 跑测试
```

## 容器化

```bash
docker-compose up -d
# 访问 http://localhost:8000/qa?question=你的问题
```

## 备注

- Week 6 embedder 使用字符袋向量，检索质量有限（计划要求真实 Embedding API）
- pytest 真 API 测试需要 `.env` 里有效 DeepSeek key
- 容器通过 `SILICONFLOW_KEY` 环境变量注入 key
