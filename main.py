class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"{self.__name} | {self.__age}"

class Group:
    __students=set()
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        result = ""
        for i in self.__students:
            result += str(i)+"\n"
        return f"{self.__name} \n{result}"

    def add_student(self, value):
        if isinstance(value, Student):
            self.__students.add(value)

if __name__ == '__main__':
    st = Student("Vasia", 23)
    st2 = Student("Oleg", 23)
    group1 = Group("1a")
    group1.add_student(st)
    group1.add_student(st2)
    print(group1)
    print("1a\nvasia - 23\noleg - 67")