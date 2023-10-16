class ProductionPlan:
    """
    Класс, представляющий план выпуска изделий.

    Attributes:
        code (int): Уникальный код плана.
        product_code (int): Код изделия.
        quantity (int): Количество выпускаемых изделий.
    """
    def __init__(self, code, product_code, quantity):
        """
        Инициализирует объект класса ProductionPlan.

        Args:
            code (int): Уникальный код плана.
            product_code (int): Код изделия.
            quantity (int): Количество выпускаемых изделий.
        """
        self.code = code
        self.product_code = product_code
        self.quantity = quantity

    def __str__(self):
        """
        Возвращает строковое представление объекта класса ProductionPlan.

        Returns:
            str: Строковое представление плана выпуска изделий.
        """
        return f"{self.code};{self.product_code};{self.quantity}"
