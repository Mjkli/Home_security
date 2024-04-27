from ble_client import read_state, connect_device
import asyncio
import json
import time

# Setup multi switch manager object

# Beable to load new devices into the list.
# go through the devices and update the state of each device to be stored



class Device:
    def __init__(self,name:str, address:str, service:str):
        self.name = name
        self.address = address
        self.service = service
        self.connection = None 

    async def connect(self):
        self.connection = await connect_device(self.address,self.service)

    def switch_status(self) -> bool:
        return read_state(self.connection)

def load_devices():
    #read json file and build object with device settings
    devs = []

    with open('devices.json', 'r') as f:
        devices = json.load(f)
        for d in devices:
            temp = Device(devices[d].get("name"), 
                                devices[d].get("address"),
                                devices[d].get("service")
                                )
            devs.append(temp)

    f.close()

    return devs

async def connect_devices(devices: []):
    for d in devices:
       await d.connect() 




# def add_device(name:str, address:str, service:str):
#     device = {}
#     device['name'] = name
#     device['address'] = address
#     device['service'] = service
#     json_data = json.dumps(device, indent=4)

#     with open('devices.json','a') as f:
#         f.write(json_data)
            


async def print_stat(dev: Device):
   print(dev.connection) 
    # print(dev.name + " " + str(con))


async def main():
    devices = []
    devices = load_devices()
    await connect_devices(devices)
    while True:
        for d in devices:
           await print_stat(d)
        time.sleep(5)


asyncio.run(main())
