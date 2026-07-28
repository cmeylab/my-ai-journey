from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key:str=""
    debug:bool=False
    model_config={"env_file":".env"}

settings=Settings()
print(f"API_KEY: {settings.api_key}")
print(f"DEBUG: {settings.debug}")
