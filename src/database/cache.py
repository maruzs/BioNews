import os
import json
import logging
import redis

log = logging.getLogger("bionews.cache")

class RedisCache:
    def __init__(self):
        self.host = os.getenv("REDIS_HOST", "redis").strip()
        self.port = int(os.getenv("REDIS_PORT", "6379").strip())
        self.enabled = os.getenv("REDIS_ENABLED", "true").strip().lower() == "true"
        self.client = None
        if self.enabled:
            try:
                self.client = redis.Redis(
                    host=self.host,
                    port=self.port,
                    db=0,
                    socket_timeout=2.0,
                    decode_responses=True
                )
                self.client.ping()
                log.info(f"Conectado a Redis en {self.host}:{self.port}")
            except Exception as e:
                log.warning(f"No se pudo conectar a Redis: {e}. Caché desactivada.")
                self.client = None

    def get(self, key: str):
        if not self.client:
            return None
        try:
            val = self.client.get(key)
            if val:
                return json.loads(val)
        except Exception as e:
            log.error(f"Error leyendo de Redis: {e}")
        return None

    def set(self, key: str, value, expire_seconds=300):
        if not self.client:
            return
        try:
            self.client.set(key, json.dumps(value), ex=expire_seconds)
        except Exception as e:
            log.error(f"Error escribiendo en Redis: {e}")

    def delete(self, key: str):
        if not self.client:
            return
        try:
            self.client.delete(key)
        except Exception as e:
            log.error(f"Error borrando de Redis: {e}")

    def invalidate_pattern(self, pattern: str):
        if not self.client:
            return
        try:
            keys = self.client.keys(pattern)
            if keys:
                self.client.delete(*keys)
                log.info(f"Caché invalidada para patrón: {pattern} ({len(keys)} llaves)")
        except Exception as e:
            log.error(f"Error invalidando patrón en Redis: {e}")

cache = RedisCache()
