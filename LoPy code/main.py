from network import LoRa 
import struct 
import binascii 
import socket 
import time
import  uos
import array
import machine
from pytrack import Pytrack
py = Pytrack()

def convert_latlon(latitude, longitude):
# latitude = -37.8597
# longitude = 144.8126

   lat = int((latitude + 90)*10000)
   lon = int((longitude + 180)*10000)

   coords = array.array('B', [0,0,0,0,0,0])
   coords[0] = lat
   coords[1] = (lat >> 8)
   coords[2] = (lat >> 16)

   coords[3] = lon
   coords[4] = (lon >> 8)
   coords[5] = (lon >> 16)

   return coords
	

print("set up to send LoRa message")
freq = 915000000 
# Initialize LoRa in LORAWAN mode. 
lora = LoRa(mode=LoRa.LORAWAN) 
#Setup the single channel for connection to the gateway 
for channel in range(0, 72): 
   lora.remove_channel(channel) 
for chan in range(0, 8): 
   lora.add_channel(chan,  frequency=freq,  dr_min=0,  dr_max=3) 
#Device Address, get this from TTN
dev_addr = struct.unpack(">l", binascii.unhexlify('26011BD7'))[0] 
print("device address")
print(dev_addr)
#Network Session Key, get this from TTN 
nwk_swkey = binascii.unhexlify('8D51BDB02381CFC1621C27FF6FD5D0AE') 
#App Session Key, get this from TTN 
app_swkey = binascii.unhexlify('BFFE575DDE86A4647EEA1CE781CD7F43') 
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey)) 
# create a LoRa socket 
print("create a LoRa socket ")
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW) 
# set the LoRaWAN data rate 
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3) 
# make the socket non-blocking 
s.setblocking(False)
print("delay 2 seconds")
time.sleep(2)    # <- emm, not sure why I have this..will clean up soon..
print("setup done, send message")
print("first check coords, print lat and lon here")
print(lat,lon)

# lat and lon are floating points, this will not be supported in the TTN HTTP API integration, if you want to decode the payload...
# convert to array of bytes in function convert_latlon
gps_array = convert_latlon(lat, lon)
print("converted array is..")
print(gps_array)

# Send coordinates

s.send(gps_array) # <- sent as array of bytes, we then can decode as appropriate in TTN payload configuration..
print("sent message, wait for 10 secs")
time.sleep(10)   # <- delay to ensure message sent before going to sleep, improve this...

# Deep Sleep
# Since this project uses the Pytracker shield, there is no need to use the sleep shield. When using the Pytracker shield, deep sleep is achived 
# using py.go_to_sleep. Hence make sure the correct library is used !!! See lib folder. 

print("now sleep 120 seconds..")	 
py.setup_sleep(120) # deep sleep for 120 seconds, change this to suit your own needs and respect TTN fair usage policy. 
py.go_to_sleep()
