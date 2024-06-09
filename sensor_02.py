import asyncio
import logging

from bleak import BleakClient

format_string = "%(asctime)s %(levelname)s %(name)s: %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=format_string,
                    )
logger = logging.getLogger('run')

def disconnect_handler(c: BleakClient):
    logger.info("Disconnect handler")
    asyncio.get_running_loop().create_task(reconnect(c))


async def reconnect(c: BleakClient):
    logger.info("Reconnect")
    await c.connect()
    if not c.is_connected:
        # lazily call recursively, as shouldn't be more than a few
        await asyncio.sleep(10)
        await reconnect(c)


async def run():

    BLE_ID = '0C:8C:DC:34:E8:FE'

    client = BleakClient(BLE_ID)
    client.set_disconnected_callback(disconnect_handler)
    await client.connect()
    logger.info("Connected")
    await asyncio.sleep(90)
    logger.info("90 seconds, disconnecting")
    await client.disconnect()


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(run())