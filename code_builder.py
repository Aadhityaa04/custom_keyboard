import json
import os


if os.path.exists("config.json"):
    with open("config.json", "r") as file:
        content = json.load(file)
        with open("code.ino", "w") as arduino_code:
            arduino_code.write("")
        with open("code.ino", "a") as arduino_code:

            # Adding Libraries
            arduino_code.write("#include <HID-Project.h> \n\n// Define pin constants\n")
            
            # Define pin constants
            for key in content:
                arduino_code.write(f"const int {key} = {content[key][0]};\n")
            
            # Variables to hold the last state of the buttons
            arduino_code.write("\n// Variables to hold the last state of the buttons\n")
            for key in content:
                arduino_code.write(f"bool lastState{key} = HIGH;\n")

            # setup function
            arduino_code.write("\nvoid setup() {\n")
            arduino_code.write("\tSerial.begin(9600);\n\tKeyboard.begin();\n\tConsumer.begin();\n\n")
            for key in content:
                arduino_code.write(f"\tpinMode({key}, INPUT_PULLPU);\n")
            arduino_code.write("}\n")
            
            # loop function
            arduino_code.write("\nvoid loop() {\n")
            for key in content:
                arduino_code.write(f"\tbool currentState{key} = digitalRead({key});\n")
            arduino_code.write("\n")
            for key in content:
                arduino_code.write(f"\tif (currentState{key} == LOW && lastState{key} == HIGH) {{\n")
    
                arduino_code.write(f"\t\tKeyboard.press({content[key][1]});\n")
                arduino_code.write(f"\t\tdelay(100);\n")
                arduino_code.write(f"\t\tKeyboard.releaseAll();\n")

                arduino_code.write("\t\t}\n")
            arduino_code.write("}\n")

else:
    print("Config.json file missing")