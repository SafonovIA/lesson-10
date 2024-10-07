# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture()
def print_id(request):
    marker = request.node.get_closest_marker("id_check")
    if marker:
        print(*marker.args)


@pytest.mark.id_check(1, 2, 3)
def test(print_id):
    pass
