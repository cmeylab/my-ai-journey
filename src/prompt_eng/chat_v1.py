from openai import OpenAI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key=""
    model_config = {"env_file": ".env"}

settings = Settings()
client = OpenAI(api_key=settings.api_key,base_url="https://api.deepseek.com")

resp=client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role":"user","content":"你好"}]
)
print(resp.choices[0].message.content)