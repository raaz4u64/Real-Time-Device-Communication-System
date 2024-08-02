import unittest
import asyncio
from device_manager import DeviceManager
from stubs import TCPIPStub

# Unit tests
class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.manager = DeviceManager()
        self.device1 = TCPIPStub("192.168.1.1", 8080)
        self.device2 = TCPIPStub("192.168.1.2", 8081)
        self.manager.add_device("device1", self.device1)
        self.manager.add_device("device2", self.device2)

    def test_add_device(self):
        self.assertIn("device1", self.manager.devices)
        self.assertIn("device2", self.manager.devices)

    def test_read_write_device(self):
        async def test():
            await self.manager.write_to_device("device1", "Hello")
            data = await self.manager.read_from_device("device1")
            self.assertEqual(data, "Hello")

        asyncio.run(test())

    def test_read_write_all_devices(self):
        async def test():
            await self.manager.write_all_devices("Test")
            data = await self.manager.read_all_devices()
            self.assertEqual(data, {"device1": "Test", "device2": "Test"})

        asyncio.run(test())