class Product:
    """
    Класс, представляющий изделия.

    Attributes:
        code (int): Уникальный код изделия.
        name (str): Название изделия.
    """
    def __init__(self, code, name):
        """
        Инициализирует объект класса Product.

        Args:
            code (int): Уникальный код изделия.
            name (str): Название изделия.
        """
        self.code = code
        self.name = name

    def __str__(self):
        """
        Возвращает строковое представление объекта класса Product.

        Returns:
            str: Строковое представление изделия.
        """
        return f"{self.code};{self.name}"
