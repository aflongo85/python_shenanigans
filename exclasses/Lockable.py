
class Lockable:

    __is_locked = True

    def __setattr__(self, key, value):
        if self.__is_locked and not hasattr(self, key):
            print ("!!! - it's not possibile to set {} attribute - !!!".format(key))
        else:
            object.__setattr__(self, key, value)

    def unlock(self):
        self.__is_locked = False