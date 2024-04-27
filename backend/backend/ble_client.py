import time
import asyncio
from bleak import BleakClient


async def connect_device(address: str, service: str):    
    async with BleakClient(address) as client:
        await client.connect()
        return client
    return "error"



async def read_state(client: BleakClient) -> bool:
    return await client.read_gatt_char(service)





