import serial
serialFromArduino = serial.Serial('COM3', 9600)

while True:
    valueFromArduino = serialFromArduino.read()
    print(valueFromArduino)
