from lib import *

def main():
	menu()


def menu():
	print(
		"""
		0. Exit.
		1. Task 1. Noise
		2. Task 2. Medianfilter

		"""
	)

	while True:
		input_symbol = int(input('Task >>> '))
		if input_symbol == 0:
			break
		if input_symbol == 1:
			Noise()
		elif input_symbol == 2:
			Medianfilter()

#if __name__ == '__main__':
def Noise():
	#task 1
	img = cv2.imread('images/oka.jpg')
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.imshow('Image', add_gaussian_noise(image=img, mu=20, sigma=15))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def Medianfilter():
#task 2
	img = cv2.imread('images/noise.jpg')
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	e1 = cv2.getTickCount()
	result = calcNewImage(image = img)
	e2 = cv2.getTickCount()
	time = (e2 - e1) / cv2.getTickFrequency()
	print(time,"sec")
	cv2.imshow('ImageFil', result)
	cv2.waitKey(0)
	cv2.imwrite('images/ImageMedianFilter.png', result)
	cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
