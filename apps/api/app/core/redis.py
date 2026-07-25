from typing import Optional
import redis.asyncio as aioredis
from app.core.config import settings
from app.core.logging import logger

redis_client: Optional[aioredis.Redis] = None


async def get_redis_client() -> aioredis.Redis:
    global redis_client
    if redis_client is None:
        try:
            redis_client = aioredis.from_url(
                settings.REDIS_URL,
                encoding="utf-8",
                decode_responses=True
            )
            await redis_client.ping()
            logger.info("redis_connected", host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        except Exception as e:
            logger.warning("redis_connection_failed_fallback_mode", error=str(e))
            redis_client = None
    return redis_client


async def close_redis_connection():
    global redis_client
    if redis_client is not None:
        await redis_client.close()
        logger.info("redis_connection_closed")
        redis_client = None
