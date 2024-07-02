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



from pynput import keyboard
def on_release(key):
    print(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
