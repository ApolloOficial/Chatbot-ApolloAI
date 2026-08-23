from __future__ import annotations

import redis

from app.services.redis_service import RedisSupport


def test_redis_uses_configurable_remote_timeout(monkeypatch):
    captured = {}
    client = object()

    def fake_from_url(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return client

    monkeypatch.setattr(redis.Redis, "from_url", fake_from_url)
    service = RedisSupport.from_config({
        "REDIS_URL": "rediss://default:secret@redis.example:6380/0",
        "REDIS_ENABLED": True,
        "REDIS_TIMEOUT_SECONDS": 5,
    })

    assert service._client is client
    assert captured["url"].startswith("rediss://")
    assert captured["socket_connect_timeout"] == 5
    assert captured["socket_timeout"] == 5
    assert captured["decode_responses"] is True
