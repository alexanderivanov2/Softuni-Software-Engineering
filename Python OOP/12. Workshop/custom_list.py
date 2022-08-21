from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        try:
            self.__values.pop(index)
        except IndexError:
            raise IndexError("Invalid index")

    def get(self, index):
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError("Invalid index")

    def extend(self, object):
        try:
            some_object_iterator = iter(object)
            self.__values.extend(object)
        except TypeError:
            self.__values.append(object)

        return deepcopy(self.__values)

    def insert(self, index, value):
        if index >= len(self.__values) or index < 0:
            raise IndexError("Invalid index")
        self.__values.insert(index, value)
        return self.__values
