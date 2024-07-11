from dataclasses import dataclass


@dataclass
class DBConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
