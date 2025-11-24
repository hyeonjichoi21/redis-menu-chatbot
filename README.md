# Redis Menu Chatbot

우테코 프리코스 오픈 미션으로 진행한 **Redis 기반 메뉴 추천 챗봇** 프로젝트입니다.  
FastAPI, Redis, OpenAI API, SSE(Stream) 등 새로운 기술들을 직접 설계하고 적용하며  
"낯선 기술을 활용해 작은 결과물을 완성한다"는 오픈 미션의 취지에 맞춰 진행했습니다.

---

## 📌 프로젝트 개요

이 프로젝트는 **사용자의 대화 히스토리와 취향을 Redis에 저장**하고  
**OpenAI 모델을 활용해 실시간으로 메뉴를 추천**하는 챗봇 서비스입니다.

특히 다음 두 가지를 강조했습니다:

1. **비즈니스 로직과 API 로직의 분리**  
2. **SSE 기반 스트리밍 응답**을 이용한 자연스러운 실시간 답변 제공

또한, “배달의민족 스타일” UI의 간단한 프론트엔드를 직접 제작해  
백엔드-프론트엔드가 함께 동작하는 완전한 작은 서비스 형태로 완성했습니다.

---

## 🔧 기술 스택

- **FastAPI** — 비동기 Python API 서버
- **Redis** — 대화/상태 저장소
- **OpenAI API** — LLM 기반 메뉴 추천
- **SSE (Server-Sent Events)** — 실시간 스트리밍 응답
- **Python 3.13**
- **Cursor** — AI-assisted 개발 환경

---

## 📁 프로젝트 구조

```
app/
├── main.py            # API 엔드포인트(SSE/일반 응답)
├── config.py          # 환경 설정
├── redis_client.py    # Redis 연결
├── dependencies.py    # 의존성 주입 관리
├── schemas.py         # 요청/응답 DTO
└── services/
    └── chat_service.py   # 핵심 비즈니스 로직 (OpenAI + Redis)
frontend/
└── index.html         # 배민 스타일의 UI 샘플 페이지
```

---

## 📝 구현 기능 체크리스트

### ✔ 1단계 — 기본 서버 & 환경 구성
- [x] FastAPI 서버 구성
- [x] 환경 변수 및 settings 분리
- [x] Redis 연결 설정

### ✔ 2단계 — 기본 챗봇 기능
- [x] 채팅 API 기본 엔드포인트 구현
- [x] OpenAI 모델을 이용한 메뉴 추천 로직 구현
- [x] 대화 저장용 Redis 리스트 구조 설계

### ✔ 3단계 — 스트리밍 & UX 개선
- [x] SSE 기반 스트리밍 엔드포인트 구현
- [x] 프론트엔드 UI 제작 (배민 스타일 챗 UI)
- [x] 토큰 단위 실시간 답변 렌더링

### ⏳ 4단계 — 확장 및 리팩토링 (추후 진행)
- [ ] 대화 히스토리 구조 고도화
- [ ] 사용자 상태(기분/날씨/시간대) 이용 개선
- [ ] 테스트 코드 작성 및 예외 처리 확장

---

## 🚀 실행 방법

### 1) Redis 실행
Windows(Winget 설치 기준)
```
redis-server
```

### 2) FastAPI 서버 실행
```
uvicorn app.main:app --reload
```

### 3) 프론트엔드 열기
`frontend/index.html` 파일을 브라우저로 열어 직접 챗봇을 사용해볼 수 있습니다.

---

## 🙌 프로젝트 목표 & 회고 요약

이번 오픈 미션에서 가장 큰 목표는 **새로운 기술을 직접 선택하고**,  
**0에서 기능을 설계하여 완성까지 이끌어 보는 경험**이었습니다.

- Redis를 처음 설치하고 설정하며 많은 시행착오를 겪었고
- pydantic 버전 차이 문제, config import 충돌, Windows Redis 충돌 등 여러 문제도 직접 해결했습니다
- SSE 스트리밍은 생소했지만 성공적으로 구현해 자연스러운 대화 흐름을 만들었습니다
- Cursor를 적극 활용해 리팩토링, 파일 구조 개선, 빠른 개발 작업을 효율화했습니다

“낯선 기술을 붙잡고 끝까지 동작하게 만든 경험”이 이번 미션의 핵심 성과였습니다.

---

## 📎 저장소

GitHub Repository  
👉 *https://github.com/hyeonjichoi21/redis-menu-chatbot*

