import pyduinocli

arduino = pyduinocli.Arduino("./arduino-cli")
arduino.compile(r"demo/demo.ino", fqbn="arduino:avr:mega")
arduino.upload(r"demo/demo.ino", fqbn="arduino:avr:mega", port="COM6")
