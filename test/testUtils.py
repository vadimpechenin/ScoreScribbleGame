import pathlib
import unittest

from common.commonUtils import CommonUtils


class TestUtils(unittest.TestCase):
    @staticmethod
    def getTestFolder():
        solutionFolder = CommonUtils.getSolutionFolder()
        return pathlib.Path(solutionFolder).joinpath("ScoreScribbleGame").joinpath("test").resolve()


if __name__ == "__main__":
    unittest.main()
