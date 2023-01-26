class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
    
    @property
    def name(self):
        return self._name
    
    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Число страниц должно быть задано целочисленным значением")
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным")
        self._pages = pages
        
        
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
    
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность аудиокниги должна быть задана числовым значением")
        if duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительной")
        self._duration = float(duration)
