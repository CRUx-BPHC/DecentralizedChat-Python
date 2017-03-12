import threading
import asyncio

import client


class NetworkThread(threading.Thread):

    def __init__(self,
                 host: str,
                 port: int,
                 recv_cor: asyncio.coroutine) -> None:
        threading.Thread.__init__(self)
        self.network_event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.network_event_loop)

        # coroutine passed to client while initializing client
        # in create client method
        self.recv_cor = recv_cor
        self.host = host
        self.port = port
        self.client = None

    def run(self):
        self.network_event_loop.run_until_complete(self.create_client())

    async def create_client(self):
        # streams is list containing stream_reader and stream_writer
        streams = await asyncio.open_connection(self.host,
                                                self.port,
                                                loop=self.network_event_loop)
        # client is created with msg_recv_cor (a coroutine, to which we can
        # send the received broadcast message from server, an easy way to do
        # share objects(string here) between threads
        self.client = client.Client(
            streams[0], streams[1], self.recv_cor)
        await self.client.receive_broadcast()

    @asyncio.coroutine
    def msg_send_cor(self):
        while True:
            client_message = yield
            self.client.send_client_message(client_message)