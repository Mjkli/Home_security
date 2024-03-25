# from ble_client import state
# import asyncio
import json

# Setup multi switch manager object

class Device:
    def __init__(self, name,address,service):
        self.name = name
        self.address = address
        self.service = service




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


def main():
    devices = load_devices()
    
    # await state(address1)

main()
