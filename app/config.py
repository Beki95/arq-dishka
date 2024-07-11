from dataclasses import dataclass

from infra.db.config import DBConfig
from infra.redis.config import REDISConfig
from presentation.config import APIConfig


@dataclass
class Config:
    api: APIConfig
    db: DBConfig
    redis: REDISConfig
