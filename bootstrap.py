import appEnvironment as AE
from kivy.lang import Builder

from kivy.core.window import Window
from clientProxy import ClientProxy
from model.applicationSettings import ApplicationSettings
from serverProxy import ServerProxy
from test import Test


class Bootstrap:

    @staticmethod
    def initEnviroment():
        if (AE.koef == 1):
            Window.size = (420, 800)
        else:
            Window.size = (1100, 2300)
        AE.kv = Builder.load_file("windows/navigationrail.kv")
        AE.TestObj = Test()
        AE.ClientProxyObj = ClientProxy()
        AE.ApplicationSettingObj = ApplicationSettings()
        AE.ServerProxyObj = ServerProxy(AE.ServerHost, AE.ServerPort)

    @staticmethod
    def run():
        AE.TestObj.run()
