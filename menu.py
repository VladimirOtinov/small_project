from product import Product
from articles import Articles
from calculation import Calculation
from production_plan import ProductionPlan

# Функции для каждой опции меню

def show_product_list(products):
    for product in products:
        print(f"{product.code}. {product.name}")

def show_articles_list(articles):
    for article in articles:
        print(f"{article.code}. {article.name}")

def calculate_total_cost(calculation, production_plan):
    total_cost = 0
    for plan in production_plan:
        for calc in calculation:
            if plan.product_code == calc.product_code:
                total_cost += calc.amount * plan.quantity
    print(f"Суммарная себестоимость выпуска: {total_cost:.2f}")

def calculate_article_share(calculation, articles, production_plan):
    article_costs = {article.code: 0 for article in articles}
    total_cost = 0

    for plan in production_plan:
        for calc in calculation:
            if plan.product_code == calc.product_code:
                article_costs[calc.article_code] += calc.amount * plan.quantity
                total_cost += calc.amount * plan.quantity

    for article in articles:
        share = (article_costs[article.code] / total_cost) * 100
        print(f"Доля статьи {article.name} в общей себестоимости: {share:.2f}%")

# Главное меню
def main_menu():
    print("\nГлавное меню")
    print("1. Показать список изделий")
    print("2. Показать список статей затрат")
    print("3. Рассчитать суммарную себестоимость выпуска")
    print("4. Рассчитать долю статей затрат в общей себестоимости")
    print("5. Выход")

# Функции для опций меню
def option1(products):
    show_product_list(products)

def option2(articles):
    show_articles_list(articles)

def option3(calculation, production_plan):
    calculate_total_cost(calculation, production_plan)

def option4(calculation, articles, production_plan):
    calculate_article_share(calculation, articles, production_plan)

# Загрузка данных из текстовых файлов и создание объектов
def load_data_from_files():
    products = []
    articles = []
    calculation = []
    production_plan = []

    # Загрузка данных из текстовых файлов и создание объектов
    with open("product.txt", "r", encoding='utf-8') as products_file:
        for line in products_file:
            code, name = line.strip().split(";")
            products.append(Product(int(code), name))

    with open("articles.txt", "r", encoding='utf-8') as articles_file:
        for line in articles_file:
            code, name = line.strip().split(";")
            articles.append(Articles(int(code), name))

    with open("calculation.txt", "r", encoding='utf-8') as calculation_file:
        for line in calculation_file:
            code, product_code, article_code, amount = line.strip().split(";")
            calculation.append(Calculation(int(code), int(product_code), int(article_code), float(amount)))

    with open("production_plan.txt", "r", encoding='utf-8') as production_plan_file:
        for line in production_plan_file:
            code, product_code, quantity = line.strip().split(";")
            production_plan.append(ProductionPlan(int(code), int(product_code), int(quantity)))

    return products, articles, calculation, production_plan

if __name__ == '__main__':
    products, articles, calculation, production_plan = load_data_from_files()

    while True:
        main_menu()
        choice = input("\nВыберите опцию (1/2/3/4/5): ")
        if choice == '1':
            option1(products)
        elif choice == '2':
            option2(articles)
        elif choice == '3':
            option3(calculation, production_plan)
        elif choice == '4':
            option4(calculation, articles, production_plan)
        elif choice == '5':
            print("\nПрограмма завершена.")
            break
        else:
            print("\nНеверный выбор. Пожалуйста, выберите опцию снова.")
