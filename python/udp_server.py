#!/usr/bin/env python3

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class UdpServer(DatagramProtocol):
    def __init__(self):
        self.running = False

    def datagramReceived(self, data, addr):
        '''Inhereted method'''
        #TODO: Build a dictionary of addresses
        print("received {!r} from {}".format(data, addr))
        self.transport.write(data, addr)


def main():
    udp_server = UdpServer()
    reactor.listenUDP(33001, UdpServer())
    reactor.run()


if __name__ == '__main__':
    main()