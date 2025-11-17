from Section import Section
class Person:
    __sections = set()

    def __init__(self, fio, phone):
        self.__fio = fio
        self.__phone = phone

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    def add_section(self, value):
        if isinstance(value, Section):
            self.__sections.add(value)

    def del_section(self, section_name):
        for i in self.__sections:
            if i.name == section_name:
                self.__sections.discard(i)
                break

    def __str__(self):
        result = ""
        for i in self.__sections:
            result += str(i) + "\n"
        return f"{self.__fio} - {self.__phone} \n{result}"


if __name__ == '__main__':
    person = Person("fio", "12563")
    section = Section("бокс", 23)
    section2 = Section("гребля", 23)
    person.add_section(section)
    person.add_section(section2)
    person.del_section("бокс")
    print(person)

