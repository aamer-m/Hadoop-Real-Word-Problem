#!/usr/bin/python
import sys
import json

for line in sys.stdin:
  jOne = json.loads(line.strip())
  coord_dict = {'lat':0,'long':0,'yes':0}
  if "geo" in jOne.keys() and jOne["geo"] != None:
  	geoJOne = jOne["geo"]
  	coord_dict['lat'] = geoJOne["coordinates"][0]
  	coord_dict['long'] = geoJOne["coordinates"][1]
  	coord_dict['yes'] = 1
  elif "place" in jOne.keys() and jOne["place"] != None and "bounding_box" in jOne["place"].keys() and jOne["place"]["bounding_box"] != None:
    placeJOne = jOne["place"]
    boundingPlaceJOne = placeJOne['bounding_box']
    if "coordinates" in boundingPlaceJOne:
      coordsBPJOne = boundingPlaceJOne['coordinates']
    else:
      coordsBPJOne = [[[0.0, 0.0]]]
    centerBPJOne = [0.0,0.0]
    coordsLen = len(coordsBPJOne)
    for coord in coordsBPJOne[0]:
      centerBPJOne[0] += coord[0]
      centerBPJOne[1] += coord[1]
    coord[0] /= coordsLen
    coord[1] /= coordsLen
    coord_dict['lat'] = coord[0]
    coord_dict['long'] = coord[1]
    coord_dict['yes'] = 1
  print "coords\t%s" % ('{"lat": %s, "long": %s, "yes": %s}' %(coord_dict['lat'], coord_dict['long'], coord_dict['yes']))
