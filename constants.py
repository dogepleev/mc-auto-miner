import locale

VERSION = '1.0.0'
NAME = 'MC AutoMiner'
CREATOR = 'DogePleev'
GITHUB = 'https://github.com/dogepleev/mc-auto-miner'
CONFIG_PATH = 'config.json'
DEFAULT_CONFIG = {
                'language':locale.getdefaultlocale()[0][0:2],
                'show_notifications':True,
                'shift_key':'left shift',
                'walk_key':'w',
                'mine_mouse_button':'left',
                'use_mouse_button':'right',
                'start_key':'alt',
                'pause_key':'`',
                'unpause_key':'tab',
                'stop_key':'0'
                }
FREEZE_TIME = 0.1