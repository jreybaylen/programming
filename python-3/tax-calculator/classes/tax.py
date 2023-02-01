from sys import path

path.append('..')

from abstract.tax import TaxAbstract

class Tax(TaxAbstract):
    def config(self, config) -> None:
        self.config = config

    def monthly(self):
        pass

    def yearly(self):
        pass

    def take_home(self):
        print()
        print(self.config)
        print()