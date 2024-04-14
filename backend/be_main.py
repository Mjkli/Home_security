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
        #self.state = async read_state(self.address)
        self.state = not self.state #swapping for debugging outside of pi 
        return self.state


def load_devices():
    #read json file and build object with device settings
    devs = []

    with open('devices.json', 'r') as f:
        d = json.load(f)
        devs = Device(d['name'],d['address'],d['service']) 
    f.close()

    return devs

def add_device(name:str, address:str, service:str):
    device = {}
    device['name'] = name
    device['address'] = address
    device['service'] = service
    json_data = json.dumps(device, indent=4)

    with open('devices.json','a') as f:
        f.write(json_data)
        
    


def print_stat(dev: Device):
    print(dev.name + " " + str(dev.status()))


def main():
    devices = load_devices()
    print(devices)
    add_device("switch_2","34:85","b7f5-ea07361b26a8")
    # devices = load_devices()
    # print(devices)

    time.sleep(5)


main()
