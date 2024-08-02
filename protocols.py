import abc
import asyncio
from typing import Any

class CommunicationProtocol(abc.ABC):
    @abc.abstractmethod
    async def read(self) -> Any:
        pass

    @abc.abstractmethod
    async def write(self, data: Any) -> None:
        pass


class TCPIPProtocol(CommunicationProtocol):
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.ip, self.port)

    async def read(self) -> str:
        if not self.reader:
            await self.connect()
        data = await self.reader.read(100)
        return data.decode()

    async def write(self, data: str) -> None:
        if not self.writer:
            await self.connect()
        self.writer.write(data.encode())
        await self.writer.drain()