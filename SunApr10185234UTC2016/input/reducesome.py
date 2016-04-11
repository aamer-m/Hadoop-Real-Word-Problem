#!/usr/bin/python
import sys
import string
import json

lats_sum = 0
longs_sum = 0
coord_count = float(0)
total_count = float(0)
result = {}
for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  # if key=="coords":
  coordsD = json.loads(val)
  lats_sum += float(coordsD["lat"])
  longs_sum += float(coordsD["long"])
  coord_count += float(coordsD["yes"])
  total_count += 1
cLatLong = (0, 0)
if coord_count:
  cLatLong = (lats_sum/float(coord_count), longs_sum/float(coord_count))  
result['centroid'] = cLatLong
result['proportionOfCoordsToNoCoords'] = ((total_count - coord_count)/coord_count)
print 'result\t%s' % json.dumps(result)
