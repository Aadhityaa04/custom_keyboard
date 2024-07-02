# import serial.tools.list_ports

# def get_com_ports():
#   ports = serial.tools.list_ports.comports()
#   return ports

# if __name__ == "__main__":
#   com_ports = get_com_ports()
#   if com_ports:
#     for _ in com_ports:
#       print(_)
#   else:
#     print("None")




key_mapping = key_mapping = {
    "Key.backspace": "KEY_BACKSPACE",
    "Key.caps_lock": "KEY_CAPS_LOCK",
    "Key.delete": "KEY_DELETE",
    "Key.down": "KEY_DOWN_ARROW",
    "Key.end": "KEY_END",
    "Key.esc": "KEY_ESC",
    "Key.f1": "KEY_F1",
    "Key.f10": "KEY_F10",
    "Key.f11": "KEY_F11",
    "Key.f12": "KEY_F12",
    "Key.f13": "KEY_F13",
    "Key.f14": "KEY_F14",
    "Key.f15": "KEY_F15",
    "Key.f16": "KEY_F16",
    "Key.f17": "KEY_F17",
    "Key.f18": "KEY_F18",
    "Key.f19": "KEY_F19",
    "Key.f2": "KEY_F2",
    "Key.f20": "KEY_F20",
    "Key.f21": "KEY_F21",
    "Key.f22": "KEY_F22",
    "Key.f23": "KEY_F23",
    "Key.f24": "KEY_F24",
    "Key.f3": "KEY_F3",
    "Key.f4": "KEY_F4",
    "Key.f5": "KEY_F5",
    "Key.f6": "KEY_F6",
    "Key.f7": "KEY_F7",
    "Key.f8": "KEY_F8",
    "Key.f9": "KEY_F9",
    "Key.home": "KEY_HOME",
    "Key.insert": "KEY_INSERT",
    "*": "KEY_KP_ASTERISK",
    "Key.enter": "KEY_KP_ENTER",
    "-": "KEY_KP_MINUS",
    "+": "KEY_KP_PLUS",
    "/": "KEY_KP_SLASH",
    ".": "KEY_KP_DOT",
    "Key.alt_l": "KEY_LEFT_ALT",
    "Key.left": "KEY_LEFT_ARROW",
    "Key.ctrl_l": "KEY_LEFT_CTRL",
    "Key.cmd": "KEY_LEFT_GUI",
    "Key.shift": "KEY_LEFT_SHIFT",
    "Key.menu": "KEY_MENU",
    "Key.num_lock": "KEY_NUM_LOCK",
    "Key.page_down": "KEY_PAGE_DOWN",
    "Key.page_up": "KEY_PAGE_UP",
    "Key.print_screen": "KEY_PRINT_SCREEN",
    "Key.return": "KEY_RETURN",
    "Key.alt_r": "KEY_RIGHT_ALT",
    "Key.alt_gr": "KEY_RIGHT_ALT",
    "Key.right": "KEY_RIGHT_ARROW",
    "Key.ctrl_r": "KEY_RIGHT_CTRL",
    "Key.cmd": "KEY_RIGHT_GUI",
    "Key.shift_r": "KEY_RIGHT_SHIFT",
    "Key.tab": "KEY_TAB",
    "Key.up": "KEY_UP_ARROW",
    "Key.left": "KEY_LEFT_ARROW",
    "Key.space": "KEY_SPACE",
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "z": "z",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",

}

from pynput import keyboard
def on_release(key):  
    # if str(key) in key_mapping: 
    #   print(key_mapping[str(key)]) 
    # elif key.char in key_mapping:
    #    print(key_mapping[key.char])
    # else:
    #    print("printing Here"+str(key))
    #    print(key.char == 'q')
    print(key.char)
# Collect events until released
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()