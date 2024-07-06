import serial.tools.list_ports
import json
import customtkinter
import os
from tkinter import filedialog, messagebox
import code_builder
import threading
from pynput import keyboard



command_sequence = []
clear_timeout = 0.5
timer = None
lst = []
keys = []
com_port_selected = None


def get_com_ports():
    com_ports = serial.tools.list_ports.comports()
    if com_ports:
        disp_comports(com_ports)
    else:
        messagebox.showwarning("Warning", message="No device Found")


def update_command_to_json(switch_number, command):
    if "EN" not in str(switch_number):
      if os.path.exists("config.json"):
          with open("config.json", "r") as file:
              content = json.load(file)
          if f"SW{switch_number}" in content:
              content[f"SW{switch_number}"][1] = command
              with open("config.json", "w") as file:
                  json.dump(content, file, indent=4)
          else:
              content[f"SW{switch_number}"] = code_builder.default_config[f"SW{switch_number}"]
              content[f"SW{switch_number}"][1] = command
              with open("config.json", "w") as file:
                  json.dump(content, file, indent=4)
    else:
        if os.path.exists("config.json"):
          with open("config.json", "r") as file:
              content = json.load(file)
          if f"{switch_number}" in content:
              content[f"{switch_number}"][1] = command
              with open("config.json", "w") as file:
                  json.dump(content, file, indent=4)
          else:
              content[f"{switch_number}"] = code_builder.default_config[f"{switch_number}"]
              content[f"{switch_number}"][1] = command
              with open("config.json", "w") as file:
                  json.dump(content, file, indent=4)


def encoder_command(encoder):
    win = customtkinter.CTk()
    win.geometry("250x190")
    win.title(f"Encoder ctrl {encoder}")
    win.resizable(False, False)
    btn1 = customtkinter.CTkButton(master=win, text="Media Fast Forward/Rewind", width=200, command=lambda:[update_command_to_json(f"EN{encoder}", "Rewind"), win.destroy()])
    btn2 = customtkinter.CTkButton(master=win, text="Media Next/Prev", width=200, command=lambda:[update_command_to_json(f"EN{encoder}", "Next"), win.destroy()])
    btn3 = customtkinter.CTkButton(master=win, text="Media Volume Up/Down", width=200, command=lambda:[update_command_to_json(f"EN{encoder}", "Volume"), win.destroy()])
    btn4 = customtkinter.CTkButton(master=win, text="Screen brightness Up/Down", width=200, command=lambda:[update_command_to_json(f"EN{encoder}", "brightness"), win.destroy()])
    btn1.place(x=30, y=20)
    btn2.place(x=30, y=60)
    btn3.place(x=30, y=100)
    btn4.place(x=30, y=140)
    win.mainloop()


def disp_comports(com_ports_list):
    wind = customtkinter.CTk()
    length = len(com_ports_list)
    wind.geometry(f"500x{60 + 40 * (length - 1)}")
    wind.resizable(width=False, height=False)
    wind.title("Select COM Port")
    btn_list = []
    for i, port in enumerate(com_ports_list):
        btn = customtkinter.CTkButton(
            master=wind, text=port, width=300, 
            command=lambda port=port: comport_selected(port, wind)
        )
        btn_list.append(btn)
        btn.place(x=100, y=(15 + 40 * i))
    wind.mainloop()


def comport_selected(port, wind):
    global com_port_selected
    com_port_selected = port[0]
    wind.destroy()


def export_config():
    path = filedialog.asksaveasfile(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    with open("config.json", "r") as file:
        content = json.load(file)
        with open(path.name, "w") as file1:
            json.dump(content, file1, indent=4)


def import_config():
    path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    with open(path, "r") as file:
        with open("config.json", "w") as file1:
            json.dump(json.load(file), file1, indent=4)


def verify_layout():
    win = customtkinter.CTk()
    win.geometry("350x210")
    win.resizable(False, False)
    # x_place = [160, 220, 280]
    # global lst
    # for i in range(9):
    #     lst.append(customtkinter.CTkLabel(win, width=50, height=50, text=i + 1, corner_radius=15, bg_color="#2682cb"))
    #     if i < 3:
    #         lst[i].place(x=x_place[i % 3], y=20)
    #     elif 3 <= i < 6:
    #         lst[i].place(x=x_place[i % 3], y=80)
    #     else:
    #         lst[i].place(x=x_place[i % 3], y=140)

    # threading.Thread(target=start_key_listener, daemon=True).start()
    lab = customtkinter.CTkLabel(win, text="Coming soon")
    lab.place(x=130, y=80)
    win.mainloop()

def start_key_listener():
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    listener.join()  # This will keep the listener running in the background

def on_release(key):
    global timer

    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key).replace("Key.", "")

    if key_char not in command_sequence:
        command_sequence.append(key_char)
        with open("config.json", "r") as file:
            content = json.load(file)
            temp = ""
            for _ in command_sequence:
                temp += f"{_}+"
            temp = temp[:len(temp)-1]
            print(command_sequence)
            for key in content:
                if content[key][1] == temp:
                    print(int(key[2:]))
                    keys.append(int(key[2:]))
    for _ in keys:
        lst[_ - 1].configure(bg_color = "green")

    if timer:
        timer.cancel() 
    timer = threading.Timer(clear_timeout, clear_command_sequence)
    timer.start()

    if key == keyboard.Key.esc:
        return False

def clear_command_sequence():
    global command_sequence
    command_sequence = []
