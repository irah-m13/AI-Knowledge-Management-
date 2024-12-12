from abc import ABC, abstractmethod

class BaseRecord(ABC):
    @abstractmethod
    def save(self):
        pass
