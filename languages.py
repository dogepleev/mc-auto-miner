import constants

class Localization:
    """Multi-language system"""
    def __init__(self, lang):
        """Available langiages: en, ru"""
        self.language = lang.lower()
        if self.language == 'ru':
            self.greetings = f"""Добро пожаловать в {constants.NAME} {constants.VERSION}!
Данная программа поможет в автономном копании ресурсов.
Эта программа является читом. Использовать в персональных целях и на свой страх и риск.
Разработчик: {constants.CREATOR}. Репозиторий на GitHub: {constants.GITHUB}"""
            self.just_created_config = "Только что в этой директории был создан файл config.json, содержащий настройки программы."
            self.current_settings = "Текущая конфигурация:"
            self.notifications = "Уведомления: "
            self.start = "Клавиша старта: "
            self.pause = "Клавиша паузы: "
            self.unpause = "Клавиша снятия паузы: "
            self.stop = "Клавиша остановки: "
            self.walk = "Клавиша ходьбы вперёд: "
            self.shift = "Клавиша удержания шифта: "
            self.mine = "Кнопка мыши копания: "
            self.use = "Кнопка мыши использования: "
            self.guide = """Как пользоваться?
1. Возьмите с собой кирку (или несколько), минимально железного уровня, и еду. Для большей безопасности можно взять блоки, вёдра воды и зелья огнестойкости.
2. Опуститесь на высоту y=11-12
3. В главную руку возьмите кирку, а во вторую - еду.
4. Нажмите на клавишу старта, чтобы начать.
5. Используйте клавиши паузы и вообновления, если вам нужно взять управление на себя.
6. Используйте клавишу стоп, чтобы остановить работу и закрыть программу."""
            self.started = "Работа началась."
            self.paused = "Работа приостановлена. Чтобы возообновить, нажмите "
            self.unpaused = "Работа возообновлена."
            self.stopped = "Работа закончена."

        else:
            self.greetings = f"""Welcome to the {constants.NAME} {constants.VERSION}!
This program helps you mining resources automatically.
This program is cheat. Only for personal use. Use at one's own risk.
Developer: {constants.CREATOR}. GitHub repository: {constants.GITHUB}"""
            self.just_created_config = "File config.json just created in current directory. This file containts program settings."
            self.current_settings = "Current configuration:"
            self.notifications = "Show notifications: "
            self.start = "Start key: "
            self.pause = "Pause key: "
            self.unpause = "Unpause key: "
            self.stop = "Stop key: "
            self.walk = "Walk key: "
            self.shift = "Shift key: "
            self.mine = "Mine mouse button: "
            self.use = "Use mouse button: "
            self.guide = """How use this?
1. Take pickaxe(s), iron level minimum, food. For safety, also take blocks, water buckets, fire resistance potions.
2. Go at level y=11-12
3. In the main hand take pickaxe, in the second - food.
4. Press start key and program start working.
5. Use pause and unpause key, if you need to take controls to self.
6. Press stop key to stop script and close program."""
            self.started = "Script has started work."
            self.paused = "Paused. To unpause, press "
            self.unpaused = "Unpaused."
            self.stopped = "Script has stopped work."
    
    def translate_key(self, key):
        if self.language == 'ru':
            try:
                res = f'[{key.replace("left", "левый").replace("right", "правый").title()}]'
            except AttributeError:
                res = "[Не назначено]"
            return res
        else:
            try:
                res = f'[{key.title()}]'
            except AttributeError:
                res = "[Not bound]"
            return res

    def translate_bool(self, value):
        if self.language == 'ru':
            if value: return 'Вкл.'
            elif not value: return 'Выкл.'
            elif value == '' or value is None: return 'Отсутствует/Выключено'
        else:
            if value: return 'On'
            elif not value: return 'Off'
            elif value == '' or value is None: return 'None/Off'