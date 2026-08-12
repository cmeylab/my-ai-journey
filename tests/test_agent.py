import json

import pytest

from src.agent import agent_v1


def make_replies(*texts: str):
    calls = {"n": 0}

    def fake_ask_llm(messages: list) -> str:
        reply = texts[calls["n"]]
        calls["n"] += 1
        return reply

    return fake_ask_llm


def test_scene1_tool_call(monkeypatch):
    monkeypatch.setattr(
        agent_v1, "ask_llm",
        make_replies(
            '调用工具: {"name": "calculator", "arg": {"expression": "3+5*2"}}',
            "答案是 13",
        ),
    )
    result = agent_v1.agent_run("3+5*2")
    assert "13" in result


def test_scene2_direct_answer(monkeypatch):
    monkeypatch.setattr(agent_v1, "ask_llm", make_replies("你好呀"))
    result = agent_v1.agent_run("你好")
    assert result == "你好呀"


def test_scene3_unknown_tool(monkeypatch):
    monkeypatch.setattr(
        agent_v1, "ask_llm",
        make_replies(
            '调用工具: {"name": "xxx", "arg": {}}',
            "没有这个工具，我直接回答",
        ),
    )
    result = agent_v1.agent_run("调用一个不存在的工具")
    assert "未知工具" in result or "直接回答" in result


def test_scene4_bad_format(monkeypatch):
    monkeypatch.setattr(
        agent_v1, "ask_llm",
        make_replies("调用工具: {{{坏格式", "重试后正常回答"),
    )
    result = agent_v1.agent_run("说句怪话")
    assert "重试后正常回答" in result


def test_scene5_time_tool(monkeypatch):
    monkeypatch.setattr(
        agent_v1, "ask_llm",
        make_replies(
            '调用工具: {"name": "get_current_time", "arg": {}}',
            "现在的时间是：2026-08-07 12:00:00",
        ),
    )
    result = agent_v1.agent_run("现在几点")
    assert "2026" in result
