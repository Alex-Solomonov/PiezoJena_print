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
	Load RGB image and convert into grayscale array
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
	return img_data