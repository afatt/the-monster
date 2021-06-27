#!/usr/bin/env python3

'''
This server connects and exposes its functions to the Hello World 
anvil client via uplink
'''

import yaml
import anvil.server


class UplinkServer():
    def __init__(self):
        self.anvil_key = self._load_key()


    def _load_key(self):
        '''opens the yaml file and sets variable containing the anvil uplink key'''

        with open('secrets.yaml') as yml:
          contents = yaml.load(yml, Loader=yaml.FullLoader)
          anvil_key = contents['api_keys']['anvil']

        return(anvil_key)


# this is how you make a function callable by the anvil client
# could also make it callable under a different name
# @anvil.server.callable('different_name')
@anvil.server.callable
def from_uplink(name):
  print("Hello from the uplink, %s!" % name)

def main():

    uplink_server = UplinkServer()
    anvil.server.connect(uplink_server.anvil_key)
    anvil.server.wait_forever() #this is blocking


if __name__ == '__main__':
    main()