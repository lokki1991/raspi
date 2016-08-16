import serial
def read_rfid():
        ser = serial.Serial("/dev/ttyS0")
        ser.baudrate = 9600
        daten = ser.read(14)
        daten = daten.replace("/x02", "" )
        daten = daten.replace("/x03", "" )
        return daten
test = read_rfid()
print (test)
