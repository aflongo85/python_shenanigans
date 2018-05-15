
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Person:

    def __init__(self, name, surname, dob):
        self.name = name
        self.surname = surname
        self.dob = dob

    def get_info(self):

        age = relativedelta(datetime.today(), self.dob).years
        return ("{} {}, {} years old".format(self.name, self.surname, age))
