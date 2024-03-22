import time
import asyncio
from bleak import BleakClient

address = "34:85:18:7A:99:31"
service = "beb5483e-36e1-4688-b7f5-ea07361b26a8"


async def main(address):
    async with BleakClient(address) as client:
        while client:
            out = await client.read_gatt_char(service)
            if out:
                print("ERROR!")
            else:
                print("Fine!")
            time.sleep(5)

asyncio.run(main(address))
