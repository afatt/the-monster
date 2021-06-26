#!/usr/bin/env python3

'''
This server connects and exposes its functions to the Hello World 
anvil client via uplink
'''
import yaml
import anvil.server

# opens the yaml file and sets variable containing the anvil 'uplink key'
with open('secrets.yaml') as yml:
	contents = yaml.load(yml, Loader=yaml.FullLoader)
	anvil_key = contents['api_keys']['anvil']
 
anvil.server.connect(anvil_key)

# this is how you make a function callable by the anvil client
@anvil.server.callable
def from_uplink(name):
  print("Hello from the uplink, %s!" % name)

# maintains the connection to the client even when client disconnects
anvil.server.wait_forever()