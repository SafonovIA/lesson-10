import pytest
import time


@pytest.fixture(scope="class")
def class_timer():
    print('\n', "Время начала (класс):", time.ctime(), '\n')
    yield None
    print('\n', "Время окончания (класс):", time.ctime(), '\n')


@pytest.fixture
def func_timer():
    print('\n', "Время начала (функция):", time.ctime(), '\n')
    yield None
    print('\n', "Время окончания (функция):", time.ctime(), '\n')
