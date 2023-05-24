#!/usr/bin/env python3
from qgis.core import *
import qgis.utils
pathLayerZone = '/test.shp'
layer_Zone = QgsVectorLayer(pathLayerZone, pathLayerZone, "ogr")


LandFeatures = layer_Zone.getFeatures()
ZoneFeatures = layer_Zone.getFeatures()

for ZoneFeature in ZoneFeatures:
    a = ZoneFeature.geometry()
    print (a)
    
