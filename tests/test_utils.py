from src.utils import calculate_taxes, get_day_name
import pytest

@pytest.fixture
def prices():
    return [10, 50, 150]

def test_calculate_taxes_correct(prices):
    assert calculate_taxes(prices, 10) == [11, 55, 165]

def test_calculate_taxes_wrong_tax(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, -5)

def test_calculate_taxes_wrong_price():
    with pytest.raises(ValueError):
        calculate_taxes([10, -50, 150], 10)


@pytest.mark.parametrize('day_number, expected', [(1, 'Monday'),
                                                  (2, 'Tuesday'),
                                                  (3, 'Wednesday'),
                                                  (5, 'Other day')])
def test_get_day_name(day_number, expected):
    assert get_day_name(day_number) == expected
