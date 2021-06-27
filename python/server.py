#!/usr/bin/env python3

'''
This server connects and exposes its functions to the Hello World 
anvil client via uplink
'''
import yaml
import anvil.server
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echo(DatagramProtocol):
    def datagramReceived(self, data, addr):
        print("received {!r} from {}".format(data, addr))
        self.transport.write(data, addr)

class Server():
    def __init__(self):
        self.anvil_key = self._load_key()

    def _load_key(self):
        '''opens the yaml file and sets variable containing the anvil uplink key'''

        with open('secrets.yaml') as yml:
          contents = yaml.load(yml, Loader=yaml.FullLoader)
          anvil_key = contents['api_keys']['anvil']

        return(anvil_key)

    # this is how you make a function callable by the anvil client
    @anvil.server.callable
    def from_uplink(name):
      print("Hello from the uplink, %s!" % name)

def main():
    message_server = Server()
    anvil.server.connect(message_server.anvil_key)
    anvil.server.wait_forever() #this is blocking
    reactor.listenUDP(33001, Echo())
    reactor.run()
    print('Closed Server')

if __name__ == '__main__':
    main()