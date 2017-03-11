from gi.repository import Gtk


class Window(Gtk.ApplicationWindow):

    def __init__(self,
                 application: Gtk.Application) -> None:
        Gtk.ApplicationWindow.__init__(self)
        self.set_application(application)
        self.set_title("Decentralized Chat")

        builder = Gtk.Builder()
        # builder.new_from_resource("org/crux/Chat/basic_server_client.ui")
        builder.add_from_file("basic_server_client.ui")
        grid = builder.get_object("grid_main_ui")
        self.add(grid)

        self.entry_server_ip = builder.get_object("entry_server_ip")
        self.entry_server_port = builder.get_object("entry_server_port")
        self.entry_username = builder.get_object("entry_username")

        chat_display = builder.get_object("scrolled_window_chat_display")
        chat_display.set_size_request(-1, 300)
        self.grid_chat_display = Gtk.Grid()
        self.grid_chat_display.set_orientation(Gtk.Orientation.VERTICAL)
        chat_display.add_with_viewport(self.grid_chat_display)

        self.entry_chat_message = builder.get_object("entry_chat_message")

        self.button_send = builder.get_object("button_chat_message_send")
        image_send = Gtk.Image()
        image_send.set_from_file("send_msg_16.png")
        self.button_send.set_image(image_send)
        self.button_send.connect("clicked", self.send_message)

    def send_message(self, button_send: Gtk.Button) -> None:
        pass