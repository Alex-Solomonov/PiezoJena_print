import tools.controller as controller
import tools.data as data
import numpy as np
import matplotlib.pyplot as plt
# Parameters
com_port = 'COM3' #See at Computer Management/Ports

#Exposure time in seconds
delay_time = 0.1
#Longest side length
length_of_side = 40. #mkm

image_name = 'example\\logo.png'
size = 128, 128

	
# controller.connect(com_port, True)

image = data.load_image_as_thumbnail(image_name, size)
# image = data.load_image(image_name) #for small image only

listofcoord =  data.get_coordinates(image, length_of_side)
print(listofcoord)

plt.plot(listofcoord[:,0], listofcoord[:,1])
plt.plot(listofcoord[:,0], listofcoord[:,1], '*')
plt.show()

# controller.draw(com_port, listofcoord, delay_time)
