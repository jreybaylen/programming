from abc import ABC, abstractmethod

class TaxAbstract(ABC):

    @abstractmethod
    def config():
        pass

    @abstractmethod
    def monthly():
        pass

    @abstractmethod
    def yearly():
        pass

    @abstractmethod
    def take_home():
        pass