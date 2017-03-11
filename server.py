import asyncio


class Server:

    def __init__(self, host: str,
                 port: int, loop: asyncio.AbstractEventLoop) -> None:
        self.connections = list()
        loop.create_task(asyncio.start_server(
            self.accept_connection, host, port, loop=loop)
        )

    async def accept_connection(self, reader: asyncio.StreamReader,
                                writer: asyncio.StreamWriter) -> None:
        self.connections.append((reader, writer))
        writer.write("Welcome to chat server.\n".encode('utf-8'))
        await self.manage_connection(reader, writer)

    async def manage_connection(self, reader: asyncio.StreamReader,
                                writer: asyncio.StreamWriter) -> None:
        while True:
            received_message = (await reader.read(4096)).decode('utf-8')
            print("Received data: " + received_message)
            for (client_reader, client_writer) in self.connections:
                client_writer.write(received_message.encode('utf-8'))


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    server = Server('', 8888, event_loop)
    try:
        event_loop.run_forever()
    finally:
        event_loop.close()
