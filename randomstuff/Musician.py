
from Person import Person


class Musician(Person):

    def __init__(self, name, surname, dob, **kwargs):
        super().__init__(name, surname, dob)
        self.instruments = kwargs

    def __get_info_about_instruments(self):

        dict_count = len(self.instruments)
        counter = 0

        instruments = "{} plays: ".format(self.name)
        for key, instr in self.instruments.items():
            instruments += "{}".format(instr)
            counter += 1

            if counter == dict_count:
                instruments += "."
            elif counter == dict_count - 1:
                instruments += " and "
            else:
                instruments += ", "

        return instruments

    def get_info(self):
        return super().get_info() + "\n" + self.__get_info_about_instruments()
