def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        taxed_prices.append(calculate_tax(price, tax_rate))

    return taxed_prices

def calculate_tax(price: float, tax_rate: float) -> float:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    if price <= 0:
        raise ValueError('Неверная цена')

    tax = price * tax_rate / 100

    return price + tax


def get_day_name(day_num):
    if day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return 'Wednesday'
    else:
        return 'Other day'



result = calculate_taxes([10,50,150], 10)
print(result)

print(calculate_tax(10, 10))
