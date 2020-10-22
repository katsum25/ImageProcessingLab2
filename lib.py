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

def calcNewImage(image):
	result_image = cp.copy(image)
	height, width = image.shape[:2]
	vector=[result_image[0,0]]
	for x in range( 1, width - 1):
		for y in range( 1, height - 1):
			vector = calcNewPixelColor(image, x, y)
			result_image[x,y]=vector
	return result_image

def calcNewPixelColor(image, x, y):
	source = cp.copy(image)
	vector=[source[0,0]]*9
	vector[0] = source[x-1,y-1]
	vector[1] = source[x,y-1]
	vector[2] = source[x+1,y-1]
	vector[3] = source[x-1,y]
	vector[4] = source[x,y]
	vector[5] = source[x+1,y]
	vector[6] = source[x-1,y+1]
	vector[7] = source[x,y+1]
	vector[8] = source[x+1,y+1]
	sortvec(vector, 9)
	return vector[4]

def sortvec(vec , n):
	for i in range(n-1):
		for j in range(n-i-1):
			brig1 = vec[j][0]*0.3 + vec[j][1]*0.59 + vec[j][2]*0.11
			brig2 = vec[j+1][0]*0.3 + vec[j+1][1]*0.59 + vec[j+1][2]*0.11
			if brig1 > brig2:
				vec[j], vec[j+1] = vec[j+1], vec[j]
	return vec

