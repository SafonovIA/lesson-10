# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import pytest


@pytest.fixture(autouse=True)
def setup_class(class_timer):
    pass

class TestClass:

    def test_1(self):
        assert True

    def test_2(self, func_timer):
        assert True

    def test_3(self):
        assert True