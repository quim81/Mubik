import asyncio

from bleak import BleakScanner


async def main():
    # cube_found = false
    devices = await BleakScanner.discover()
    mubik: BLEdevice
    for d in devices:
        if d.name == 'Gi144467':
            mubik = d
            print(mubik)

    """
    if (cube_found == true):
        # Connect Cube
        async with BleakClient(mubik.address) as client
    """

if __name__ == '__main__':
    asyncio.run(main())