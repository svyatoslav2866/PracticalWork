x = int(input("введите координаты для точки x"))
y = int(input("введите координаты для точки y"))
radius = int(input("введите радиус круга:"))

def point(x, y, radius):
    distance = (x**2 + y**2) <= radius**2
    return distance

if point(x, y, radius):
    print(f"Точка {x}, {y} принадлежит кругу с радиусом {radius}")
else:
    print(f"Точка {x}, {y} не принадлежит кругу с радиусом {radius}")