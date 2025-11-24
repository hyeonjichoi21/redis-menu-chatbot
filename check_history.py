import json
import redis

# Redis 연결
r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

# 사용자 ID
USER_ID = "demo-user-1"

# 밑줄 주의: chat:history:{user_id}
key = f"chat:history:{USER_ID}"

# Redis에서 전체 대화기록 가져오기
history = r.lrange(key, 0, -1)

print("\n=== Redis Conversation History ===\n")

for idx, item in enumerate(history, 1):
    try:
        msg = json.loads(item)
        print(f"{idx}. [{msg['role']}] {msg['content']}")
    except Exception as e:
        print(f"{idx}. [INVALID JSON] {item}")

print("\n=== END ===")
