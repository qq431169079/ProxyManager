import threading
import time
import re
import os
from os import listdir
from os.path import  isfile, join
from Proxy import Proxy

class ProxyFileReader(threading.Thread):

    def __init__(self, observable):
        super(ProxyFileReader, self).__init__()

    def run(self):
        while True:
            fileList = [f for f in listdir('ProxyFiles') if isfile(join('ProxyFiles', f)) and f != '.gitkeep']
            for file in fileList:
                lines = [line.strip() for line in open('ProxyFiles/ProxyList')]
                for line in lines:
                    if re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$', line) is not None:
                        proxyParts = line.split(":")
                        print(line + ' - ', end='', flush=True)

                        px = Proxy(proxyParts[0], int(proxyParts[1]))
                        if px.updateProxy():
                            print('WORKING', flush=True)
                        else:
                            print(flush=True)
                    else:
                        print("Odd line: " + line, flush=True)

                os.remove(join('ProxyFiles', file))
            time.sleep(60)