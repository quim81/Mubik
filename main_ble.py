import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d.details)

if __name__ == '__main__':
    asyncio.run(main())