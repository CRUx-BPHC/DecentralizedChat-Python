import asyncio


class Client:

    def __init__(self,
                 reader: asyncio.StreamReader,
                 writer: asyncio.StreamWriter,
                 loop: asyncio.AbstractEventLoop) -> None:
        self.stream_reader = reader
        self.stream_writer = writer
        loop.create_task(self.receive_broadcast())
        loop.run_forever()

    async def broadcast_message(self, msg: str):
        self.stream_writer.write(msg)

    async def receive_broadcast(self):
        while True:
            message = (await self.stream_reader.read(4096)).decode('utf-8')
            print("Received message:", message)
