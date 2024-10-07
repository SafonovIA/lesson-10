# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0, 12, 2)



def test_normal_data():
    assert all_division(5, 3, 32, 2) == 0.026041666666666668


def test_by_one():
    assert all_division(1, 1, 1, 1) == 1


def test_big_data():
    assert all_division(10000, 1234321, 5412344, 597846571) == 2.503783352986916e-18


@pytest.mark.smoke
def test_by_zero():
    assert all_division(0, 1, 2, 63) == 0

