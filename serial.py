import serial
ser = serial.Serial('/dev/ttyAMA0',115200)
ser.write('a')
exit(0)

