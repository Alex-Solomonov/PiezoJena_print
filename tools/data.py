import typing
import numpy as np

try:
	from PIL import Image
except ImportError:
	from pip._internal import main as pip
	pip(['install', '--user', 'Pillow'])
	from PIL import Image

try:
	from PIL.ImageOps import grayscale
except ImportError:
	from pip._internal import main as pip
	pip(['install', '--user', 'Pillow'])
	from PIL.ImageOps import grayscale

__author__ = "Alexander Solomonov"
__maintainer__  = "Alexander Solomonov"
__email__ = "solomonoff.alexandr@gmail.com"

def load_image(file_path: str) -> np.ndarray:
	'''
	Load RGB image and convert into normalize grayscale array

	Parameters
	----------
	file_path : string
		File name of the image which contain name, fileformat and path

	Returns
	-------
	img_data : ndarray
		array in grayscale format

	'''

	img = Image.open(file_path)# type(img) -- <class 'PIL.*ImagePlugin.*ImageFile'
	img_data = np.array(grayscale(img)) # type(img_data) -- <class 'numpy.ndarray'>
	
	return img_data/np.max(img_data)

def load_image_as_thumbnail(file_path: str, size: tuple) -> np.ndarray:
	'''
	Load RGB image and convert into normalize grayscale array as thumbnail

	Parameters
	----------
	file_path : string
		File name of the image which contain name, fileformat and path

	Returns
	-------
	img_data : ndarray
		array in grayscale format

	'''
	img = Image.open(file_path)# type(img) -- <class 'PIL.*ImagePlugin.*ImageFile'
	img = grayscale(img)# convert RGB image to grayscale
	img.thumbnail(size)
	img_data = np.array(img)
	'''
	TODO:

	Find optimal algorithm of removing gray 
	'''
	img_data[img_data >= 122.5] = 255
	img_data[img_data <= 122.5] = 0

	return img_data/np.max(img_data)


def get_coordinates(array: np.ndarray, length: float = 80.) -> np.ndarray:
	'''
	Get coordinate of offset from zero pont

	Parameters
	----------
	array : ndarray
		An image in the form of a matrix of binary values

	length : optional, float
		The length of the longest side of the image in physical space

	Returns
	-------
	coordinates : ndarray
		The coordinates to which the piezocontroller should move

	'''

	shape = np.shape(array) 

	#Set scale to other size of image in physical space
	scale = shape[1]/shape[0]
	if scale <= 1:
		y_length  = scale*length
	else:
		y_length = length/scale

	#Step of piezocontroller
	dx = length/shape[1]
	dy = y_length/shape[0]

	#Searches for indices of black pixels in the image
	row_coord, col_coord = np.where(array == 0)
	coordinates = np.zeros([np.size(row_coord), 2])
	for i in range(np.size(row_coord)):
		coordinates[i, 0] = col_coord[i]*dx
		coordinates[i, 1] = (shape[0] - row_coord[i])*dy

	return coordinates