from lib import *


if __name__ == '__main__':
    # task 1
    img = cv2.imread('images/oka.jpg')
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.imshow('Image', add_gaussian_noise(image=img, mu=2, sigma=15))
    cv2.waitKey(0)
    cv2.destroyAllWindows()