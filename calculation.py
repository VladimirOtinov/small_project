class Calculation:
    """
    Класс, представляющий данные о затратах на изделие.

    Attributes:
        code (int): Уникальный код калькуляции.
        product_code (int): Код изделия.
        article_code (int): Код статьи затрат.
        amount (float): Сумма затрат.
    """
    def __init__(self, code, product_code, article_code, amount):
        """
        Инициализирует объект класса Calculation.

        Args:
            code (int): Уникальный код калькуляции.
            product_code (int): Код изделия.
            article_code (int): Код статьи затрат.
            amount (float): Сумма затрат.
        """
        self.code = code
        self.product_code = product_code
        self.article_code = article_code
        self.amount = amount

    def __str__(self):
        """
        Возвращает строковое представление объекта класса Calculation.

        Returns:
            str: Строковое представление данных о затратах на изделие.
        """
        return f"{self.code};{self.product_code};{self.article_code};{self.amount}"
