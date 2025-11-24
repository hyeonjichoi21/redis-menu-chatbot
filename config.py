from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    애플리케이션 전역 설정을 관리하는 클래스.

    - OPENAI_API_KEY: OpenAI API 키 (필수, .env에서 로딩)
    - REDIS_URL: Redis 접속 URL
    - OPENAI_MODEL: 사용할 OpenAI 모델 이름
    - CHAT_HISTORY_PREFIX: 대화 히스토리 Redis 키 prefix
    - USER_PROFILE_PREFIX: 유저 프로필 Redis 키 prefix
    - MAX_HISTORY: 불러올 최대 대화 히스토리 개수
    """

    OPENAI_API_KEY: str
    REDIS_URL: str = "redis://localhost:6379/0"

    OPENAI_MODEL: str = "gpt-4.1-mini"
    CHAT_HISTORY_PREFIX: str = "chat:history:"
    USER_PROFILE_PREFIX: str = "chat:profile:"
    MAX_HISTORY: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
