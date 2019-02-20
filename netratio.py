"""
Script name: ratio.py
Get 
"""

import time
from dnac import *


# Controller ip, username and password are defined in dnac_config.py
# The get() function is defined in dnac.py
# Get token function is called in get() function

def interfacecount():

  try:
    resp= get(api="interface/count")
    response_json = resp.json() # Get the json-encoded content from response
    return(response_json['response'])
  except:
    print ("Something wrong with GET /interface/count request")
    sys.exit()



def wiredhostcount(thetime):

  try:
    payload = {'timestamp':str(thetime)}
    resp = get(api="client-health" , params=payload)
    response_json = resp.json() # Get the json-encoded content from response
    return(response_json['response'][0]['scoreDetail'][1]['clientCount'])
  except:
    print ("Something wrong with GET /client-health request")
    sys.exit()


millis = int(round(time.time() * 1000))
nbint=interfacecount()
print ("Total interfaces : %s"%(nbint))
nbusedint=wiredhostcount(millis)
print ("Used interfaces : %s"%(nbusedint))
ratio=100*nbusedint/(nbint*0.9)
print ("RATIO = %s percent (considering 10 percent used by network interconnections"%(ratio))
