from functools import lru_cache

from .services.chat_service import ChatService


@lru_cache()
def get_chat_service() -> ChatService:
    """
    ChatService 인스턴스를 제공하는 의존성 주입 함수.

    FastAPI의 Depends와 함께 사용되며,
    애플리케이션 전역에서 하나의 ChatService 인스턴스를 재사용한다.
    """
    return ChatService()
