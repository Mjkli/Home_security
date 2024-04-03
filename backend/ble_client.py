import time
import asyncio
from bleak import BleakClient



async def read_state(address: str) -> bool:
    async with BleakClient(address) as client:
        while client:
            out = await client.read_gatt_char(service)
            if out:
                return False
            else:
                return True
            time.sleep(5)




