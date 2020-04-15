from shapely.geometry import (
    Point, asPoint,
    LineString, asLineString,
    Polygon, asPolygon,
    MultiPoint, asMultiPoint,
    MultiLineString, asMultiLineString,
    MultiPolygon, asMultiPolygon
)


def test_as_point():
    coords = [0, 0]
    geom = Point(coords)

    coords_adapter = asPoint(coords)
    geom_adapter = asPoint(geom)

    assert geom.wkt == coords_adapter.wkt
    assert geom.wkt == geom_adapter.wkt


def test_as_multipoint():
    l = LineString([(0, 0), (1, 1), (2, 2)])
    coords = l.coords
    mp = asMultiPoint(l)
    assert len(mp) == 3
    for idx, pt in enumerate(mp):
        coord = coords[idx]
        assert coord == (pt.x, pt.y)
