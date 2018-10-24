class KolejkasNode:

    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_priority(self):
        return self.__priority

    def set_priority(self, priority):
        self.__priority = priority

    def to_string(self):
        return "Priorytet: {}, Zadanie: {}".format(self.__priority, self.__data)

    def __eq__(self, other):
        if self.__priority == other.get_priority():
            return 0
        elif self.__priority < other.get_priority():
            return -1
        elif self.__priority > other.get_priority():
            return 1


def priority_key(e: KolejkasNode):
    return e.get_priority()


class Kolejka:

    def __init__(self):
        self.__data = []*2000

    def empty(self):

        if self.__data is not []:
            return False
        else:
            return True

    def sort(self):
        self.__data.sort(key=priority_key)

    def enqueue(self, element):
        self.__data.append(element)

    def dequeue(self):
        return self.__data.pop(0)

