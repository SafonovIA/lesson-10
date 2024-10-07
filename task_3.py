# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a, b, c, d, result", [
    pytest.param(1, 0, 12, 2, Exception, marks=pytest.mark.skip("zero_error")),
    pytest.param(0, 1, 2, 63, 0, marks=pytest.mark.smoke("smoke")),
    pytest.param(5, 3, 32, 2, 0.026041666666666668),
    pytest.param(1, 1, 1, 1, 1),
    pytest.param(10000, 1234321, 5412344, 597846571, 2.503783352986916e-18),
])
def test(a, b, c, d, result):
    assert  all_division(a, b, c, d) == result
