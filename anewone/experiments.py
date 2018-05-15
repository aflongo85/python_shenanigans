

def testfunction(*args, **kwargs):
    print(args)
    print(kwargs)

    # Iteration on args and kwargs examples
    # for thing in args:
    #     print(thing)
    #
    # for key, value in kwargs.items():
    #     print(value)


testfunction("Andrea", "Filippo", "Longo", age=33, gender="male")
testfunction(["A", "b", "c"], my_key="psswrd", my_value="Qwerty1234!")


class Lockable:

    __is_locked = False

    def __setattr__(self, key, value):
        if self.__is_locked and not hasattr(self, key):
            print("cannot set {} attribute".format(key))
            #raise TypeError("%r is a frozen class" % self)
        else:
            object.__setattr__(self, key, value)

    def lock(self):
        self.__is_locked = True


class Person(Lockable):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


a_person = Person("Andrea", "Wrongo")
a_person.lock()
a_person.age = 18
a_person.surname = "Longo"
print (a_person.surname)


# Ternary operator in Python! -------
x = 1
y = x if x > 10 else 15
print(y)
# -----------------------------------



#DUCK TYPING ---------------------------


class Duck:

    def help(self):
        print("QUAAAAAACK!")


class Person:

    def help(self):
        print("HEEEEEEELP!")


class Car:

    def turnOn(self):
        print("wrooooooom")



def ask_for_help(living_being):

    try:
        living_being.help()
    except AttributeError:
        print("???????? could not invoke help")


donald = Duck()
mario = Person()
lambo = Car()

ask_for_help(donald)
ask_for_help(mario)
ask_for_help(lambo)
