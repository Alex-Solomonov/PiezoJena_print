try:
	import serial
except ImportError:
	from pip._internal import main as pip
	pip(['install', '--user', 'pyserial'])
	import serial

import typing

__author__ = "Alexander Solomonov"
__maintainer__  = "Alexander Solomonov"
__email__ = "solomonoff.alexandr@gmail.com"

def connect(com_port: str, remote: bool = True) -> None:
	'''
	Connect to current controller and 

	Parameters
	----------
	com_port : string
		Port name for connection

	remote : optional, bool
		Set regime of control
		Default is true mean remote control of piezocontroller

	Returns
	-------
	None

	'''

	with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
		'''
		str(int(Bool)) return int bool state in string

		'''

		input_code = str(int(remote))

		command = 'setk,0,'+input_code+'\r' #x_axis
		ser.write(command.encode())
		command = 'setk,1,'+input_code+'\r' #y_axis
		ser.write(command.encode())
		command = 'setk,2,'+input_code+'\r' #z_axis
		ser.write(command.encode())

		if remote:
			print('Remote control set\n')
		else:
			print('Manual control set\n')