dictDay = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресение'}
dictMonth = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля',
             8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

koef = 1

login = False

TestObj = None
AppSetObj = None

NewWObj = None
ContinueWObj = None
GameWObj = None
ReportWObj = None
SaveWObj = None
SettingsWObj = None
LogInOutWObj = None
NewSettingsWObj = None
NavigationrailObj = None

nameOfJson = 'json_data.json'

kv = None

ServerHost = "127.0.0.1"
ServerPort = 8080
ServerProxyObj = None

filenameEnv = []

title_of_windows = ['Новая игра',
                    'Продолжить игру',
                    'Игровой процесс',
                    'Сохранение игры',
                    'Меню настроек',
                    'Меню выхода']

title_label_new = ['Введите имя игрока ',
                   'Введите название файла']

title_label_continue = ['Выберите файл и продолжите игру']

title_label_game = ['Ходит ',
                    'Общий счет ',
                    'Имя игрока не введено',
                    'Раунд ']
