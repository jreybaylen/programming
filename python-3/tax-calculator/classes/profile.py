from sys import path

path.append('..')

from abstract.profile import ProfileAbstract
from .tax import Tax

class Profile(ProfileAbstract, Tax):

    def get_information(self) -> None:
        self.first_name = input('Enter First Name: ')
        self.last_name = input('Enter Last Name: ')
        self.middle_name = input('Enter Middle Name: ')
        
        dependents = 0
        civil_status = None
        salary = input('Enter Salary: ')

        while civil_status not in [ 'S', 'M', 'W' ]:
            civil_status = input('Enter Civil Status [S/M/W]: ').upper()

        if not civil_status == 'S':
            dependents = int(input('Enter Dependents: '))

        self.salary = salary
        self.config({
            'salary': salary,
            'dependents': dependents,
            'civil_status': civil_status
        })

    def display_information(self) -> None:
        print()
        print('************************************************')
        print('Account Name: {}'.format(self.get_name()))
        print('Account Balance: P {:,.2f}'.format(
            float(self.salary)
        ))
        print('************************************************')

    def get_name(self) -> str:
        return '{l}, {f} {m}'.format(
            l=self.last_name,
            f=self.first_name,
            m=self.middle_name
        )

    def compute_tax(self, tax_type: str) -> None:
        dict(self.tax_config).update({
            'tax_type': tax_type
        })