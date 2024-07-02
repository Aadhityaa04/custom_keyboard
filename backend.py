import serial.tools.list_ports
def get_com_ports():
  com_ports = serial.tools.list_ports.comports()
  if com_ports:
    for _ in com_ports:
      print(_)
  else:
    print("None")