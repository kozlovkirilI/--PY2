from math import pi


class Figure:
    def __init__(self, position: list[int]):
        """
        Инициализация объекта класса Figure

        :param position: Положение объекта на экране в пикселях.
            Точка [0, 0] соответствует левому верхнему краю экрана
        """
        self.position = position

    @property
    def position(self) -> list[int]:
        return self._position

    @position.setter
    def position(self, pos: list[int]):
        """Валидация введенных данных для положения объекта"""
        if not isinstance(pos, list):
            raise TypeError("Положение объекта должно задаваться списком")
        if len(pos) != 2:
            raise ValueError("Положение на экране должно задаваться двумя координатами")
        if not all(isinstance(coord, int) for coord in pos):
            raise TypeError("Координаты должны задаваться целым числом пикселей")
        self._position = pos

    @property
    def area(self):
        """
        Вычисление площади фигуры

        :raise NotImplementedError: если метод не был переопределен в дочернем классе
        """
        raise NotImplementedError("Не переопределен метод area базового класса Figure")

    def __str__(self):
        return f"{self.__class__.__name__} на позиции {self.position}"

    # Замечание о том, что для абстрактного класса repr можно не создавать видел,
    # но раз уж в задании сказано сделать - делаю
    def __repr__(self):
        return f"{self.__class__.__name__}({self.position!r})"


class Circle(Figure):
    def __init__(self, position: list[int], radius: int):
        """
        Инициализация объекта класса Figure

        :param position: Положение объекта на экране в пикселях.
            Точка [0, 0] соответствует левому верхнему краю экрана
        :param radius: радиус окружности в пикселях
        """
        super().__init__(position)
        self.radius = radius

    @property
    def area(self) -> float:
        """
        Вычисление площади круга

        :return: площадь круга
        """
        return pi * (self.radius ** 2)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position!r}, {self.radius!r})"


class Rectangle(Figure):
    def __init__(self, position: list[int], width: int, height: int):
        """
        Инициализация объекта класса Figure

        :param position: Положение объекта на экране в пикселях.
            Точка [0, 0] соответствует левому верхнему краю экрана
        :param width: ширина прямоугольника в пикселях
        :param height: высота прямоугольника в пикселях
        """
        super().__init__(position)
        self.height = height
        self.width = width

    @property
    def area(self) -> int:
        """
        Вычисление площади прямоугольника

        :return: площадь прямоугольника
        """
        return self.width * self.height

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position!r}, {self.width!r}, {self.height!r})"


if __name__ == "__main__":
    # Write your solution here
    circle = Circle([4, 6], 2)
    print(circle)
    print(repr(circle))
    print(circle.area)

    rect = Rectangle([1, 6], 3, 4)
    print(rect)
    print(repr(rect))
    print(rect.area)
