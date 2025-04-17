class MyClass:
    def __init__(self, variable1 = None, variable2 = None):
        if variable1 is not None and variable2 is not None:
            self.variable1 = variable1
            self.variable2 = variable2
        else:
            self.variable1 = "значение по умолчанию 1: New value"
            self.variable2 = "значение по умолчанию 2: 643"
        print(f"создан объект: {self.variable1}, {self.variable2}")

    def __del__(self):
        print(f"объект удален: {self.variable1}, {self.variable2}")

    def show_variable(self):
        print(f"текущие свойства объекта: {self.variable1}, {self.variable2}")

object1 = MyClass("Hello", 123)
object1.show_variable()

object2 = MyClass()
object2.show_variable()

del object1
del object2