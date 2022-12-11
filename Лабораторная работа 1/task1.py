import doctest
from typing import Union


# TODO Написать 3 класса с документацией и аннотацией типов
class Chair:
    def __init__(self, position: tuple, material: str, color: str):
        self.validate_position(position)
        if not isinstance(material, str) or not isinstance(color, str):
            raise TypeError("Характеристика предмета должна представлять собой строку")

        self.position = position
        self.material = material
        self.color = color

    @staticmethod
    def validate_position(position: tuple):
        if not isinstance(position, tuple):
            raise TypeError("Позиция должна быть задана кортежем")

        for coord in position:
            if not isinstance(coord, (int, float)):
                raise TypeError("Координаты должны быть числами")

    def move(self, new_pos: tuple):
        """
        Метод перемещает объект на новую позицию

        >>> chair = Chair((1, 1), "plastic", "white")
        >>> chair.move((1, 2.0))
        >>> chair.position == (1, 2.0)
        True
        >>> chair.move(("4", 2))
        Traceback (most recent call last):
            ...
        TypeError: Координаты должны быть числами

        :param new_pos: новая позиция объекта
        """

        self.validate_position(new_pos)
        self.position = new_pos

    def use(self):
        """
        Метод помечает объект как использующийся в данный момент,
        предотвращая его от дальнейшего взаимодействия с другими пользователями

        >>> chair = Chair((1, 1), "plastic", "white")
        >>> chair.use()
        """
        ...


class User:
    def __init__(self, username: str, password: str):
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if username.startswith((",", ".", "/", '\\')):
            raise ValueError("Имя пользователя не может начинаться с символов ,./\\")

        self.password = None
        self.update_password(password)
        self.username = username

    def update_password(self, new_password: str):
        """
        Метод изменяет текущее значение пароля пользователя

        >>> user = User("Кирилл", "1234")
        >>> user.update_password("12345678")
        >>> user.password == "12345678"
        True
        >>> user.update_password(12345678)
        Traceback (most recent call last):
            ...
        TypeError: Пароль должен быть строкой

        :param new_password: новый пароль
        """

        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой")
        if len(new_password) < 4 or len(new_password) > 255:
            raise ValueError("Длина пароля должна быть в диапазоне 4-255")

        self.password = new_password

    def get_user_data(self) -> tuple:
        """
        Метод вовзвращает данные о пользователе

        >>> user = User("Кирилл", "1234")
        >>> user.get_user_data()
        ('Кирилл', '1234')

        :return: кортеж, состоящий из имени пользователя и его пароля
        """

        return self.username, self.password


class Vector2D:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Координаты должны быть числами")

        self.x = x
        self.y = y

    def get_length(self) -> float:
        """
        Метод возвращает длину вектора

        >>> vector = Vector2D(3, 4)
        >>> vector.get_length()
        5.0
        """

        return (self.x ** 2 + self.y ** 2) ** 0.5

    def dot(self, other_vector) -> Union[int, float]:
        """
        Метод возвращает скалярное произведение двух векторов

        >>> vector = Vector2D(1, 1)
        >>> vector.dot(Vector2D(2, 2))
        4

        :param other_vector: вектор, на который производится умножение
        """

        if not isinstance(other_vector, Vector2D):
            raise TypeError("Один из умножаемых векторов не является объектом класса Vector2D")

        return self.x * other_vector.x + self.y * other_vector.y


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
