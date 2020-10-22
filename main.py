from lib import *


#if __name__ == '__main__':
    # task 1
    #img = cv2.imread('images/oka.jpg')
   # cv2.imshow('Image', img)
  #  cv2.waitKey(0)
 #   cv2.imshow('Image', add_gaussian_noise(image=img, mu=20, sigma=15))
 #   cv2.waitKey(0)
 #   cv2.destroyAllWindows()
#a=[]
#check_sort(a)

if __name__ == '__main__':
#task 2
	img = cv2.imread('images/noise.jpg')
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	result = calcNewImage(image = img)
	cv2.imshow('ImageFil', result)
	cv2.waitKey(0)
	cv2.imwrite('images/ImageMedianFilter.png', result)
	cv2.destroyAllWindows()
