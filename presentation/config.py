from dataclasses import dataclass
from typing import Text


@dataclass
class APIConfig:
    host: Text
    port: int
