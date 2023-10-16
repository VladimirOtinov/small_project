class Articles:
    """
    Класс, представляющий статьи затрат.

    Attributes:
        code (int): Уникальный код статьи.
        name (str): Название статьи.
    """
    def __init__(self, code, name):
        """
        Инициализирует объект класса Articles.

        Args:
            code (int): Уникальный код статьи.
            name (str): Название статьи.
        """
        self.code = code
        self.name = name

    def __str__(self):
        """
        Возвращает строковое представление объекта класса Articles.

        Returns:
            str: Строковое представление статьи затрат.
        """
        return f"{self.code};{self.name}"
