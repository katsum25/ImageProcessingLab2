import cv2
import numpy as np
import copy as cp

def add_gaussian_noise(image, mu, sigma):
    res_image = cp.copy(image)
    width, height, channel = image.shape
    noise = np.random.normal(mu, sigma, size=(width, height))
    for c in range(channel):
        res_image[:, :, c] = res_image[:, :, c] + noise
    return res_image