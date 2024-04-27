from ble_client import read_state, connect_device
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
    connection = null

    async def __init__(self,name:str, address:str, service:str):
        self.name = name
        self.address = address
        self.service = service
        self.connection = await connect_device(self.address, self.service) 

    async def switch_status(self) -> bool:
        return await read_state(self.connection)

def load_devices():
    #read json file and build object with device settings
    devs = []

    with open('devices.json', 'r') as f:
        d = json.load(f)
        devs = Device(d['name'],d['address'],d['service']) 
    f.close()

    return devs

# def add_device(name:str, address:str, service:str):
#     device = {}
#     device['name'] = name
#     device['address'] = address
#     device['service'] = service
#     json_data = json.dumps(device, indent=4)

#     with open('devices.json','a') as f:
#         f.write(json_data)
            


async def print_stat(dev: Device):
    print(dev.name + " " + str(await dev.switch_status()))


def main():
    devices = []
    devices.append(load_devices())
    while True:
        for d in devices:
            print_stat(d)
        time.sleep(5)


main()
