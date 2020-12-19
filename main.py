import win10toast
import pyautogui
import keyboard
import json
import time
import os
import constants
import languages

class Config:
    """Program configuration, key settings"""
    def __init__(self):
        """Initialize config data"""
        # Creating config file, if not exists
        if not os.path.exists(constants.CONFIG_PATH):
            self.create()
            self.just_created = True
        else: self.just_created = False
        self.load() # Reading config data
    def create(self):
        """(Re)Create config file"""
        with open(constants.CONFIG_PATH, 'w', encoding='utf-8') as config:
            json.dump(constants.DEFAULT_CONFIG, config)
    def load(self):
        """Load and read config data"""
        with open(constants.CONFIG_PATH, 'r', encoding='utf-8') as data:
            loaded_data = json.load(data)
            try:
                # Settings
                self.language = loaded_data['language']
                self.show_notification = loaded_data['show_notifications']
                # Mouse buttons
                self.mine_mouse_button = loaded_data['mine_mouse_button']
                self.use_mouse_button = loaded_data['use_mouse_button']
                # Keys
                try: self.shift_key = keyboard.normalize_name(loaded_data['shift_key'])
                except ValueError: self.shift_key = loaded_data['shift_key']
                try: self.walk_key = keyboard.normalize_name(loaded_data['walk_key'])
                except ValueError: self.walk_key = loaded_data['walk_key']
                try: self.start_key = keyboard.normalize_name(loaded_data['start_key'])
                except ValueError: self.start_key = loaded_data['start_key']
                try: self.pause_key = keyboard.normalize_name(loaded_data['pause_key'])
                except ValueError: self.pause_key = loaded_data['pause_key']
                try: self.unpause_key = keyboard.normalize_name(loaded_data['unpause_key'])
                except ValueError: self.unpause_key = loaded_data['unpause_key']
                try: self.stop_key = keyboard.normalize_name(loaded_data['stop_key'])
                except ValueError: self.stop_key = loaded_data['stop_key']
            except KeyError: # Config incompatible
                self.create() # Recreate config file
                self.just_created = True
                self.load() # Try again

class System:
    """System info"""
    def __init__(self):
        """Initialize system data"""
        if os.name == 'nt': # If running on Windows, we show notifications
            self.system = 'windows'
            self.toast = win10toast.ToastNotifier()
            os.system(f'title {constants.NAME} {constants.VERSION}')
        else:
            self.toast = None
        self.notifications_queue = []
    def open_config(self):
        if self.system == 'windows':
            os.system('explorer.exe ' + constants.CONFIG_PATH)
    def create_notification(self, message):
        """Create new notification"""
        self.notifications_queue.append(message)
    def destroy_notifications(self):
        """Clear notifications queue"""
        self.queue = []
    def show_notification(self):
        """Showing notifications. Must be running in thread."""
        if self.toast != None and not self.toast.notification_active() and len(self.notifications_queue) > 0:
            message = self.notifications_queue[0]
            if config.show_notification: self.toast.show_toast(title=constants.NAME, msg=message, duration=3, threaded=True, icon_path='icon.ico')
            else: print(message)
            self.notifications_queue.pop(0)
    def freeze(self):
        """Freeze program"""
        time.sleep(constants.FREEZE_TIME)

config = Config()
system = System()
string = languages.Localization(config.language)

def press():
    """Press button to start/unpause mining"""
    if config.walk_key != '' and config.walk_key != None: keyboard.press(config.walk_key)
    if config.shift_key != '' and config.shift_key != None: keyboard.press(config.shift_key)
    if config.mine_mouse_button != '' and config.mine_mouse_button != None: pyautogui.mouseDown(button=config.mine_mouse_button)
    if config.use_mouse_button != '' and config.use_mouse_button != None: pyautogui.mouseDown(button=config.use_mouse_button)

def release():
    """Release buttons to stop/pause mining"""
    if config.walk_key != '' and config.walk_key != None: keyboard.release(config.walk_key)
    if config.shift_key != '' and config.shift_key != None: keyboard.release(config.shift_key)
    if config.mine_mouse_button != '' and config.mine_mouse_button != None: pyautogui.mouseUp(button=config.mine_mouse_button)
    if config.use_mouse_button != '' and config.use_mouse_button != None: pyautogui.mouseUp(button=config.use_mouse_button)

# Before start, showing main information
print(string.greetings)
print()
if config.just_created:
    print(string.just_created_config)
    system.open_config()
print(string.current_settings)
print(string.notifications + string.translate_bool(config.show_notification))
print(string.start + string.translate_key(config.start_key))
print(string.pause + string.translate_key(config.pause_key))
print(string.unpause + string.translate_key(config.unpause_key))
print(string.stop + string.translate_key(config.stop_key))
print(string.shift + string.translate_key(config.shift_key))
print(string.walk + string.translate_key(config.walk_key))
print(string.mine + string.translate_key(config.mine_mouse_button))
print(string.use + string.translate_key(config.use_mouse_button))
print()
print(string.guide)
# Start
keyboard.wait(config.start_key)
system.create_notification(string.started)
press()
# Main loop
while True:
    system.freeze()
    system.show_notification()
    if keyboard.is_pressed(config.pause_key):
        system.create_notification(string.paused + string.translate_key(config.unpause_key))
        release()
    elif keyboard.is_pressed(config.unpause_key):
        system.create_notification(string.unpaused)
        press()
    if keyboard.is_pressed(config.stop_key):
        system.destroy_notifications()
        system.create_notification(string.stopped)
        system.show_notification()
        release()
        break