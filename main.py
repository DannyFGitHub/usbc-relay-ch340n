from time import sleep
import serial
import serial


# Open : b'\xA0\x01\x01\xA2'
# Close : b'\xA0\x01\x00\xA1'
# or as a list of integers
# Open : [160, 1, 1, 162]
# Close : [160, 1, 0, 161]

# Write a program that conncets to '/dev/tty.wchusbserial1420', at baud rate 9600 (9800 to 10000 works quite well and faster)
# 9800 is also more reliable

try: 
    while True:
            # Connect to the serial port
            # Ask the user if they want to open or close the door
            user_input = input("On or Off?: >")
            # If the user wants to open the door, send the open command
            if user_input == "on":
                with serial.Serial(port='/dev/tty.wchusbserial1420', baudrate=9900) as ser:
                    ser.write([160, 1, 1, 162])
                    ser.close()
            # If the user wants to close the door, send the close command
            elif user_input == "off":
                with serial.Serial(port='/dev/tty.wchusbserial1420', baudrate=9900) as ser:
                    ser.write([160, 1, 0, 161])
                    ser.close()
            # If the user wants to quit, exit the program
            elif user_input == "quit":
                break
            # If the user enters something else, print an error message
            else:
                print("Invalid input")
            sleep(0.1)
except Exception as e:
    print("Closing: ", e)
finally:
    ser.close()
    print("Done")


# Try to turn on the light with every baudrate in baudrates list
# If the light turns on, print the baudrate and break out of the loop

# After testing the three most responsive are: 9800, 9900, 10000
# baudrates = [9600, 9700, 9800, 9900, 10000]
# for baudrate in baudrates:
#     print("Trying baudrate: ", baudrate)
#     print("On")
#     with serial.Serial(port='/dev/tty.wchusbserial1420', baudrate=baudrate) as ser:
#         ser.write([160, 1, 1, 162])
#         ser.close()
#     sleep(0.5)
#     print("Off")
#     with serial.Serial(port='/dev/tty.wchusbserial1420', baudrate=baudrate) as ser:
#         ser.write([160, 1, 0, 161])
#         ser.close()
#     sleep(0.5)

