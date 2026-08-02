from collections.abc import Generator
from openai import OpenAI
from pydantic_settings import BaseSettings
from tenacity import retry,stop_after_attempt,wait_exponential

class Settings(BaseSettings):
    api_key:str=""
    model_config = {"env_file":".env"}
settings = Settings()
client = OpenAI(api_key=settings.api_key,base_url="https://api.deepseek.com")

@retry(stop=stop_after_attempt(3),wait=wait_exponential(multiplier=1,min=2,max=10))
def llm_chat(messages:list[dict],temperature:float=0.7)->str:
    resp = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""
@retry(stop=stop_after_attempt(3),wait=wait_exponential(multiplier=1,min=2,max=10))
def llm_chat_stream(messages:list[dict],temperature:float=0.7)->Generator[str,None,None]:
    stream = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        temperature=temperature,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content