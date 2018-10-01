import serial
data=serial.Serial('COM3',9600)
if data.inWaiting>0:
  c=data.readline()
  print(a)
