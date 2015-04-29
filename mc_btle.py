import serial, time, rn4020, uuid
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

for pin in [HW,MLDP]:
	gpio.output(pin,gpio.LOW)
gpio.output(SW,gpio.HIGH)

# Create the object, use the built-in serial port of a Raspberry Pi
ble = rn4020.RN4020P('/dev/ttyAMA0')

# Generate UUIDs for a user service with two characteristics
suuid = uuid.uuid4()
cuuid = [uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]

# Set up the BLE with a standard device information and a custom service
ble.setup({
  'name': 'test_mod',
  'serialize_name': True,
  'device_information': {
    'manufacturer': 'eCouture',
    'model': 'bracelet',
    'hardware': '1.0',
    'software': '0.1'
  },
  'services': ['device_information', 'user'],
  'user_service': {
    'uuid':suuid,
    'characteristics': [
      { 'uuid': cuuid[0], 'properties': ['read', 'notify'], 'size': 2 },
      { 'uuid': cuuid[1], 'properties': ['read', 'write'], 'size': 4 },
      { 'uuid': cuuid[2], 'properties': ['read'], 'size': 6 }
    ]
  }
})

gpio.cleanup()
