import json
import os
from tkinter import messagebox

key_mappings = {
    "backspace": "KEY_BACKSPACE",
    "caps_lock": "KEY_CAPS_LOCK",
    "delete": "KEY_DELETE",
    "down": "KEY_DOWN_ARROW",
    "end": "KEY_END",
    "esc": "KEY_ESC",
    "f1": "KEY_F1",
    "f10": "KEY_F10",
    "f11": "KEY_F11",
    "f12": "KEY_F12",
    "f13": "KEY_F13",
    "f14": "KEY_F14",
    "f15": "KEY_F15",
    "f16": "KEY_F16",
    "f17": "KEY_F17",
    "f18": "KEY_F18",
    "f19": "KEY_F19",
    "f2": "KEY_F2",
    "f20": "KEY_F20",
    "f21": "KEY_F21",
    "f22": "KEY_F22",
    "f23": "KEY_F23",
    "f24": "KEY_F24",
    "f3": "KEY_F3",
    "f4": "KEY_F4",
    "f5": "KEY_F5",
    "f6": "KEY_F6",
    "f7": "KEY_F7",
    "f8": "KEY_F8",
    "f9": "KEY_F9",
    "home": "KEY_HOME",
    "insert": "KEY_INSERT",
    "*": "KEY_KP_ASTERISK",
    "enter": "KEY_KP_ENTER",
    "-": "KEY_KP_MINUS",
    "+": "KEY_KP_PLUS",
    "/": "KEY_KP_SLASH",
    ".": "KEY_KP_DOT",
    "alt_l": "KEY_LEFT_ALT",
    "left": "KEY_LEFT_ARROW",
    "ctrl_l": "KEY_LEFT_CTRL",
    "cmd": "KEY_LEFT_GUI",
    "cmd_l": "KEY_LEFT_GUI",
    "shift": "KEY_LEFT_SHIFT",
    "shift_l": "KEY_LEFT_SHIFT",
    "menu": "KEY_MENU",
    "num_lock": "KEY_NUM_LOCK",
    "page_down": "KEY_PAGE_DOWN",
    "page_up": "KEY_PAGE_UP",
    "print_screen": "KEY_PRINT_SCREEN",
    "return": "KEY_RETURN",
    "alt_r": "KEY_RIGHT_ALT",
    "alt_gr": "KEY_RIGHT_ALT",
    "right": "KEY_RIGHT_ARROW",
    "ctrl_r": "KEY_RIGHT_CTRL",
    "cmd": "KEY_RIGHT_GUI",
    "cmd_r": "KEY_RIGHT_GUI",
    "shift_r": "KEY_RIGHT_SHIFT",
    "tab": "KEY_TAB",
    "up": "KEY_UP_ARROW",
    "left": "KEY_LEFT_ARROW",
    "space": "KEY_SPACE",
    "a": "'a'",
    "c": "'c'",
    "b": "'b'",
    "d": "'d'",
    "a": "'a'",
    "c": "'c'",
    "b": "'b'",
    "d": "'d'",
    "e": "'e'",
    "f": "'f'",
    "g": "'g'",
    "h": "'h'",
    "i": "'i'",
    "j": "'j'",
    "k": "'k'",
    "l": "'l'",
    "m": "'m'",
    "n": "'n'",
    "o": "'o'",
    "p": "'p'",
    "q": "'q'",
    "r": "'r'",
    "s": "'s'",
    "t": "'t'",
    "u": "'u'",
    "v": "'v'",
    "w": "'w'",
    "x": "'x'",
    "y": "'y'",
    "z": "'z'",
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
key_mappings1 = {
    "Rewind" : ["MEDIA_FAST_FORWARD", "MEDIA_REWIND"],
    "Next": ["MEDIA_PREV", "MEDIA_NEXT"],
    "Volume": ["MEDIA_VOLUME_DOWN", "MEDIA_VOLUME_UP"],
    "brightness": ["CONSUMER_BRIGHTNESS_DOWN", "CONSUMER_BRIGHTNESS_UP"],
}

default_config = {
    "SW1": [7, "page_down"],
    "SW2": [4, "page_up"],
    "SW3": [2, "page_down"],
    "SW4": [14, "page_up"],
    "SW5": [15, "page_down"],
    "SW6": [18, "page_up"],
    "SW7": [8, "page_down"],
    "SW8": [10,"page_up"],
    "SW9": [16, "page_down"],
    "EN1": [20, "volume_up"],
    "EN2": [21, "brightness_up"],
}
def code_builder():
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            content = json.load(file)
            with open("code/code.ino", "w") as arduino_code:
                arduino_code.write("")
            with open("code/code.ino", "a") as arduino_code:
                ctrl_1_0 = key_mappings1[content["EN1"][1]][0]
                ctrl_1_1 = key_mappings1[content["EN1"][1]][1]
                ctrl_2_0 = key_mappings1[content["EN2"][1]][0]
                ctrl_2_1 = key_mappings1[content["EN2"][1]][1]

                # Adding Libraries
                arduino_code.write("#include <HID-Project.h> \n\n// Define pin constants\n")
                print(content,"\n\n\n\n\n\n\n\n\n\n\n\n")
                # Define pin constants
                for key in content:
                    print(key, type(key))
                    if key != "EN1" and key != "EN2":
                        arduino_code.write(f"const int {key} = {content[key][0]};\n")
                arduino_code.write("#define CLK 3\n#define DT 5\n#define SW A1\n#define LED_ZOOM A2\n#define LED_VOLUME A3\n")
                
                # Variables to hold the last state of the buttons
                arduino_code.write("\n// Variables to hold the last state of the buttons\n")
                for key in content:
                    if key != "EN1" and key != "EN2":
                        arduino_code.write(f"bool lastState{key} = HIGH;\n")
                arduino_code.write('int counter = 0;\nint currentStateCLK;\nint lastStateCLK;\nint btnstate = 0;\nString currentDir = "";\nunsigned long lastButtonPress = 0;\nconst unsigned long debounceDelay = 50;\nbool buttonPressed = false;\n')

                # setup function
                arduino_code.write("\nvoid setup() {\n")
                arduino_code.write("\tSerial.begin(9600);\n\tKeyboard.begin();\n\tConsumer.begin();\n\n")
                for key in content:
                    if key != "EN1" and key != "EN2":
                        arduino_code.write(f"\tpinMode({key}, INPUT_PULLUP);\n")
                arduino_code.write("\tpinMode(CLK, INPUT);\n\tpinMode(DT, INPUT);\n\tpinMode(SW, INPUT_PULLUP);\n\tpinMode(LED_ZOOM, OUTPUT);\n\tpinMode(LED_VOLUME, OUTPUT);\n\tlastStateCLK = digitalRead(CLK);\n")
                arduino_code.write("}\n")
                
                # loop function
                arduino_code.write("\nvoid loop() {\n")
                for key in content:
                    if key != "EN1" and key != "EN2":
                        arduino_code.write(f"\tbool currentState{key} = digitalRead({key});\n")
                arduino_code.write("\n")
                for key in content:
                    if key != "EN1" and key != "EN2":
                        arduino_code.write(f"\n\t// Check if button {key} was pressed\n")
                        arduino_code.write(f"\tif (currentState{key} == LOW && lastState{key} == HIGH) {{\n")
                        temp = content[key][1].split("+")
                        for _ in temp:
                            if _ in key_mappings:
                                arduino_code.write(f"\t\tKeyboard.press({key_mappings[_]});\n")
                        arduino_code.write(f"\t\tdelay(100);\n")
                        arduino_code.write(f"\t\tKeyboard.releaseAll();\n")

                        arduino_code.write("\t}\n")
                arduino_code.write("\t// Update the last state of each button\n")
                for key in content:
                    if key != "EN1" and key != "EN2":
                        arduino_code.write(f"\tlastState{key} = currentState{key};\n")
                arduino_code.write( "\n\tcurrentStateCLK = digitalRead(CLK);\n\tif (currentStateCLK != lastStateCLK && currentStateCLK == 1) {")
                arduino_code.write('\n\t\tif (digitalRead(DT) != currentStateCLK) {\n\t\t\tcounter--;\n\t\t\tcurrentDir = "CCW";\n\t\t} else {\n\t\t\tcounter++;\n\t\t\tcurrentDir = "CW";\n\t\t}')
                arduino_code.write('\n\t// Perform action based on the current mode\n\tif (btnstate == 1) {  // Volume control mode\n\t\tif (currentDir == "CW") {')
                arduino_code.write(f"\n\t\t\tConsumer.write({ctrl_1_0});")
                arduino_code.write('\n\t\t} else if (currentDir == "CCW") {')
                arduino_code.write(f"\n\t\t\tConsumer.write({ctrl_1_1});\n\t\t}}")
                arduino_code.write('\n\t\t} else {  // Zoom control mode\n\t\t\tif (currentDir == "CW") {')
                arduino_code.write(f"\n\t\t\t\tConsumer.write({ctrl_2_0});")
                arduino_code.write(f'\n\t\t\t\tdelay(50);\n\t\t\t\tKeyboard.releaseAll();\n\t\t\t}} else if (currentDir == "CCW") {{')
                arduino_code.write(f"\n\t\t\t\tConsumer.write({ctrl_2_1});")
                arduino_code.write(f'\n\t\t\t\tdelay(50);\n\t\t\t\tKeyboard.releaseAll();')
                arduino_code.write('\n\t\t\t}\n\t\t}\n\t}\n')
                arduino_code.write("\n\t//Encoder handelling\n\tlastStateCLK = currentStateCLK;\n\n\tint buttonState = digitalRead(SW);\n\tif (buttonState == LOW) {\n\t\tif (!buttonPressed) {\n\t\t\tunsigned long currentMillis = millis();")
                arduino_code.write('\n\t\t\tif (currentMillis - lastButtonPress > debounceDelay) {\n\t\t\t\tbtnstate = !btnstate;\n\t\t\t\tif (btnstate) {')
                arduino_code.write('\n\t\t\t\t\tdigitalWrite(LED_VOLUME, HIGH);\n\t\t\t\t\tdigitalWrite(LED_ZOOM, LOW);\n\t\t\t\t} else {')
                arduino_code.write("\n\t\t\t\t\tdigitalWrite(LED_VOLUME, LOW);\n\t\t\t\t\tdigitalWrite(LED_ZOOM, HIGH);\n\t\t\t\t}\n\t\t\t\t// Update the last button press time\n\t\t\t\tlastButtonPress = currentMillis;")
                arduino_code.write("\n\t\t\t\tbuttonPressed = true;")
                arduino_code.write("\n\t\t\t}\n\t\t}\n\t} else {\n")
                arduino_code.write("\t\tbuttonPressed = false;\n\t}")
                arduino_code.write("\n}\n")
                messagebox.showinfo("Build status", message="Code build completed")
    else:
        create_default_config()
        code_builder()
        
def create_default_config():
    with open("config.json", "w") as file:
        json.dump(default_config, file, indent=2)