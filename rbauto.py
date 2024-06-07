print("Hello, World!")
sequenceList = [
    {'name': '10-5-Go', 'interval': 5, 'warning': [-10, -5]},
    {'name': '5-4-1-Go', 'interval': 5, 'warning': [-5, -4, -1]},
    {'name': '3-2-1-Go', 'interval': 4, 'warning': [-3, -2, -1]}
]

sequenceListLights = [
    {'name': 'No lights', 'on': 0, 'flash': 0},
    {'name': 'On: 1m, Flash: 10s', 'on': -60, 'flash': -10},
]
# def my_function():
  # print("Hello from a function") 
  
activeSeq = [0,0]









# #!/usr/bin/python

# # A simple Python application for controlling a relay board from a Raspberry Pi
# # The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# # The relay is connected to one of the Pi's GPIO ports, then is defined as an Output device
# # in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

# import sys
# import time

# # Make sure you install required libraries:
# # https://gpiozero.readthedocs.io/en/stable/installing.html
# import gpiozero

# # change this value based on which GPIO port the relay is connected to
# RELAY_PIN = 18

# # create a relay object.
# # Triggered by the output pin going low: active_high=False.
# # Initially off: initial_value=False
# relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)


# def set_relay(status):
#     if status:
#         print("Setting relay: ON")
#         relay.on()
#     else:
#         print("Setting relay: OFF")
#         relay.off()


# def toggle_relay():
#     print("toggling relay")
#     relay.toggle()


# def main_loop():
#     # start by turning the relay off
#     set_relay(False)
#     while 1:
#         # then toggle the relay every second until the app closes
#         toggle_relay()
#         # wait a second 
#         time.sleep(1)


# if __name__ == "__main__":
#     try:
#         main_loop()
#     except KeyboardInterrupt:
#         # turn the relay off
#         set_relay(False)
#         print("\nExiting application\n")
#         # exit the application
#         sys.exit(0)