import asyncio
from bleak import BleakClient
import datetime

# Replace these with the actual device address and characteristic UUIDs
DEVICE_ADDRESS = "0C:8C:DC:34:E8:FE"
ACCELERATION_CHAR_UUID = "34802252-7185-4d5d-b431-630e7050e8f0"
# GYROSCOPE_CHAR_UUID = "0000fdf3-0000-1000-8000-00805f9b34fb"
# MAGNETOMETER_CHAR_UUID = "0000fdf3-0000-1000-8000-00805f9b34fb"

# File to save the data
DATA_FILE = "movesense_data.csv"

def notification_handler(sender, data):
    # This function will be called when notification is received
    print(f"Notification from {sender}: {data}")
    with open(DATA_FILE, 'a') as file:
        # Write data to file, you might want to format or decode data appropriately
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp},{sender},{data}\n")

async def run_ble_client(device_address: str):
    async with BleakClient(device_address) as client:
        # Connect to the device
        if not client.is_connected:
            try:
                await client.connect()
                print("Connected successfully.")
            except Exception as e:  # Catching a more general exception might be safer
                print(f"Failed to connect: {e}")
        else:
            print(f"Connected to {device_address}")

        # Initialize file with headers
        with open(DATA_FILE, 'w') as file:
            file.write("Timestamp,Sensor ID,Data\n")

        # Subscribe to acceleration, gyroscope, and magnetometer notifications
        await client.start_notify(ACCELERATION_CHAR_UUID, notification_handler)
        # await client.start_notify(GYROSCOPE_CHAR_UUID, notification_handler)
        # await client.start_notify(MAGNETOMETER_CHAR_UUID, notification_handler)

        # Keep the script running to continue receiving notifications
        await asyncio.sleep(3)  # Or however long you wish to collect data

        # Unsubscribe from notifications
        await client.stop_notify(ACCELERATION_CHAR_UUID)
        # await client.stop_notify(GYROSCOPE_CHAR_UUID)
        # await client.stop_notify(MAGNETOMETER_CHAR_UUID)

# Discover the uuid of device
async def discover_services_and_characteristics(client):
    async with client:
        services = await client.get_services()
        for service in services:
            print(service)
            characteristics = service.characteristics
            for char in characteristics:
                print(char)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(discover_services_and_characteristics(BleakClient(DEVICE_ADDRESS)))
    asyncio.get_event_loop().run_until_complete(run_ble_client(DEVICE_ADDRESS))
