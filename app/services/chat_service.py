import json
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
        JSON 문자열로 저장된 데이터를 파싱해 role/content 리스트로 복원한다.
        """
        key = settings.CHAT_HISTORY_PREFIX + user_id
        items = self.redis.lrange(key, -settings.MAX_HISTORY, -1)
        if not items:
            return []

        history = []
        for item in items:
            try:
                history.append(json.loads(item))
            except json.JSONDecodeError:
                # 잘못 저장된 값이 있더라도 전체 흐름은 깨지지 않도록 방어
                continue
        return history

    def _save_message(self, user_id: str, role: str, content: str):
        """
        Redis에 대화 메시지를 JSON 문자열로 저장한다.
        """
        key = settings.CHAT_HISTORY_PREFIX + user_id
        payload = {"role": role, "content": content}
        self.redis.rpush(key, json.dumps(payload))

    def _build_messages(self, user_id: str, message: str) -> List[Dict[str, str]]:
        """
        OpenAI에 전달할 messages 리스트를 생성한다.
        - system 프롬프트
        - 과거 대화 히스토리
        - 현재 사용자 메시지
        """
        history = self._get_user_history(user_id)

        system_prompt = (
            "당신은 한국 사용자에게 오늘 먹을 메뉴를 추천해주는 챗봇입니다. "
            "사용자의 대화 맥락을 기억하고, 기분과 상황(시간대, 날씨 등)을 고려해 "
            "한두 가지 메뉴를 자연스러운 한국어로 추천해 주세요. "
            "추천 이유도 짧게 덧붙여 주세요."
        )

        messages: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt},
        ]

        # 과거 대화 히스토리 추가
        messages.extend(history)

        # 현재 사용자 메시지 추가
        messages.append({"role": "user", "content": message})

        return messages

    def generate_reply(self, user_id: str, message: str) -> str:
        """
        OpenAI Chat Completions API를 사용해 메뉴 추천 응답을 생성한다.
        """
        # 현재 사용자 메시지를 먼저 저장
        self._save_message(user_id, "user", message)

        messages = self._build_messages(user_id, message)

        try:
            completion = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=messages,
            )
            reply = completion.choices[0].message.content.strip()
        except Exception:
            # 모델 호출 실패 시 기본 안내 응답
            reply = "메뉴를 추천하는 중 문제가 발생했어요. 잠시 후 다시 시도해 주세요!"

        # 챗봇 응답도 히스토리에 저장
        self._save_message(user_id, "assistant", reply)

        return reply
