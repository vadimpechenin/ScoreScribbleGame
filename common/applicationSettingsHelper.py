"""
Записать файл, прочитать файл настроек
"""
import json
from os.path import join

from kivy.utils import platform

from common.commonUtils import CommonUtils

import appEnvironment as AE

class ApplicationSettingHelper():
    @staticmethod
    def isFileNameInDevice(filename):
        base_dir = ApplicationSettingHelper.base_dir_done()

        json_file_name = join(base_dir, filename)
        with open(json_file_name) as json_file:
            data = json.load(json_file)
        if (data==None):
            return False
        else:
            return True


    @staticmethod
    def readSettingsFromFile(filename, parameters):
        #Добавить путь, прочитать из файла, формат json
        base_dir = ApplicationSettingHelper.base_dir_done()
        if (len(AE.filenameEnv) > 0):
            json_file_name = AE.filenameEnv[0]
        else:
            json_file_name = join(base_dir, filename)

        with open(json_file_name) as json_file:
            data = json.load(json_file)
            #print(data) #'json_data.json'
        parameters.gamerNames = data.get('gamerNames')
        parameters.gamerCount = data.get('gamerCount')
        parameters.round = data.get('round')
        parameters.timeOfGameInSec = data.get('timeOfGameInSec')
    @staticmethod
    def writeSettingsToFile(filename, parameters):
        #Добавить путь, записать в файл, формат json

        base_dir = ApplicationSettingHelper.base_dir_done()

        json_file_name = join(base_dir, filename)
        data = {
            'gamerNames': parameters.gamerNames,
            'gamerCount': parameters.gamerCount,
            'round': parameters.round,
            'timeOfGameInSec': parameters.timeOfGameInSec,
        }

        # .dumps() as a string
        json_string = json.dumps(data)

        # Using a JSON string
        with open(json_file_name, 'w') as outfile:
            outfile.write(json_string)

    @staticmethod
    def base_dir_done():
        if platform == 'android':
            base_dir = '/storage/emulated/0/DCIM'
        else:
            base_dir = CommonUtils.getSolutionFolder().joinpath("PYTHON").\
                joinpath("Programms").\
                joinpath("ScoreScribbleGame").\
                joinpath("resources").joinpath("json")
        return base_dir

    @staticmethod
    def nomenclatureListsUnpacking(parameters):
        #Распаковка в списки справочника по номенклатуре деталей
        parameters.nomenclatureNameList = []
        parameters.nomenclatureIDList = []
        for item in parameters.nomenclatureList:
            parameters.nomenclatureNameList.append(item['name'])
            parameters.nomenclatureIDList.append(item['id'])

    @staticmethod
    def operationTypeListsUnpacking(parameters):
        #Распаковка в списки справочника по операциям
        parameters.operationTypeDescriptionList = []
        parameters.operationTypeIDList = []
        for item in parameters.operationTypeList:
            parameters.operationTypeDescriptionList.append(item['description'])
            parameters.operationTypeIDList.append(item['id'])

    @staticmethod
    def stateTypeListsUnpacking(parameters):
        # Распаковка в списки справочника по характеристикам годности
        parameters.stateTypeDescriptionList = []
        parameters.stateTypeIDList = []
        for item in parameters.stateTypeList:
            parameters.stateTypeDescriptionList.append(item['stateDescription'])
            parameters.stateTypeIDList.append(item['id'])

    @staticmethod
    def partListsUnpacking(parameters):
        # Распаковка в списки справочника по деталям
        parameters.partTypeList = []
        parameters.partExternalIdList = []
        parameters.partIdList = []
        for item in parameters.operationTypeList:
            parameters.operationTypeDescriptionList.append(item['description'])
            parameters.operationTypeIDList.append(item['id'])