import geopy
import geojsoncontour
import geopandas as gpd
from geopy.distance import geodesic


# convert x_2d to lon_range, y_2d to lat_range
def get_dd(x, origin_lon=0, origin_lat=0):
    return geodesic(kilometers=x * 0.001).destination(
        geopy.Point(origin_lat, origin_lon), 0
    )[0]


def contour_to_gdf(cp, out_file="test.gpkg"):
    geojson = geojsoncontour.contour_to_geojson(contour=cp, ndigits=6, unit="m")
    return gpd.read_file(geojson, driver="GeoJSON")    
