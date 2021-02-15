class Human:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.salary = 0

    def description(self):
        print(f"{self.name} {self.age}")

    def __add__(self, other):
        return self.salary + other.salary



class Male(Human):

    def __init__(self,name,age):
        super().__init__(name,age)
        self.very_strong = True
        self.salary = 50000




class Female(Human):

    def __init__(self,name,age):
        super().__init__(name,age)
        self.very_beautiful = True
        self.salary = 6000000

    def description(self):
        print(f"{self.name} {self.age} WOMAN")


male1 = Male(name='steve',age=29)
female1 = Female(name='mary',age=29)


print(male1 + female1)



