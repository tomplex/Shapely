import itertools

import pytest

from shapely import geometry
from tests.conftest import almost_equals_deprecated


@pytest.fixture()
def coords():
    return [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]


@pytest.fixture()
def simple_poly(coords):
    return geometry.Polygon(coords)


@pytest.fixture()
def reversed_poly(coords):
    return geometry.Polygon(reversed(coords))


@pytest.fixture()
def offset_poly(coords):
    coords = coords[1:] + [coords[1]]
    return geometry.Polygon(coords)


@almost_equals_deprecated
class TestPointEquality:
    def test_equals_exact(self):
        p1 = geometry.Point(1.0, 1.0)
        p2 = geometry.Point(2.0, 2.0)
        assert not p1.equals(p2)
        assert not p1.equals_exact(p2, 0.001)

    def test_almost_equals_default(self):
        p1 = geometry.Point(1.0, 1.0)
        p2 = geometry.Point(1.0 + 1e-7, 1.0 + 1e-7)  # almost equal to 6 places
        p3 = geometry.Point(1.0 + 1e-6, 1.0 + 1e-6)  # not almost equal
        assert p1.almost_equals(p2)
        assert not p1.almost_equals(p3)

    def test_almost_equals(self):
        p1 = geometry.Point(1.0, 1.0)
        p2 = geometry.Point(1.1, 1.1)
        assert not p1.equals(p2)
        assert p1.almost_equals(p2, 0)
        assert not p1.almost_equals(p2, 1)

    def test_almost_equals_deprecated(self):
        p1 = geometry.Point(1.0, 1.0)
        p2 = geometry.Point(1.0 + 1e-7, 1.0 + 1e-7)  # almost equal to 6 places
        with pytest.warns(FutureWarning, match="almost_equals"):
            p1.almost_equals(p2)


class TestPolygonEquality:
    def test_simple(self, simple_poly, reversed_poly, offset_poly):
        # All of these polygons have the same topological structure or "footprint"
        equals = [poly.equals(other) for poly, other in itertools.combinations(
                [simple_poly, reversed_poly, offset_poly], 2)]
        assert all(equals)

