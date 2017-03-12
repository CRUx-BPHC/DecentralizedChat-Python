import asyncio


class Client:

    def __init__(self,
                 reader: asyncio.StreamReader,
                 writer: asyncio.StreamWriter,
                 recv_cor: asyncio.coroutine) -> None:
        self.stream_reader = reader
        self.stream_writer = writer
        self.recv_cor = recv_cor
        self.recv_cor.send(None)

    def send_client_message(self, message: str):
        self.stream_writer.write(message.encode())

    async def receive_broadcast(self):
        while True:
            message = (await self.stream_reader.read(4096)).decode()
            # received broadcast message from server passed to coroutine in GUI
            self.recv_cor.send(message)
