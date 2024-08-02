import asyncio
import asyncio
from typing import Dict, Any
from protocols import CommunicationProtocol # type: ignore

class DeviceManager:
    def __init__(self):
        self.devices: Dict[str, CommunicationProtocol] = {}

    def add_device(self, name: str, protocol: CommunicationProtocol):
        self.devices[name] = protocol

    async def read_from_device(self, name: str) -> Any:
        if name not in self.devices:
            raise ValueError(f"Device {name} not found")
        return await self.devices[name].read()

    async def write_to_device(self, name: str, data: Any) -> None:
        if name not in self.devices:
            raise ValueError(f"Device {name} not found")
        await self.devices[name].write(data)

    async def read_all_devices(self) -> Dict[str, Any]:
        tasks = [self.read_from_device(name) for name in self.devices]
        results = await asyncio.gather(*tasks)
        return dict(zip(self.devices.keys(), results))

    async def write_all_devices(self, data: Any) -> None:
        tasks = [self.write_to_device(name, data) for name in self.devices]
        await asyncio.gather(*tasks)