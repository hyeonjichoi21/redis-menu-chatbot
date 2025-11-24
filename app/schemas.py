from typing import Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    채팅 요청 DTO.

    - user_id: 유저를 구분하기 위한 식별자 (필수)
    - message: 사용자가 보낸 메시지 (필수)
    - mood: 현재 기분 (선택)
    - weather: 현재 날씨 (선택)
    - time_of_day: 시간대 (예: 아침, 점심, 저녁, 야식) (선택)
    """

    user_id: str = Field(..., description="유저 식별자")
    message: str = Field(..., description="사용자 채팅 메시지")
    mood: Optional[str] = Field(None, description="유저의 현재 기분")
    weather: Optional[str] = Field(None, description="현재 날씨")
    time_of_day: Optional[str] = Field(None, description="현재 시간대 (아침/점심/저녁/야식 등)")


class ChatResponse(BaseModel):
    """
    채팅 응답 DTO.

    - reply: 챗봇이 사용자에게 반환하는 메시지
    """

    reply: str = Field(..., description="챗봇 응답 메시지")
