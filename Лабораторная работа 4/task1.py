class Tetragon:
    def __init__(self, position: list[int], sides: list[int]):
        """
        Инициализация объекта класса Tetragon

        :param position: Положение объекта на экране в пикселях.
            Точка [0, 0] соответствует левому верхнему краю экрана
        :param sides: Список с длинами сторон четырехугольника
        """
        self.position = position
        self.sides = sides

    @property
    def position(self) -> list[int]:
        """Возвращает список координат четырехугольника"""
        return self._position

    @position.setter
    def position(self, pos: list[int]):
        """
        Валидация введенных данных для положения объекта

        :param pos: Положение объекта на экране в пикселях.
        Точка [0, 0] соответствует левому верхнему краю экрана
        """
        if not isinstance(pos, list):
            raise TypeError("Положение объекта должно задаваться списком")
        if len(pos) != 2:
            raise ValueError("Положение на экране должно задаваться двумя координатами")
        if not all(isinstance(coord, int) for coord in pos):
            raise TypeError("Координаты должны задаваться целым числом пикселей")
        self._position = pos

    @property
    def sides(self) -> list[int]:
        """Вовзвращает список сторон четырехугольника"""
        return self._sides

    @sides.setter
    def sides(self, sides: list[int]):
        """
        Валидация введенных данных для сторон четырехугольника

        :param sides: Список с длинами сторон четырехугольника
        """
        if not isinstance(sides, list):
            raise TypeError("Длины сторон задаются списком")
        if len(sides) != 4:
            raise ValueError("Длина списка сторон должна быть равна 4")
        if not all(isinstance(side, int) for side in sides):
            raise TypeError("Длина каждой стороны задается целым числом")
        self._sides = sides

    def perimeter(self) -> int:
        """
        Вычисление периметра четырехугольника

        :return: периметр четырехугольника
        """
        return sum(self.sides)

    def area(self):
        """
        Вычисление площади четырехугольника

        :raise NotImplementedError: если метод не был переопределен в дочернем классе
        """
        raise NotImplementedError("Не переопределен метод area базового класса Tetragon")

    def __str__(self):
        return f"{self.__class__.__name__} на позиции {self.position}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position!r}, {self.sides!r})"


class Square(Tetragon):
    def __init__(self, position: list[int], length: int):
        """
        Инициализация объекта класса Square

        :param position: Положение объекта на экране в пикселях.
            Точка [0, 0] соответствует левому верхнему краю экрана
        :param length: длина стороны квадрата в пикселях
        """
        super().__init__(position, [length] * 4)

    @property
    def length(self):
        """Возвращает длину стороны квадрата"""
        return self.sides[0]

    @length.setter
    def length(self, new_length: int):
        """
        Установка новой длины квадрата

        :param new_length: новое значение длины квадарата
        """
        self.sides = [new_length] * 4

    def area(self) -> int:
        """
        Вычисление площади квадрата

        :return: площадь квадрата
        """
        return self.length ** 2

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position!r}, {self.length!r})"


class Rectangle(Tetragon):
    def __init__(self, position: list[int], width: int, height: int):
        """
        Инициализация объекта класса Rectangle

        :param position: Положение объекта на экране в пикселях.
            Точка [0, 0] соответствует левому верхнему краю экрана
        :param width: ширина прямоугольника в пикселях
        :param height: высота прямоугольника в пикселях
        """
        super().__init__(position, [width, height, width, height])

    @property
    def width(self) -> int:
        """Возвращает ширину прямоугольника"""
        return self.sides[0]

    @width.setter
    def width(self, new_width):
        """
        Установка новой ширины прямоугольника

        :param new_width: новое значение ширины прямоугольника
        """
        self.sides = [new_width, self.height, new_width, self.height]

    @property
    def height(self) -> int:
        """Возвращает высоту прямоугольника"""
        return self.sides[1]

    @height.setter
    def height(self, new_height):
        """
        Установка новой высоты прямоугольника

        :param new_height: новое значение высоты прямоугольника
        """
        self.sides = [self.width, new_height, self.width, new_height]

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
    square = Square([4, 6], 2)
    print(square)
    print(repr(square))
    print(square.perimeter())
    print(square.area())

    rect = Rectangle([1, 6], 3, 4)
    print(rect)
    print(repr(rect))
    print(rect.perimeter())
    print(rect.area())
