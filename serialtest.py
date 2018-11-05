import serial

port = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout=3.0)
#port.write("mac join otaa")
#serial.delay(10000)
port.write("mac tx ucnf 10 68656C6C")

while True:
    print(port.read(30))
