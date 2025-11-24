from typing import List, Dict
from openai import OpenAI
from ..config import settings
from ..redis_client import get_redis_client


class ChatService:
    """
    대화 관리 및 메뉴 추천의 핵심 비즈니스 로직을 담당하는 서비스.
    - Redis에 대화 및 유저 상태 저장
    - OpenAI를 활용한 메뉴 추천 생성
    """

    def __init__(self):
        self.redis = get_redis_client()
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def _get_user_history(self, user_id: str) -> List[Dict[str, str]]:
        """
        Redis에서 대화 히스토리를 조회한다.
        """
        key = settings.CHAT_HISTORY_PREFIX + user_id
        items = self.redis.lrange(key, -settings.MAX_HISTORY, -1)

        return [eval(item) for item in items] if items else []

    def _save_message(self, user_id: str, role: str, content: str):
        """
        Redis에 대화 메시지를 저장한다.
        """
        key = settings.CHAT_HISTORY_PREFIX + user_id
        self.redis.rpush(key, str({"role": role, "content": content}))

    def generate_reply(self, user_id: str, message: str) -> str:
        """
        1차 버전: 단순한 응답(에코 기반) 반환.
        이후 모델 프롬프트/메뉴 추천 로직은 점진적으로 추가한다.
        """
        # 대화 저장 (사용자 메시지)
        self._save_message(user_id, "user", message)

        # 간단한 응답 생성 (임시)
        reply = f"'{message}' 라고 하셨군요! 곧 메뉴 추천 기능이 추가될 예정이에요 :)"

        # 저장 (챗봇 응답)
        self._save_message(user_id, "assistant", reply)

        return reply
