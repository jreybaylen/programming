from abc import ABC, abstractmethod

class TaxAbstract(ABC):

    @abstractmethod
    def config():
        pass

    @abstractmethod
    def take_home():
        pass