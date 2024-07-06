import pyduinocli
# import json
# def arduino_upload():
#     arduino = pyduinocli.Arduino("./arduino-cli")
#     try:
#         a = arduino.compile(r"code/code.ino", fqbn = "arduino:avr:micro")
#     except:
#         pass
#     with open("demo.json", "w") as f:
#         json.dump(a, f, indent=4)
#     # print("Success" if "Global variables use" in a else "Error")
#     return a["result"]["success"]
arduino = pyduinocli.Arduino("./arduino-cli")
arduino.upload(r"code/code.ino", fqbn="arduino:avr:micro", port="COM9")
