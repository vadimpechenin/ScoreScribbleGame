from kivymd.app import MDApp
from windows.navigationrail import Navigationrail

class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        return Navigationrail()