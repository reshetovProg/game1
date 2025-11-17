class Section:
    def __init__(self, name, max_count):
        self.__name = name
        self.__max_count = max_count

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} | {self.__max_count}"