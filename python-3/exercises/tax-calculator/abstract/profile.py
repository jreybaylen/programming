from abc import ABC, abstractmethod

class ProfileAbstract(ABC):

    @abstractmethod
    def get_name():
        pass

    @abstractmethod
    def get_information():
        pass

    @abstractmethod
    def display_information():
        pass

    @abstractmethod
    def compute_tax():
        pass