from sys import path

path.append('..')

from abstract.tax import TaxAbstract

class Tax(TaxAbstract):
    def config(self, config: dict) -> None:
        self.tax_config = config

    def take_home(self) -> None:
        print()
        print(self.tax_config)
        print()