# import serial.tools.list_ports

# def get_com_ports():
#   """
#   Retrieves a list of connected serial devices using pyserial.

#   Returns:
#       list: A list of tuples containing information about connected serial devices.
#   """

#   # Get a list of connected ports
#   ports = serial.tools.list_ports.comports()
#   return ports

# if __name__ == "__main__":
#   com_ports = get_com_ports()
#   if com_ports:
#     print("Connected serial devices:")
#     for port, desc, hwid in com_ports:
#       print(f"- Port: {port}")
#   else:
#     print("No serial devices found.")



import customtkinter

win = customtkinter.CTk()
win.geometry("200x400")
customtkinter.set_default_color_theme("blue")
btn = customtkinter.CTkButton(win, text="✅", corner_radius=100, width=20, height=20)
btn.pack()
win.mainloop()