class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Я не знаю кто я!'

class Dog(Animal):
    def speak(self):
        return 'Я собака!'

class Cat(Animal):
    def speak(self):
        return 'Я кот!'

animal = Animal("Неизвестное животное")
dog = Dog("Шарик")
cat = Cat("Мурзик")

print(animal.speak())
print(dog.speak())
print(cat.speak())