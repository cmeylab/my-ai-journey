# 面试准备：3 个项目故事 + 手写伪代码

> 8 周学习路线的面试弹药库。每个故事按「背景 → 做法 → 成果 → 亮点 → 话术 → 追问」组织。
> 标注 `(实测)` 的数字请用代码真实跑出来填，不要编。

---

## 故事一：手写 ReAct Agent（不依赖框架）

### 背景
需要让 LLM 具备"调用工具解决复杂任务"的能力。市面上大多直接用 LangChain，但我想真正理解 Agent 的底层原理，所以**从零手写**了一个 ReAct 循环。

### 做法
- **工具标准化**：用 JSON Schema 定义工具列表（`schemas.py`），每个工具有 name / description / parameters
- **3 个工具**（`tool.py`）：
  - `get_current_time` —— 获取当前时间（LLM 自身不知道）
  - `calculator` —— 数学计算（LLM 算不准）
  - `search_local_docs` —— 搜索本地文档（LLM 不知道你电脑里有什么）
- **解析模型输出**（`agent_v1.py`）：识别 `调用工具: {...}` 格式 → 执行工具；否则视为直接回答
- **Agent 循环**：多轮 `messages` 累积，设 `max_steps` 上限防止死循环；工具输出格式非法时返回 `__retry__` 让模型重试
- **会话持久化**：对话记录存 SQLite（`db.py`），用 `session_id` 区分

### 成果
- 5 个测试场景全过（monkeypatch 掉真实 API 调用，`test_agent.py`）
- 混合问题（如"北京现在几点 + 帮我算 3+5*2"）能正确编排多个工具

### 亮点（最值钱的点）
> "我没有用 LangChain，而是手写 ReAct 循环。这样我对 System Prompt 怎么定义工具、怎么解析模型输出、怎么控制步数和重试，理解得非常深。框架是黑盒，手写一遍之后再看框架反而更通透。"

### 可能的追问 + 怎么答
- **Q：为什么不用 LangChain？** A：学习阶段手写更值钱；生产环境我会用框架提效，但手写经验让我知道框架在替我做什么。
- **Q：模型输出格式不合法怎么办？** A：解析失败时返回 `__retry__`，在 messages 里追加"格式不合法请重新输出"，最多重试到 max_steps。
- **Q：工具调用失败呢？** A：`try/except` 包住，把异常信息回灌给模型，让它自我纠正。

---

## 故事二：RAG 知识库问答管线

### 背景
想基于自己的本地文档（PDF/Word/ txt）做一个"只根据资料回答、不会胡说"的问答系统。

### 做法
- **向量库**：ChromaDB 持久化存储（`vectordb.py`）
- **文档加载**：`doc_loader.py` 支持 txt / PDF（PyPDF2）/ Word（python-docx）
- **文本切分**：`text_splitter.py` 实现 **3 种切分方法 + overlap**（chunk_size / overlap 可调），对比哪种检索更准
- **Embedding**：字符袋向量作离线兜底（计划要求接真实 Embedding API）
- **检索 + 生成**：`rag_v1.py` 检索 Top-K 相关块 → 拼成 Prompt（"只根据下面资料回答，资料没有就说不知道"）→ 交给 LLM
- **调参实验**：`experiment_report.py` 对比不同 `chunk_size` / `top_k` 的效果
- **工程化**：Dockerfile + docker-compose 容器化，GitHub Actions CI 自动跑测试

### 成果
- 完整 RAG 管线跑通，丢 3 个 PDF 能正确回答资料内问题
- 三种切分方法对比实验有数据支撑 (`实测：chunk_size=X 时命中率最优`)

### 亮点
> "RAG 不是调个库就完事。我对比了三种切分策略和 overlap 参数，发现切太碎会丢掉上下文、切太大检索不精准，最后用实验数据选了平衡点。而且我做了防幻觉约束——资料没有的答案直接说'未找到'。"

### 可能的追问 + 怎么答
- **Q：为什么不用真实 Embedding？** A：课程计划先用字符袋向量兜底保证离线可跑，真实 API 已在 requirements 里预留，换一行即可。
- **Q：怎么防止幻觉？** A：Prompt 明确要求"只根据资料"，且对检索结果为空的情况单独处理。
- **Q：ChromaDB 和 FAISS 怎么选？** A：ChromaDB 开箱即用、带持久化，适合原型；FAISS 性能更好但更底层，生产大规模会考虑。

---

## 故事三：Prompt 工程与结构化提取

### 背景
真实业务里经常要把**杂乱的非结构化文本**转成**结构化数据**（比如从一段描述里抽姓名/电话/地址），还要评估不同 Prompt 策略的效果。

### 做法
- **三种 Prompt 策略对比**：Zero-shot / Few-shot / Chain-of-Thought（`prompt_compare.py`）
- **结构化输出**：`info_extractor.py` 用 System Prompt 约束只输出 JSON，正则清洗 ```json 标记后 `json.loads`
- **调参**：`temperature=0` 保证提取稳定，`max_tokens` 控制长度
- **健壮性**：`llm_utils.py` 用 tenacity 做自动重试 + 流式输出优化体验
- **自动化评测**：`eval_report.py` 用 **10 条测试集**批量跑，断言提取结果是否等于期望值，输出准确率
- **模型对比**：同一任务对比 DeepSeek vs Qwen 的延迟与成本

### 成果
- 结构化提取在 10 条测试集上准确率 `(实测：X%)`
- 有可复现的评测脚本，不是"感觉效果还行"

### 亮点
> "Prompt 工程不是玄学。我用 10 条测试集做了自动化评测，Few-shot + CoT 比 Zero-shot 准确率明显更高；用 tenacity 解决 API 偶发失败，用流式输出优化前端体验。所有结论都有数据，不是拍脑袋。"

### 可能的追问 + 怎么答
- **Q：准确率怎么算的？** A：eval_report.py 跑 10 条 case，逐条比对提取结果和期望值，输出 correct/total。
- **Q：JSON 解析失败怎么办？** A：正则先去掉 ```json 标记，失败就记一次错误；生产环境会加 schema 校验和重试。
- **Q：Few-shot 例子怎么选？** A：覆盖典型格式（带标点、带破折号、中英文混排），提高鲁棒性。

---

## Day 6 模拟面试：手写 Agent 伪代码

> 面试官常让你白板写 Agent 核心循环。下面这份伪代码要能脱稿写出来。

```python
def agent_loop(query, tools, max_steps=5):
    messages = [
        {"role": "system", "content": build_prompt(tools)},  # 工具列表 + 角色
        {"role": "user",   "content": query},
    ]
    for step in range(max_steps):
        resp = llm_chat(messages)                 # 调 LLM
        if tool_call := parse_tool_call(resp):    # 解析：要调工具吗？
            try:
                result = execute_tool(tool_call)  # 执行工具
            except Exception as e:
                result = f"错误: {e}"             # 失败回灌模型
            messages.append({"role": "tool", "content": str(result)})
        else:
            return resp                          # 直接回答，结束
    return "超出最大步数"
```

**讲解要点（边写边说）：**
1. System Prompt 里塞工具定义，让模型知道能调什么
2. 循环里不断把"工具结果"追加进 messages，模型下一轮就能看到
3. `max_steps` 防止无限循环
4. 异常不崩溃，回灌给模型让它自我纠正

---

## 一句话总结（面试收尾用）
"我这个暑假从零做了一个完整 repo：手写 ReAct Agent + RAG 管线 + Prompt 工程评测，全程类型注解、pytest 测试、GitHub Actions CI 自动跑。比任何简历都有说服力。"
