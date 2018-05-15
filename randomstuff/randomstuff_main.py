
from array import *
from collections import namedtuple
from datetime import date

from Musician import *
from Analiser import *

'''
my_unnamed_tuple = (1, 2)
print(my_unnamed_tuple[0])
'''

name = "named_tuple"
fields = 'first second third'
AFLNamedTuple = namedtuple(name, fields)

myTuple = AFLNamedTuple("Andrea", "Filippo", "Longo")
print(myTuple.first)
print(myTuple.third)

my_dictionary = dict({"name": "Dylan", "surname": "Dog"})
print(my_dictionary["name"])


my_array = array('l', [1, 2, 3, 4, 5, 6, 7, 8])

for x in my_array:
    print(x*2)

print(my_array*3)


for x in my_array*2:
    print(x*2)

a_list = [1, 4, 7, "A", "B"]

for x in a_list:
    if isinstance(x, int):
        print("this is an int")
        print(x)
    elif isinstance(x, str):
        print("this is an string")
        print(x)


def a_switch(variable):
    if variable < 1 or variable > 3:
        return "!#! {} is out of bounds !#!".format(variable)
    return dict({
        1: "One",
        2: "Two",
        3: "Three"
    })[variable]

print(a_switch(5))
print(a_switch(2))

#interesting stuff about dictionary
somedict = dict({"Hello": "Nora"})
print(somedict.get("Salut"))
print(somedict.get("CIAO", "No result"))
print(somedict.get("Hello"))

def a_better_switch(variable):
    return {
        1: "One",
        2: "Two",
        3: "Three"
    }.get(variable, "{} is an unknown key".format(variable)) #this is the way to provide a default value

print(a_better_switch(1))
print(a_better_switch(2))
print(a_better_switch(5))

#instruments = dict({"first": "guitar", "second": "bass", "third": "drums"})
#andrea = Musician("Andrea", "Longo", date(1985, 5, 17), **instruments)
andrea = Musician("Andrea", "Longo", date(1985, 5, 17), first="guitar", second="bass", third="drums")

#print(andrea.get_info_about_instruments())
print("FIRST INSTRUMENT = {}".format(andrea.instruments.get("first")))
print(andrea.get_info())

tizio = Person("Tizio", "Pulvirenti", date(2000, 12, 25))
print(tizio.get_info())


Analiser().ig_analysis(date(2011, 2, 21), date.today(), 1673)