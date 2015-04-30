import serial, time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

RTS = 29
CTS = 31
SW = 35
HW = 37
MLDP = 33

out_pins = [HW,SW,MLDP]
FC_pins = [CTS,RTS]
for pin in out_pins:
	pi.set_mode(pin,pi.OUTPUT)
for pin in FC_pins:
	pi.set_mode(pin,pi.ALT3)

pi.write(MLDP,1)
pi.write(SW,1)

ble = serial.Serial('/dev/ttyAMA0',baudrate = 921600,timeout = 0.1)
time.sleep(1)
print ble.readline().strip()
ble.write('SR,3a004800\n')
print ble.readline().strip()
print ble.readline().strip()
ble.write('R,1\n')
time.sleep(1)
time.sleep(0.5)
print ble.readline().strip()
print ble.readline().strip()
ble.write('A\n')
time.sleep(0.5)
print ble.readline().strip()
print ble.readline().strip()
resp = ''
while not 'passcode' in resp.lower():
	resp += ble.readline()
print resp
resp = ''
while not 'connected' in resp.lower():
	resp += ble.readline()
print resp
time.sleep(0.2)
ble.write('I\n')
print ble.readline().strip()
print ble.readline().strip()
print ble.readline().strip()
