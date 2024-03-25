import time
import asyncio
from bleak import BleakClient



async def state(address):
    async with BleakClient(address) as client:
        while client:
            out = await client.read_gatt_char(service)
            if out:
                print("ERROR!")
            else:
                print("Fine!")
            time.sleep(5)




