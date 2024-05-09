import logging
from abc import ABCMeta, abstractmethod
from typing import List

from pvsnapshot.model import DataCatalog

_logger: logging.Logger = logging.getLogger(__name__)


class RemoteRepository(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> DataCatalog:
        pass

    @abstractmethod
    def put(self, data: DataCatalog):
        pass


class LocalRepository(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key: str) -> DataCatalog:
        pass

    @abstractmethod
    def put(self, data: DataCatalog):
        pass

    @abstractmethod
    def list(self) -> List[str]:
        pass