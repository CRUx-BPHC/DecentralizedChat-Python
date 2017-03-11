import sys

from gi.repository import Gtk, GLib

from ui.window import Window


class Application(Gtk.Application):

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 600

    def __init__(self) -> None:
        Gtk.Application.__init__(self)
        GLib.set_application_name("Decentralized Chat")
        GLib.set_prgname("decentralized_chat")

    def do_activate(self) -> None:
        window = Window(self)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_default_size(Application.WINDOW_WIDTH,
                                Application.WINDOW_HEIGHT)
        window.set_border_width(20)
        window.show_all()

    def do_startup(self) -> None:
        Gtk.Application.do_startup(self)

if __name__ == "__main__":
    app = Application()
    exit_status = app.run()
    sys.exit(exit_status)