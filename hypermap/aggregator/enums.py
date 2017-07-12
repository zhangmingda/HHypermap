SERVICE_TYPES = (
    ('OGC:CSW', 'Catalogue Service for the Web (CSW)'),
    ('OGC:WMS', 'Web Map Service (WMS)'),
    ('OGC:WMTS', 'Web Map Tile Service (WMTS)'),
    ('OSGeo:TMS', 'Tile Map Service (TMS)'),
    ('ESRI:ArcGIS:MapServer', 'ArcGIS REST MapServer'),
    ('ESRI:ArcGIS:ImageServer', 'ArcGIS REST ImageServer'),
    ('Hypermap:WorldMap', 'Harvard WorldMap'),
    ('Hypermap:WARPER', 'Mapwarper'),
    ('Harvard:HGL', 'Harvard Geospatial Library'),
)

CSW_RESOURCE_TYPES = {
    'OGC:CSW': 'http://www.opengis.net/cat/csw/2.0.2',
    'OGC:WMS': 'http://www.opengis.net/wms',
    'OGC:WMTS': 'http://www.opengis.net/wmts/1.0',
    'OSGeo:TMS': 'https://wiki.osgeo.org/wiki/TMS',
    'ESRI:ArcGIS:MapServer': 'urn:x-esri:serviceType:ArcGIS:MapServer',
    'ESRI:ArcGIS:ImageServer': 'urn:x-esri:serviceType:ArcGIS:ImageServer',
    'Hypermap:WorldMap': 'http://worldmap.harvard.edu/',
    'Hypermap:WARPER': 'https://github.com/timwaters/mapwarper',
}

SUPPORTED_SRS = [
                    'EPSG:3978', '3978',
                    'EPSG:3995', '3995',
                    'EPSG:4326', '4326',
                    'EPSG:5936', '5936',
                    'EPSG:102100', '102100',
                    'EPSG:102113', '102113',
                    'EPSG:102736', '102736',
                ]

DATE_DETECTED = 0
DATE_FROM_METADATA = 1

DATE_TYPES = (
    (DATE_DETECTED, 'Detected'),
    (DATE_FROM_METADATA, 'From Metadata'),
)
