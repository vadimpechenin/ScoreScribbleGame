import unittest

from model.applicationSettings import ApplicationSettings
from serverProxy import ServerProxy
import appEnvironment as AE


class CreateNewGame(unittest.TestCase):

    def test_createNewGame(self):
        AppSetObj = ApplicationSettings()
        ServerProxyObj = ServerProxy(AE.ServerHost, AE.ServerPort)
        AppSetObj.gamerNames = []
        AppSetObj.gamerCount = []
        AppSetObj.round = []
        AppSetObj.timeOfGameInSec = []
        AppSetObj.gamerIndex = 0

        AppSetObj.gamerNames.append("Вадим")
        AppSetObj.gamerCount.append(0)
        AppSetObj.gamerNames.append("Екатерина")
        AppSetObj.gamerCount.append(0)
        AppSetObj.round.append(1)
        result = ServerProxyObj.saveAndLoadGame(2, "TestGame", AppSetObj)

        self.assertEqual(True, result)


if __name__ == "__main__":
    unittest.main()
