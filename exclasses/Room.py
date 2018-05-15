
#from Lockable import Lockable

class Room: #(Lockable):

    def __init__(self, number, number_of_beds, daily_rate, has_fridge=True, has_aircon=True, is_booked=False,
                 client_name="NONE"):

        self.number = number
        self.number_of_beds = number_of_beds
        self.has_fridge = has_fridge
        self.has_aircon = has_aircon
        self.is_booked = is_booked
        self.client_name = client_name
        self.daily_rate = daily_rate
        self.__debt = 0

    def book(self, number_of_days):
        if self.is_booked or number_of_days <= 0:
            # return exception
            print("Room {} is already booked.".format(self.number))
            return

        self.is_booked = True
        self.charge(self.daily_rate * number_of_days)

    def info(self):
        status_info = ""
        if self.is_booked:
            status_info = "booked - Total debt = {}".format(self.__debt)
        else:
            status_info = "available"

        print("Room {} is {}".format(self.number, status_info))


    def charge(self, amount):

        if not self.is_booked:
            # return exception
            print("Room {} is not booked.".format(self.number))
            return

        self.__debt += amount
        if self.__debt > 0:
            print("Room {} Total debt = {}".format(self.number, self.__debt))

    def pay(self, amount):

        if not self.is_booked:
            # return exception
            print("Room {} is not booked.".format(self.number))
            return

        self.__debt -= amount

        if self.__debt > 0:
            print("Room {} remaining debt = {}".format(self.number, self.__debt))
        elif self.__debt < 0:
            print("Room {} Surplus paid = {}".format(self.number, self.__debt))
        else:
            print("Room {} Total amount paid".format(self.number))

    def get_debt(self):
        return self.__debt







