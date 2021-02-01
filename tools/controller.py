try:
	import serial
except ImportError:
	from pip._internal import main as pip
	pip(['install', '--user', 'pyserial'])
	import serial
import numpy as np
from time import sleep
import typing

__author__ = "Alexander Solomonov"
__maintainer__  = "Alexander Solomonov"
__email__ = "solomonoff.alexandr@gmail.com"

def connect(com_port: str, remote: bool = True) -> None:
	'''
	Connect to current controller and set type of control

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

def draw(com_port: str, path_matrix: np.ndarray, delay_time: float) -> None:
	'''
	Connect to current controller and draw

	Parameters
	----------
	com_port : string
		Port name for connection

	path_matrix : array_like
		Array of coordinates

	delay_time:
		Time of exposure

	Returns
	-------
	None

	'''

	with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
		for coord in path_matrix:
			x, y = coord

			command = 'set,0,'+str(x)+'\r' #set x-coord
			ser.write(command.encode())

			command = 'set,1,'+str(y)+'\r' #set y-coord
			ser.write(command.encode())
			sleep(delay_time)