import redis
from functools import lru_cache
from .config import settings


@lru_cache()
def get_redis_client() -> redis.Redis:
    """
    Redis 클라이언트를 싱글톤처럼 재사용하기 위해 LRU 캐시 적용.
    - 우테코 가이드의 '하드코딩 금지', '구조적 설계' 충족
    """

    return redis.Redis.from_url(
        settings.REDIS_URL,
        decode_responses=True  # 문자열을 자동으로 str로 반환
    )
