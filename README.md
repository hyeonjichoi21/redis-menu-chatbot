# Redis Menu Chatbot

우테코 프리코스 오픈 미션으로 진행하는 **Redis 기반 메뉴 추천 챗봇**입니다.

## 📌 프로젝트 개요
Redis를 활용해 사용자의 대화 맥락과 취향을 기억하고,
OpenAI 모델을 통해 상황별 메뉴를 추천하는 챗봇입니다.
FastAPI + Redis + LLM 조합을 통해 비즈니스 로직 분리, 의존성 관리,
스트리밍 응답(SSE) 등 다양한 기술적 실험을 진행했습니다.

## 🔧 기술 스택

- FastAPI — 빠른 비동기 API 서버 개발
- Redis — 대화 메모리 및 사용자 상태 저장
- OpenAI API — 메뉴 추천 생성
- Python (3.13)
- Cursor — 생산성 향상을 위한 AI 개발 환경


## 📁 프로젝트 구조 (초안)

```
app/
├── main.py # API 엔드포인트
├── config.py # 환경 설정
├── redis_client.py # Redis 연결
├── dependencies.py # 의존성 주입
├── schemas.py # 요청/응답 DTO
└── services/
└── chat_service.py # 핵심 비즈니스 로직
```



## 📝 구현할 기능 목록 (초안)

- [x] FastAPI 서버 기본 구조 만들기
- [x] Redis 연결 설정하기
- [x] 채팅 API 기본 엔드포인트 만들기
- [X] 메뉴 추천 로직(예: OpenAI API 연동) 설계하기
- [ ] 대화 히스토리 및 유저 상태(기분/날씨/시간대) 저장 방식 고민하기
- [x] SSE 기반 스트리밍 엔드포인트 구현
- [ ] 대화 기록 구조 고도회
- [ ] 테스트 코드 작성 및 예외 케이스 검증 


