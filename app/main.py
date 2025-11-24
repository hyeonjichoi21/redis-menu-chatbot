from fastapi import FastAPI, Depends

from .dependencies import get_chat_service
from .schemas import ChatRequest, ChatResponse
from .services.chat_service import ChatService

app = FastAPI(
    title="Redis Menu Chatbot",
    description="Redis와 OpenAI를 활용한 메뉴 추천 챗봇 API",
    version="0.1.0",
)


@app.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    """
    기본 채팅 엔드포인트.

    - 요청으로부터 user_id와 message를 받아서
    - ChatService에 위임하여 응답 메시지를 생성하고
    - ChatResponse 형태로 반환한다.
    """
    reply = chat_service.generate_reply(user_id=request.user_id, message=request.message)
    return ChatResponse(reply=reply)
