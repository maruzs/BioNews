import os
import json
import logging
import redis

log = logging.getLogger("bionews.cache")

class RedisCache:
    def __init__(self):
        self.host = os.getenv("REDIS_HOST", "redis").strip()
        self.port = int(os.getenv("REDIS_PORT", "6379").strip())
        self.password = os.getenv("REDIS_PASSWORD", None)  # None = sin contraseña (dev local)
        self.enabled = os.getenv("REDIS_ENABLED", "true").strip().lower() == "true"
        self.client = None
        if self.enabled:
            try:
                self.client = redis.Redis(
                    host=self.host,
                    port=self.port,
                    password=self.password or None,
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
            import datetime
            from decimal import Decimal
            def json_serializer(obj):
                if isinstance(obj, (datetime.datetime, datetime.date)):
                    return obj.isoformat()
                if isinstance(obj, Decimal):
                    return float(obj)
                raise TypeError(f"Type {type(obj)} not serializable")
            self.client.set(key, json.dumps(value, default=json_serializer), ex=expire_seconds)
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

    # ── JWT Blacklist (revocación de tokens) ─────────────────────────────────
    def blacklist_jti(self, jti: str, ttl_seconds: int = 60 * 60 * 24 * 31):
        """Agrega un JWT ID (jti) a la lista negra. TTL debe ser >= vida del token."""
        if not self.client:
            return
        try:
            self.client.set(f"blacklist:jti:{jti}", "1", ex=ttl_seconds)
        except Exception as e:
            log.error(f"Error agregando jti a blacklist: {e}")

    def is_jti_blacklisted(self, jti: str) -> bool:
        """Retorna True si el jti está en la lista negra (token revocado)."""
        if not self.client:
            return False
        try:
            return self.client.exists(f"blacklist:jti:{jti}") == 1
        except Exception as e:
            log.error(f"Error verificando blacklist: {e}")
            return False

    # ── User status cache (blocked check) ────────────────────────────────────
    def get_user_blocked(self, user_id: str):
        """Retorna el estado bloqueado del usuario desde caché (None = no en caché)."""
        if not self.client:
            return None
        try:
            val = self.client.get(f"user_blocked:{user_id}")
            if val is not None:
                return val == "1"
        except Exception:
            pass
        return None

    def set_user_blocked(self, user_id: str, blocked: bool, ttl_seconds: int = 60):
        """Cachea el estado bloqueado del usuario por 60 segundos."""
        if not self.client:
            return
        try:
            self.client.set(f"user_blocked:{user_id}", "1" if blocked else "0", ex=ttl_seconds)
        except Exception:
            pass

    def invalidate_user_blocked(self, user_id: str):
        """Invalida la caché de estado del usuario (ej. cuando se bloquea desde admin)."""
        if not self.client:
            return
        try:
            self.client.delete(f"user_blocked:{user_id}")
        except Exception:
            pass


cache = RedisCache()
