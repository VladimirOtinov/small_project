from product import Product
from articles import Articles
from calculation import Calculation
from production_plan import ProductionPlan

# Создаем пустые списки для хранения объектов
products = []
articles = []
calculations = []
production_plans = []

# Чтение данных из текстовых файлов и создание объектов

# Чтение и создание объектов из файла product.txt
with open('product.txt', 'r', encoding='utf-8') as product_file:
    for line in product_file:
        code, name = line.strip().split(';')
        products.append(Product(int(code), name))

# Чтение и создание объектов из файла articles.txt
with open('articles.txt', 'r', encoding='utf-8') as articles_file:
    for line in articles_file:
        code, name = line.strip().split(';')
        articles.append(Articles(int(code), name))

# Чтение и создание объектов из файла calculation.txt
with open('calculation.txt', 'r', encoding='utf-8') as calculation_file:
    for line in calculation_file:
        code, product_code, article_code, amount = line.strip().split(';')
        calculations.append(Calculation(int(code), int(product_code), int(article_code), float(amount)))

# Чтение и создание объектов из файла production_plan.txt
with open('production_plan.txt', 'r', encoding='utf-8') as production_plan_file:
    for line in production_plan_file:
        code, product_code, quantity = line.strip().split(';')
        production_plans.append(ProductionPlan(int(code), int(product_code), int(quantity)))

# Решение задачи
total_cost = 0
article_costs = {article.code: 0 for article in articles}

# Рассчитываем суммарную себестоимость выпуска изделий по плану
for plan in production_plans:
    product_code = plan.product_code
    quantity = plan.quantity

    for calculation in calculations:
        if calculation.product_code == product_code:
            article_code = calculation.article_code
            amount = calculation.amount
            total_cost += amount * quantity
            article_costs[article_code] += amount * quantity

# Вывод суммарной себестоимости и доли каждой статьи затрат

# Вывод суммарной себестоимости
print(f"\nСуммарная себестоимость выпуска: {total_cost}\n")

# Рассчитываем и выводим долю каждой статьи затрат в общей себестоимости
for article in articles:
    article_code = article.code
    cost = article_costs[article_code]
    total_article_cost = sum(article_costs.values())
    share = (cost / total_article_cost) * 100
    print(f"Доля статьи {article.name} в общей себестоимости: {share:.2f}%")
