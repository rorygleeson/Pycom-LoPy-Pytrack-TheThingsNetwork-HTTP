from L76GNSS import L76GNSS
from pytrack import Pytrack
import gc
print("starting..get GPS")	 
py = Pytrack()
print("setup GPS")
l76 = L76GNSS(py, timeout=60)
coord = l76.coordinates()
lat, lon = coord
print("{}".format(coord))
print("lat lon")
print(lat,lon)
gc.collect()

print("continue")	 
