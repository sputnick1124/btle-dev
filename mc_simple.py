import serial, time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

RTS = 36
CTS = 38
SW = 35
HW = 37
MLDP = 33

out_pins = [HW,SW,RTS,MLDP]
in_pins = [CTS]
for pin in out_pins:
	gpio.setup(pin,gpio.OUT)
for pin in in_pins:
	gpio.setup(pin,gpio.IN)

gpio.output(MLDP,1)
gpio.output(SW,1)

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
