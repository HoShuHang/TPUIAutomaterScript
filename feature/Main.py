import unittest
import Value
from screens.MainScreen import MainScreen


class Main(unittest.TestCase):
    def setUp(self):
        self.launch_app()
        self.main_screen = MainScreen()

    def dMobile(self):
        return Value.dMobile

    def launch_app(self):
        self.dMobile()(text='Evernote').click.wait()

    def add_new_notes_in_list(self):
        self.main_screen.add_note()
        pass
