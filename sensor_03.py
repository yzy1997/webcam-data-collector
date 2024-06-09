import asyncio
from bleak import BleakScanner
from bleak import BleakClient

async def scan_for_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")

asyncio.run(scan_for_devices())

def handle_acceleration_data(sender, data):
    # Process the incoming data. The format depends on the Movesense device's specification.
    print(f"Acceleration Data from {sender}: {data}")

async def collect_data_from_movesense(device_address, characteristic_uuid):
    async with BleakClient(device_address) as client:
        # Connect to the device
        connected = await client.connect()
        if connected:
            print(f"Connected to {device_address}")

            # Subscribe to the acceleration characteristic
            await client.start_notify(characteristic_uuid, handle_acceleration_data)

            # Keep the program running to collect data
            print("Collecting data. Press Ctrl+C to stop.")
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                pass
            finally:
                # Unsubscribe and disconnect
                await client.stop_notify(characteristic_uuid)
                await client.disconnect()

device_address = "0C:8C:DC:34:E8:FE"
characteristic_uuid = "0000fdf3-0000-1000-8000-00805f9b34fb"
asyncio.run(collect_data_from_movesense(device_address, characteristic_uuid))