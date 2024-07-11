from dataclasses import dataclass
from typing import Text


@dataclass
class REDISConfig:
    host: Text
    port: int
    database: int
    username: Text
    password: Text
