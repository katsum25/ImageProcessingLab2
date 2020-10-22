import cv2
import numpy as np
import copy as cp
from random import randint 
def check_sort(a:list):
	a = [randint(-100,100) for x in range(50)]
	vstavkasort(a)
	print(a)
	return 0

def add_gaussian_noise(image, mu, sigma):
    res_image = cp.copy(image)
    width, height, channel = image.shape
    noise = np.random.normal(mu, sigma, size=(width, height))
    for c in range(channel):
        res_image[:, :, c] = res_image[:, :, c] + noise
    return res_image

def median_filter(image):
	result_image = cp.copy(image)
	source = cp.copy(image)
	height, width = image.shape[:2]
	vector=[source[0,0]]*9
	for x in range( 1, width - 1):
		for y in range( 1, height - 1):
			vector[0] = source[x-1,y-1]
			vector[1] = source[x,y-1]
			vector[2] = source[x+1,y-1]
			vector[3] = source[x-1,y]
			vector[4] = source[x,y]
			vector[5] = source[x+1,y]
			vector[6] = source[x-1,y+1]
			vector[7] = source[x,y+1]
			vector[8] = source[x+1,y+1]
			#sortvec(vector, 9)
			vector.sort(key = lambda v: v[0]*0.3 + v[1]*0.59 + v[2]*0.11 )
			result_image[x,y]=vector[4]
	return result_image
