from abc import (
    ABC,
    abstractmethod,
)
from typing import Text


class ISession(ABC):

    @abstractmethod
    def get_a(self) -> Text: ...
