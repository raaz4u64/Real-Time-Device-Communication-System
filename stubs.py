from protocols import TCPIPProtocol

# Stub for testing TCP/IP communication
class TCPIPStub(TCPIPProtocol):
    def __init__(self, ip: str, port: int):
        super().__init__(ip, port)
        self.stored_data = ""

    async def connect(self):
        pass

    async def read(self) -> str:
        return self.stored_data

    async def write(self, data: str) -> None:
        self.stored_data = data