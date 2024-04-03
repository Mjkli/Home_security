#from ble_client import read_state
#import asyncio
import json
import time

# Setup multi switch manager object

# Beable to load new devices into the list.
# go through the devices and update the state of each device to be stored



class Device:
    name = ""
    address = ""
    service = ""
    state = False

    def __init__(self,name:str, address:str, service:str):
        self.name = name
        self.address = address
        self.service = service

    def status(self) -> bool:
        self.state = not self.state #swapping for debugging outside of pi 
        return self.state


def load_devices():
    #read json file and build object with device settings
    devs = []

    with open('devices.json') as f:
        d = json.load(f)
        for device in d:
            dev = d[device] 
            temp = Device(dev['name'],dev['address'],dev['service'])
            devs.append(temp)
        
    return devs


def print_stat(dev: Device):
    print(dev.name + " " + str(dev.status()))


def main():
    devices = load_devices()
    while True:
        for d in devices:
            print_stat(d)
        time.sleep(5)


main()
