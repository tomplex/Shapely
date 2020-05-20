import pytest

from shapely.geometry import Polygon


@pytest.fixture()
def coords():
    return [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]


def test_normalize_simple(coords):
    p = Polygon(coords)
    assert p.normalize().equals(p)


def test_normalize(coords):
    p1 = Polygon(coords)
    p2 = Polygon(reversed(coords))
    p3 = p2.normalize()
    print(p1.wkt)
    print(p2.wkt)
    print(p3.wkt)
    assert p2.normalize().equals_exact(p1)
